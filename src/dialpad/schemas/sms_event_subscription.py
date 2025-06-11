from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.webhook import WebhookProto
from dialpad.schemas.websocket import WebsocketProto


class CreateSmsEventSubscription(TypedDict):
  """TypedDict representation of the CreateSmsEventSubscription schema."""

  direction: Literal['all', 'inbound', 'outbound']
  'The SMS direction this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the SMS event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully."
  include_internal: NotRequired[bool]
  'Whether or not to trigger SMS events for SMS sent between two users from the same company.'
  status: NotRequired[bool]
  'Whether or not to update on each SMS delivery status.'
  target_id: NotRequired[int]
  'The ID of the specific target for which events should be sent.'
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
  "The target's type."


class SmsEventSubscriptionProto(TypedDict):
  """TypedDict representation of the SmsEventSubscriptionProto schema."""

  direction: NotRequired[Literal['all', 'inbound', 'outbound']]
  'The SMS direction this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the SMS event subscription is enabled.'
  id: NotRequired[int]
  'The ID of the SMS event subscription.'
  include_internal: NotRequired[bool]
  'Whether or not to trigger SMS events for SMS sent between two users from the same company.'
  status: NotRequired[bool]
  'Whether or not to update on each SMS delivery status.'
  target_id: NotRequired[int]
  'The ID of the specific target for which events should be sent.'
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
  "The target's type."
  webhook: NotRequired[WebhookProto]
  "The webhook that's associated with this event subscription."
  websocket: NotRequired[WebsocketProto]
  "The websocket's ID, which is generated after creating a webhook successfully."


class SmsEventSubscriptionCollection(TypedDict):
  """Collection of sms event subscriptions."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[SmsEventSubscriptionProto]]
  'A list of SMS event subscriptions.'


class UpdateSmsEventSubscription(TypedDict):
  """TypedDict representation of the UpdateSmsEventSubscription schema."""

  direction: NotRequired[Literal['all', 'inbound', 'outbound']]
  'The SMS direction this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the SMS event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,\nplease provide a valid webhook ID here."
  include_internal: NotRequired[bool]
  'Whether or not to trigger SMS events for SMS sent between two users from the same company.'
  status: NotRequired[bool]
  'Whether or not to update on each SMS delivery status.'
  target_id: NotRequired[int]
  'The ID of the specific target for which events should be sent.'
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
  "The target's type."
