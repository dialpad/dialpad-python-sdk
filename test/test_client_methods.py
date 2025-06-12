#!/usr/bin/env python

"""Tests to automatically detect common issues with resource definitions.

In particular these tests will look through the files in dialpad-python-sdk/dialpad/resources/ and
ensure:

- All subclasses of DialpadResource are exposed directly in resources/__init__.py
- All resources are available as properties of DialpadClient
- Public methods defined on the concrete subclasses only make web requests that agree with
  the Dialpad API's open-api spec
"""

import logging
from urllib.parse import parse_qs, urlparse

import pytest
import requests
from openapi_core import OpenAPI
from openapi_core.contrib.requests import RequestsOpenAPIRequest
from openapi_core.datatypes import RequestParameters
from werkzeug.datastructures import Headers, ImmutableMultiDict

from dialpad.client import DialpadClient
from dialpad.resources.base import DialpadResource

from .utils import generate_faked_kwargs

logger = logging.getLogger(__name__)


class RequestsMockOpenAPIRequest(RequestsOpenAPIRequest):
  """
  Converts a requests-mock request to an OpenAPI request
  """

  def __init__(self, request):
    self.request = request
    if request.url is None:
      raise RuntimeError('Request URL is missing')
    self._url_parsed = urlparse(request.url, allow_fragments=False)

    self.parameters = RequestParameters(
      query=ImmutableMultiDict(parse_qs(self._url_parsed.query)),
      header=Headers(dict(self.request.headers)),
    )


# The "requests_mock" pytest fixture stubs out live requests with a schema validation check
# against the Dialpad API openapi spec.
@pytest.fixture
def openapi_stub(requests_mock):
  openapi = OpenAPI.from_file_path('dialpad_api_spec.json')

  def request_matcher(request: requests.PreparedRequest):
    openapi.validate_request(RequestsMockOpenAPIRequest(request))

    # Handle pagination for /api/v2/users endpoint
    if '/api/v2/users' in request.url:
      parsed_url = urlparse(request.url)
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

      fake_response = requests.Response()
      fake_response.status_code = 200
      fake_response._content = str.encode(str(response_data).replace("'", '"'))
      return fake_response

    # If the request is valid, return a generic fake response.
    fake_response = requests.Response()
    fake_response.status_code = 200
    fake_response._content = b'{"success": true}'
    return fake_response

  requests_mock.add_matcher(request_matcher)


class TestClientResourceMethods:
  """Smoketest for all the client resource methods to ensure they produce valid requests according
  to the OpenAPI spec."""

  def test_pagination_handling(self, openapi_stub):
    """Verifies that the DialpadClient handles pagination."""

    # Construct a DialpadClient with a fake API key.
    dp = DialpadClient('123')

    _users = list(dp.users.list())
    assert len(_users) == 5, 'Expected to resolve exactly 5 users from paginated responses.'

  def test_request_conformance(self, openapi_stub):
    """Verifies that all API requests produced by this library conform to the spec.

    Although this test cannot guarantee that the requests are semantically correct, it can at least
    determine whether they are well-formed according to the OpenAPI spec.
    """

    # Construct a DialpadClient with a fake API key.
    dp = DialpadClient('123')

    # Iterate through the attributes on the client object to find the API resource accessors.
    for a in dir(dp):
      resource_instance = getattr(dp, a)

      # Skip any attributes that are not DialpadResources
      if not isinstance(resource_instance, DialpadResource):
        continue

      logger.info('Verifying request format of %s methods', resource_instance.__class__.__name__)

      # Iterate through the attributes on the resource instance.
      for method_attr in dir(resource_instance):
        # Skip any methods and attributes that are not unique to this resource class.
        if method_attr in dir(DialpadResource):
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
        if (resource_instance.__class__.__name__, method_attr) == ('NumbersResource', 'swap'):
          # The openapi validator doesn't like that swap_details can be valid under multiple
          # OneOf schemas...
          faked_kwargs['request_body'].pop('swap_details', None)

        if (resource_instance.__class__.__name__, method_attr) == ('FaxLinesResource', 'assign'):
          # The openapi validator doesn't like it if "line" could be valid under multiple schemas.
          faked_kwargs['request_body']['line'] = {'type': 'toll-free'}

        logger.info(
          'Testing resource method %s.%s with faked kwargs: %s',
          resource_instance.__class__.__name__,
          method_attr,
          faked_kwargs,
        )
        try:
          # Call the resource method with the faked kwargs.
          result = resource_method(**faked_kwargs)
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
