
import requests

from cached_property import cached_property

from .resources import (
  AppSettingsResource,
  SMSResource,
  RoomResource,
  UserResource,
  CallResource,
  NumberResource,
  OfficeResource,
  WebhookResource,
  CompanyResource,
  ContactResource,
  CallbackResource,
  CallCenterResource,
  CallRouterResource,
  DepartmentResource,
  TranscriptResource,
  UserDeviceResource,
  StatsExportResource,
  SubscriptionResource,
  BlockedNumberResource,
  EventSubscriptionResource
)


hosts = dict(
  live='https://dialpad.com',
  sandbox='https://sandbox.dialpad.com'
)


class DialpadClient(object):
  def __init__(self, token, sandbox=False, base_url=None, company_id=None):
    self._token = token
    self._session = requests.Session()
    self._base_url = base_url or hosts.get('sandbox' if sandbox else 'live')
    self._company_id = company_id

  @property
  def company_id(self):
    return self._company_id

  @company_id.setter
  def company_id(self, value):
    self._company_id = value

  @company_id.deleter
  def company_id(self):
    del self._company_id

  def _url(self, *path):
    path = ['%s' % p for p in path]
    return '/'.join([self._base_url, 'api', 'v2'] + path)

  def _cursor_iterator(self, response_json, path, method, data, headers):
    for i in response_json['items']:
      yield i

    data = dict(data or {})

    while 'cursor' in response_json:
      data['cursor'] = response_json['cursor']
      response = self._raw_request(path, method, data, headers)
      response.raise_for_status()
      response_json = response.json()
      for i in response_json.get('items', []):
        yield i

  def _raw_request(self, path, method='GET', data=None, headers=None):
    url = self._url(*path)
    headers = headers or dict()
    if self.company_id:
      headers.update({'DP-Company-ID': str(self.company_id)})

    headers.update({'Authorization': 'Bearer %s' % self._token})
    if str(method).upper() in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
      return getattr(self._session, str(method).lower())(
        url,
        headers=headers,
        json=data if method != 'GET' else None,
        params=data if method == 'GET' else None,
      )
    raise ValueError('Unsupported method "%s"' % method)

  def request(self, path, method='GET', data=None, headers=None):
    response = self._raw_request(path, method, data, headers)
    response.raise_for_status()

    if response.status_code == 204:  # No Content
      return None

    response_json = response.json()
    response_keys = set(k for k in response_json)
    # If the response contains the 'items' key, (and maybe 'cursor'), then this is a cursorized
    # list response.
    if 'items' in response_keys and not response_keys - {'cursor', 'items'}:
      return self._cursor_iterator(
        response_json, path=path, method=method, data=data, headers=headers)
    return response_json

  @cached_property
  def app_settings(self):
    return AppSettingsResource(self)

  @cached_property
  def blocked_number(self):
    return BlockedNumberResource(self)

  @cached_property
  def call(self):
    return CallResource(self)

  @cached_property
  def call_router(self):
    return CallRouterResource(self)

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
  def subscription(self):
    return SubscriptionResource(self)

  @cached_property
  def transcript(self):
    return TranscriptResource(self)

  @cached_property
  def user(self):
    return UserResource(self)

  @cached_property
  def userdevice(self):
    return UserDeviceResource(self)

  @cached_property
  def webhook(self):
    return WebhookResource(self)
