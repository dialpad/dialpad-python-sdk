#!/usr/bin/env python

"""Tests to automatically detect common issues with async resource definitions.

In particular these tests will look through the files in dialpad-python-sdk/dialpad/async_resources/ and
ensure:

- All subclasses of AsyncDialpadResource are exposed correctly
- All resources are available as properties of AsyncDialpadClient
- Public methods defined on the concrete subclasses only make web requests that agree with
  the Dialpad API's open-api spec
"""

import inspect
import logging
from typing import AsyncIterator
from urllib.parse import parse_qs, urlparse

import httpx
import pytest
from openapi_core import OpenAPI
from openapi_core.datatypes import RequestParameters
from werkzeug.datastructures import Headers, ImmutableMultiDict

from dialpad.async_client import AsyncDialpadClient
from dialpad.async_resources.base import AsyncDialpadResource

from .utils import generate_faked_kwargs

logger = logging.getLogger(__name__)


class HttpxMockOpenAPIRequest:
  """
  Converts an httpx request to an OpenAPI request
  """

  def __init__(self, request):
    self.request = request
    if request.url is None:
      raise RuntimeError('Request URL is missing')
    self._url_parsed = urlparse(str(request.url), allow_fragments=False)

    self.parameters = RequestParameters(
      query=ImmutableMultiDict(parse_qs(self._url_parsed.query)),
      header=Headers(dict(request.headers)),
    )

  @property
  def host_url(self):
    return f'{self._url_parsed.scheme}://{self._url_parsed.netloc}'

  @property
  def path(self):
    return self._url_parsed.path

  @property
  def method(self):
    return self.request.method.lower()

  @property
  def body(self):
    return self.request.content

  @property
  def content_type(self):
    return self.request.headers.get('content-type', 'application/json')


# The "httpx_mock" pytest fixture stubs out live requests with a schema validation check
# against the Dialpad API openapi spec.
@pytest.fixture
def openapi_stub(httpx_mock):
  openapi = OpenAPI.from_file_path('dialpad_api_spec.json')

  async def request_handler(request: httpx.Request):
    openapi.validate_request(HttpxMockOpenAPIRequest(request))

    # Handle pagination for /api/v2/users endpoint
    if '/api/v2/users' in str(request.url):
      parsed_url = urlparse(str(request.url))
      query_params = parse_qs(parsed_url.query)
      cursor = query_params.get('cursor', [None])[0]

      if cursor is None:
        # First page: 3 users with cursor for next page
        response_data = {
          'items': [
            {'id': 1, 'display_name': 'User 1'},
            {'id': 2, 'display_name': 'User 2'},
            {'id': 3, 'display_name': 'User 3'},
          ],
          'cursor': 'next_page_cursor',
        }
      elif cursor == 'next_page_cursor':
        # Second page: 2 users, no next cursor
        response_data = {
          'items': [{'id': 4, 'display_name': 'User 4'}, {'id': 5, 'display_name': 'User 5'}]
        }
      else:
        # No more pages
        response_data = {'items': []}

      return httpx.Response(200, json=response_data)

    # If the request is valid, return a generic fake response.
    return httpx.Response(200, json={'success': True})

  httpx_mock.add_callback(request_handler, is_reusable=True)


class TestAsyncClientResourceMethods:
  """Smoketest for all the async client resource methods to ensure they produce valid requests according
  to the OpenAPI spec."""

  @pytest.mark.asyncio
  async def test_pagination_handling(self, openapi_stub):
    """Verifies that the AsyncDialpadClient handles pagination."""

    # Construct an AsyncDialpadClient with a fake API key.
    dp = AsyncDialpadClient('123')
    _users = []
    async for user in dp.users.list():
      _users.append(user)

    assert len(_users) == 5, 'Expected to resolve exactly 5 users from paginated responses.'

  @pytest.mark.asyncio
  async def test_request_conformance(self, openapi_stub):
    """Verifies that all API requests produced by this library conform to the spec.

    Although this test cannot guarantee that the requests are semantically correct, it can at least
    determine whether they are well-formed according to the OpenAPI spec.
    """

    # Construct an AsyncDialpadClient with a fake API key.
    dp = AsyncDialpadClient('123')
    # Iterate through the attributes on the client object to find the API resource accessors.
    for a in dir(dp):
      resource_instance = getattr(dp, a)

      # Skip any attributes that are not AsyncDialpadResources
      if not isinstance(resource_instance, AsyncDialpadResource):
        continue

      logger.info('Verifying request format of %s methods', resource_instance.__class__.__name__)

      # Iterate through the attributes on the resource instance.
      for method_attr in dir(resource_instance):
        # Skip any methods and attributes that are not unique to this resource class.
        if method_attr in dir(AsyncDialpadResource):
          continue

        # Skip private attributes.
        if method_attr.startswith('_'):
          continue

        # Skip attributes that are not functions.
        resource_method = getattr(resource_instance, method_attr)
        if not callable(resource_method):
          continue

        # Generate fake kwargs for the resource method.
        faked_kwargs = generate_faked_kwargs(resource_method)
        if (resource_instance.__class__.__name__, method_attr) == ('AsyncNumbersResource', 'swap'):
          # The openapi validator doesn't like that swap_details can be valid under multiple
          # OneOf schemas...
          faked_kwargs['request_body'].pop('swap_details', None)

        if (resource_instance.__class__.__name__, method_attr) == ('AsyncFaxLinesResource', 'assign'):
          # The openapi validator doesn't like it if "line" could be valid under multiple schemas.
          faked_kwargs['request_body']['line'] = {'type': 'toll-free'}

        logger.info(
          'Testing async resource method %s.%s with faked kwargs: %s',
          resource_instance.__class__.__name__,
          method_attr,
          faked_kwargs,
        )
        try:
          # Call the async resource method with the faked kwargs.
          result = resource_method(**faked_kwargs)

          # Check if the result is an async iterator and consume it
          if inspect.isasyncgen(result) or isinstance(result, AsyncIterator):
            items = []
            async for item in result:
              items.append(item)
            result = items
          else:
            result = await result

          logger.info(
            'Result of %s.%s: %s',
            resource_instance.__class__.__name__,
            method_attr,
            result,
          )
        except Exception as e:
          logger.error(
            'Error calling %s.%s with faked kwargs %s: %s',
            resource_instance.__class__.__name__,
            method_attr,
            faked_kwargs,
            e,
          )
          raise
