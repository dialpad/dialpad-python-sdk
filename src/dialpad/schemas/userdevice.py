from typing import Literal

from typing_extensions import NotRequired, TypedDict


class UserDeviceProto(TypedDict):
  """Dialpad user device."""

  app_version: NotRequired[str]
  'The device firmware version, or Dialpad app version.'
  date_created: NotRequired[str]
  'The time at which this device was created.'
  date_registered: NotRequired[str]
  'The most recent time at which the device registered with the backend.\n\nDevices register with the backend roughly once per hour, with the exception of mobile devices\n(iphone, ipad, android) for which this field will always be blank.'
  date_updated: NotRequired[str]
  'The most recent time at which the device data was modified.'
  display_name: NotRequired[str]
  '[single-line only]\n\nThe name of this device.'
  id: NotRequired[str]
  'The ID of the device.'
  phone_number: NotRequired[str]
  'The phone number associated with this device.'
  type: NotRequired[
    Literal[
      'android',
      'ata',
      'audiocodes',
      'c2t',
      'ciscompp',
      'dect',
      'dpmroom',
      'grandstream',
      'harness',
      'iframe_cti_extension',
      'iframe_front',
      'iframe_hubspot',
      'iframe_ms_teams',
      'iframe_open_cti',
      'iframe_salesforce',
      'iframe_service_titan',
      'iframe_zendesk',
      'ipad',
      'iphone',
      'mini',
      'mitel',
      'msteams',
      'native',
      'obi',
      'packaged_app',
      'polyandroid',
      'polycom',
      'proxy',
      'public_api',
      'salesforce',
      'sip',
      'tickiot',
      'web',
      'yealink',
    ]
  ]
  'The device type.'
  user_id: NotRequired[int]
  'The ID of the user who owns the device.'


class UserDeviceCollection(TypedDict):
  """Collection of user devices."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request.\n\nUse the cursor provided in the previous response.'
  items: NotRequired[list[UserDeviceProto]]
  'A list of user devices.'
