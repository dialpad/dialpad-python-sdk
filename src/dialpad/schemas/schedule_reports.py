from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.webhook import WebhookProto
from dialpad.schemas.websocket import WebsocketProto


class ProcessScheduleReportsMessage(TypedDict):
  """TypedDict representation of the ProcessScheduleReportsMessage schema."""

  at: int
  'Hour of the day when the report will execute considering the frequency and timezones between 0 and 23  e.g. 10 will be 10:00 am.'
  coaching_group: NotRequired[bool]
  'Whether the the statistics should be for trainees of the coach group with the given target_id.'
  enabled: NotRequired[bool]
  'Whether or not this schedule reports event subscription is enabled.'
  endpoint_id: int
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully."
  frequency: Literal['daily', 'monthly', 'weekly']
  'How often the report will execute.'
  name: str
  '[single-line only]\n\nThe name of the schedule reports.'
  on_day: int
  'The day of the week or month when the report will execute considering the frequency. daily=0, weekly=0-6, monthly=0-30.'
  report_type: Literal[
    'call_logs', 'daily_statistics', 'recordings', 'user_statistics', 'voicemails'
  ]
  'The type of report that will be generated.'
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
  timezone: NotRequired[str]
  'Timezone using a tz database name.'


class ScheduleReportsStatusEventSubscriptionProto(TypedDict):
  """Schedule report status event subscription."""

  at: NotRequired[int]
  'Hour of the day when the report will execute considering the frequency and timezones between 0 and 23  e.g. 10 will be 10:00 am.'
  coaching_group: NotRequired[bool]
  'Whether the the statistics should be for trainees of the coach group with the given target_id.'
  enabled: NotRequired[bool]
  'Whether or not the this agent status event subscription is enabled.'
  frequency: NotRequired[str]
  'The frequency of the schedule reports.'
  id: NotRequired[int]
  "The schedule reports subscription's ID, which is generated after creating an schedule reports subscription successfully."
  name: NotRequired[str]
  '[single-line only]\n\nThe day to be send the schedule reports.'
  on_day: NotRequired[int]
  'The day of the week or month when the report will execute considering the frequency. daily=0, weekly=0-6, monthly=0-30.'
  report_type: Literal[
    'call_logs', 'daily_statistics', 'recordings', 'user_statistics', 'voicemails'
  ]
  'The report options filters.'
  target_id: NotRequired[int]
  "The target's id."
  target_type: NotRequired[
    Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'company',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ]
  ]
  "Target's type."
  timezone: NotRequired[str]
  'Timezone using a tz database name.'
  webhook: NotRequired[WebhookProto]
  "The webhook's ID, which is generated after creating a webhook successfully."
  websocket: NotRequired[WebsocketProto]
  "The websocket's ID, which is generated after creating a webhook successfully."


class ScheduleReportsCollection(TypedDict):
  """Schedule reports collection."""

  cursor: NotRequired[str]
  'A token used to return the next page of results.'
  items: NotRequired[list[ScheduleReportsStatusEventSubscriptionProto]]
  'A list of schedule reports.'
