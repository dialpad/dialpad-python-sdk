#!/usr/bin/env python

"""Tests for the request plumbing that every resource method goes through.

In particular these tests ensure:

- Requests are sent with a timeout, so that an unanswered request cannot block the caller forever
- A headers dict supplied by the caller is not modified (and so never ends up holding the API token)
- The company_id can be deleted without breaking subsequent requests
"""

import httpx
import pytest

from dialpad import async_client, client
from dialpad.async_client import AsyncDialpadClient
from dialpad.client import DialpadClient

USER_PATH = '/api/v2/users/1'
USER_URL = 'https://dialpad.com' + USER_PATH


class TestClientRequests:
  """Verifies the request handling of the DialpadClient."""

  def test_default_timeout(self, requests_mock):
    """Verifies that requests are sent with a timeout by default."""
    requests_mock.get(USER_URL, json={'id': 1})

    DialpadClient('123').users.get('1')

    assert requests_mock.last_request.timeout == client.DEFAULT_TIMEOUT

  def test_custom_timeout(self, requests_mock):
    """Verifies that the timeout argument is respected, including None to disable it."""
    requests_mock.get(USER_URL, json={'id': 1})

    DialpadClient('123', timeout=5).users.get('1')
    assert requests_mock.last_request.timeout == 5

    DialpadClient('123', timeout=None).users.get('1')
    assert requests_mock.last_request.timeout is None

  def test_caller_headers_are_not_modified(self, requests_mock):
    """Verifies that the auth headers are not written into the caller's headers dict."""
    requests_mock.get(USER_URL, json={'id': 1})
    headers = {'X-Trace': 'abc'}

    dp = DialpadClient('123', company_id='42')
    dp.request(method='GET', sub_path=USER_PATH, headers=headers)

    assert headers == {'X-Trace': 'abc'}

    sent_headers = requests_mock.last_request.headers
    assert sent_headers['X-Trace'] == 'abc'
    assert sent_headers['Authorization'] == 'Bearer 123'
    assert sent_headers['DP-Company-ID'] == '42'

  def test_company_id_can_be_deleted(self, requests_mock):
    """Verifies that requests still work after the company_id has been deleted."""
    requests_mock.get(USER_URL, json={'id': 1})

    dp = DialpadClient('123', company_id='42')
    del dp.company_id

    assert dp.company_id is None
    dp.users.get('1')
    assert 'DP-Company-ID' not in requests_mock.last_request.headers


class TestAsyncClientRequests:
  """Verifies the request handling of the AsyncDialpadClient."""

  @pytest.mark.asyncio
  async def test_default_timeout(self, httpx_mock):
    """Verifies that requests are sent with a timeout by default."""
    httpx_mock.add_response(url=USER_URL, json={'id': 1})

    await AsyncDialpadClient('123').users.get('1')

    expected = httpx.Timeout(async_client.DEFAULT_TIMEOUT).as_dict()
    assert httpx_mock.get_request().extensions['timeout'] == expected

  @pytest.mark.asyncio
  async def test_custom_timeout(self, httpx_mock):
    """Verifies that the timeout argument is respected, including None to disable it."""
    httpx_mock.add_response(url=USER_URL, json={'id': 1}, is_reusable=True)

    await AsyncDialpadClient('123', timeout=5).users.get('1')
    assert httpx_mock.get_requests()[-1].extensions['timeout'] == httpx.Timeout(5).as_dict()

    await AsyncDialpadClient('123', timeout=None).users.get('1')
    assert httpx_mock.get_requests()[-1].extensions['timeout'] == httpx.Timeout(None).as_dict()

  @pytest.mark.asyncio
  async def test_caller_headers_are_not_modified(self, httpx_mock):
    """Verifies that the auth headers are not written into the caller's headers dict."""
    httpx_mock.add_response(url=USER_URL, json={'id': 1})
    headers = {'X-Trace': 'abc'}

    dp = AsyncDialpadClient('123', company_id='42')
    await dp.request(method='GET', sub_path=USER_PATH, headers=headers)

    assert headers == {'X-Trace': 'abc'}

    sent_headers = httpx_mock.get_request().headers
    assert sent_headers['X-Trace'] == 'abc'
    assert sent_headers['Authorization'] == 'Bearer 123'
    assert sent_headers['DP-Company-ID'] == '42'

  @pytest.mark.asyncio
  async def test_company_id_can_be_deleted(self, httpx_mock):
    """Verifies that requests still work after the company_id has been deleted."""
    httpx_mock.add_response(url=USER_URL, json={'id': 1})

    dp = AsyncDialpadClient('123', company_id='42')
    del dp.company_id

    assert dp.company_id is None
    await dp.users.get('1')
    assert 'DP-Company-ID' not in httpx_mock.get_request().headers
