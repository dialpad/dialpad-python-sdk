from typing import Literal

from typing_extensions import NotRequired, TypedDict


class DeskPhone(TypedDict):
  """Desk phone."""

  byod: NotRequired[bool]
  'Boolean indicating whether this desk phone was purchased through Dialpad.'
  device_model: NotRequired[str]
  '[single-line only]\n\nThe model name of the device.'
  firmware_version: NotRequired[str]
  '[single-line only]\n\nThe firmware version currently loaded onto the device.'
  id: NotRequired[str]
  'The ID of the desk phone.'
  mac_address: NotRequired[str]
  '[single-line only]\n\nThe MAC address of the device.'
  name: NotRequired[str]
  '[single-line only]\n\nA user-prescibed name for this device.'
  owner_id: NotRequired[int]
  'The ID of the device owner.'
  owner_type: NotRequired[Literal['room', 'user']]
  'The entity type of the device owner.'
  password: NotRequired[str]
  '[single-line only]\n\nA password required to make calls on with the device.'
  phone_number: NotRequired[str]
  'The phone number associated with this device.'
  port: NotRequired[int]
  'The SIP port number.'
  realm: NotRequired[str]
  'The SIP realm that this device should use.'
  ring_notification: NotRequired[bool]
  'A boolean indicating whether this device should ring when the user receives a call.'
  sip_transport_type: NotRequired[Literal['tls']]
  'The SIP transport layer protocol.'
  type: NotRequired[
    Literal[
      'ata',
      'audiocodes',
      'c2t',
      'ciscompp',
      'dect',
      'grandstream',
      'mini',
      'mitel',
      'obi',
      'polyandroid',
      'polycom',
      'sip',
      'tickiot',
      'yealink',
    ]
  ]
  'User phone, or room phone.'


class DeskPhoneCollection(TypedDict):
  """Collection of desk phones."""

  items: NotRequired[list[DeskPhone]]
  'A list of desk phones.'
