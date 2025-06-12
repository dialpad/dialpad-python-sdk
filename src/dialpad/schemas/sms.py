from typing import Annotated, Literal

from typing_extensions import NotRequired, TypedDict


class SMSProto(TypedDict):
  """SMS message."""

  contact_id: NotRequired[str]
  'The ID of the specific contact which SMS should be sent to.'
  created_date: NotRequired[str]
  'Date of SMS creation.'
  device_type: NotRequired[
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
  direction: NotRequired[Literal['inbound', 'outbound']]
  'SMS direction.'
  from_number: NotRequired[str]
  'The phone number from which the SMS was sent.'
  id: NotRequired[int]
  'The ID of the SMS.'
  message_delivery_result: NotRequired[
    Literal[
      'accepted',
      'internal_error',
      'invalid_destination',
      'invalid_source',
      'no_route',
      'not_supported',
      'rejected',
      'rejected_spam',
      'time_out',
    ]
  ]
  'The final message delivery result.'
  message_status: NotRequired[Literal['failed', 'pending', 'success']]
  'The status of the SMS.'
  target_id: NotRequired[int]
  "The target's id."
  target_type: NotRequired[
    Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ]
  ]
  "Target's type."
  text: NotRequired[str]
  'The contents of the message that was sent.'
  to_numbers: NotRequired[list[str]]
  'Up to 10 E164-formatted phone numbers who received the SMS.'
  user_id: NotRequired[int]
  'The ID of the user who sent the SMS.'


class SendSMSMessage(TypedDict):
  """TypedDict representation of the SendSMSMessage schema."""

  channel_hashtag: NotRequired[str]
  '[single-line only]\n\nThe hashtag of the channel which should receive the SMS.'
  from_number: NotRequired[str]
  'The number of who sending the SMS. The number must be assigned to user or a user group. It will override user_id and sender_group_id.'
  infer_country_code: NotRequired[bool]
  "If true, to_numbers will be assumed to be from the specified user's country, and the E164 format requirement will be relaxed."
  media: NotRequired[Annotated[str, 'base64']]
  'Base64-encoded media attachment (will cause the message to be sent as MMS).\n(Max 500 KiB raw file size)'
  sender_group_id: NotRequired[int]
  'The ID of an office, department, or call center that the User should send the message on behalf of.'
  sender_group_type: NotRequired[Literal['callcenter', 'department', 'office']]
  "The sender group's type (i.e. office, department, or callcenter)."
  text: NotRequired[str]
  'The contents of the message that should be sent.'
  to_numbers: NotRequired[list[str]]
  'Up to 10 E164-formatted phone numbers who should receive the SMS.'
  user_id: NotRequired[int]
  'The ID of the user who should be the sender of the SMS.'
