import os
import requests

from cached_property import cached_property

from .resources import UserResource, SMSResource


class DialpadClient(object):
  def __init__(self, token, beta=False, base_url=None):
    self._token = token
    if base_url is not None:
      self._base_url = base_url
    else:
      self._base_url = 'https://dialpadbeta.com' if beta else 'https://dialpad.com'

  def _url(self, *path):
    path = ['%s' % p for p in path]
    return os.path.join(self._base_url, 'api', 'v2', *path)

  def _cursor_iterator(self, response_json, path, method, data, headers):
    for i in response_json['items']:
      yield i

    data = dict(data)

    while 'cursor' in response_json:
      data['cursor'] = response_json['cursor']
      response = self._raw_request(path, method, data, headers)
      response.raise_for_status()
      response_json = response.json()
      for i in response_json['items']:
        yield i

  def _raw_request(self, path, method='GET', data=None, headers=None):
    url = self._url(*path)
    headers = headers or {}
    headers['Authorization'] = 'Bearer %s' % self._token
    if method == 'GET':
      return requests.get(url, params=data, headers=headers)

    if method == 'POST':
      return requests.post(url, json=data, headers=headers)

    if method == 'PATCH':
      return requests.patch(url, json=data, headers=headers)

    if method == 'DELETE':
      return requests.delete(url, headers=headers)

    raise ValueError('Unsupported method "%s"' % method)

  def request(self, path, method='GET', data=None, headers=None):
    response = self._raw_request(path, method, data, headers)
    response.raise_for_status()

    response_json = response.json()
    response_keys = set(k for k in response_json)
    # If the response contains the 'items' key, (and maybe 'cursor'), then this is a cursorized
    # list response.
    if 'items' in response_keys and not response_keys - {'cursor', 'items'}:
      return self._cursor_iterator(response_json, path=path, method=method, data=data, headers=headers)
    return response_json

  @cached_property
  def users(self):
    return UserResource(self)

  @cached_property
  def sms(self):
    return SMSResource(self)
