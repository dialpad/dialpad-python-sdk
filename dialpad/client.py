import os
import requests

from cached_property import cached_property

from .resources import BlockedNumberResource
from .resources import CallResource
from .resources import CallbackResource
from .resources import CallCenterResource
from .resources import CompanyResource
from .resources import ContactResource
from .resources import DepartmentResource
from .resources import EventSubscriptionResource
from .resources import NumberResource
from .resources import OfficeResource
from .resources import RoomResource
from .resources import SMSResource
from .resources import StatsExportResource
from .resources import TranscriptResource
from .resources import UserResource
from .resources import UserDeviceResource


class DialpadClient(object):
  def __init__(self, token, sandbox=False, base_url=None):
    self._token = token
    if base_url is not None:
      self._base_url = base_url
    else:
      self._base_url = 'https://sandbox.dialpad.com' if sandbox else 'https://dialpad.com'

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

    if method == 'PUT':
      return requests.put(url, json=data, headers=headers)

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
  def blocked_number(self):
    return BlockedNumberResource(self)

  @cached_property
  def call(self):
    return CallResource(self)

  @cached_property
  def callback(self):
    return CallbackResource(self)

  @cached_property
  def callcenter(self):
    return CallCenterResource(self)

  @cached_property
  def company(self):
    return CompanyResource(self)

  @cached_property
  def contact(self):
    return ContactResource(self)

  @cached_property
  def department(self):
    return DepartmentResource(self)

  @cached_property
  def event_subscription(self):
    return EventSubscriptionResource(self)

  @cached_property
  def number(self):
    return NumberResource(self)

  @cached_property
  def office(self):
    return OfficeResource(self)

  @cached_property
  def room(self):
    return RoomResource(self)

  @cached_property
  def sms(self):
    return SMSResource(self)

  @cached_property
  def stats(self):
    return StatsExportResource(self)

  @cached_property
  def transcript(self):
    return TranscriptResource(self)

  @cached_property
  def user(self):
    return UserResource(self)

  @cached_property
  def userdevice(self):
    return UserDeviceResource(self)
