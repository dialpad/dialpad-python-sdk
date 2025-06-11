from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.webhook import WebhookProto
from dialpad.schemas.websocket import WebsocketProto


class CallEventSubscriptionProto(TypedDict):
  """Call event subscription."""

  call_states: NotRequired[
    list[
      Literal[
        'admin',
        'admin_recording',
        'ai_playbook',
        'all',
        'barge',
        'blocked',
        'call_transcription',
        'calling',
        'connected',
        'csat',
        'dispositions',
        'eavesdrop',
        'hangup',
        'hold',
        'merged',
        'missed',
        'monitor',
        'parked',
        'pcsat',
        'postcall',
        'preanswer',
        'queued',
        'recap_action_items',
        'recap_outcome',
        'recap_purposes',
        'recap_summary',
        'recording',
        'ringing',
        'takeover',
        'transcription',
        'voicemail',
        'voicemail_uploaded',
      ]
    ]
  ]
  "The call event subscription's list of call states."
  enabled: NotRequired[bool]
  'Whether or not the call event subscription is enabled.'
  group_calls_only: NotRequired[bool]
  'Call event subscription for group calls only.'
  id: NotRequired[int]
  "The event subscription's ID, which is generated after creating an event subscription successfully."
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
  'The target type.'
  webhook: NotRequired[WebhookProto]
  "The webhook that's associated with this event subscription."
  websocket: NotRequired[WebsocketProto]
  "The websocket's ID, which is generated after creating a webhook successfully."


class CallEventSubscriptionCollection(TypedDict):
  """Collection of call event subscriptions."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[CallEventSubscriptionProto]]
  'A list of call event subscriptions.'


class CreateCallEventSubscription(TypedDict):
  """TypedDict representation of the CreateCallEventSubscription schema."""

  call_states: NotRequired[
    list[
      Literal[
        'admin',
        'admin_recording',
        'ai_playbook',
        'all',
        'barge',
        'blocked',
        'call_transcription',
        'calling',
        'connected',
        'csat',
        'dispositions',
        'eavesdrop',
        'hangup',
        'hold',
        'merged',
        'missed',
        'monitor',
        'parked',
        'pcsat',
        'postcall',
        'preanswer',
        'queued',
        'recap_action_items',
        'recap_outcome',
        'recap_purposes',
        'recap_summary',
        'recording',
        'ringing',
        'takeover',
        'transcription',
        'voicemail',
        'voicemail_uploaded',
      ]
    ]
  ]
  "The call event subscription's list of call states."
  enabled: NotRequired[bool]
  'Whether or not the call event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully."
  group_calls_only: NotRequired[bool]
  'Call event subscription for group calls only.'
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
  'The target type.'


class UpdateCallEventSubscription(TypedDict):
  """TypedDict representation of the UpdateCallEventSubscription schema."""

  call_states: NotRequired[
    list[
      Literal[
        'admin',
        'admin_recording',
        'ai_playbook',
        'all',
        'barge',
        'blocked',
        'call_transcription',
        'calling',
        'connected',
        'csat',
        'dispositions',
        'eavesdrop',
        'hangup',
        'hold',
        'merged',
        'missed',
        'monitor',
        'parked',
        'pcsat',
        'postcall',
        'preanswer',
        'queued',
        'recap_action_items',
        'recap_outcome',
        'recap_purposes',
        'recap_summary',
        'recording',
        'ringing',
        'takeover',
        'transcription',
        'voicemail',
        'voicemail_uploaded',
      ]
    ]
  ]
  "The call event subscription's list of call states."
  enabled: NotRequired[bool]
  'Whether or not the call event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,\nplease provide a valid webhook ID here."
  group_calls_only: NotRequired[bool]
  'Call event subscription for group calls only.'
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
  'The target type.'
