from typing import Literal

from typing_extensions import NotRequired, TypedDict


class ProcessStatsMessage(TypedDict):
  """TypedDict representation of the ProcessStatsMessage schema."""

  coaching_group: NotRequired[bool]
  'Whether or not the the statistics should be for trainees of the coach group with the given target_id.'
  coaching_team: NotRequired[bool]
  'Whether or not the the statistics should be for trainees of the coach team with the given target_id.'
  days_ago_end: NotRequired[int]
  'End of the date range to get statistics for.\n\nThis is the number of days to look back relative to the current day. Used in conjunction with days_ago_start to specify a range.'
  days_ago_start: NotRequired[int]
  'Start of the date range to get statistics for.\n\nThis is the number of days to look back relative to the current day. Used in conjunction with days_ago_end to specify a range.'
  export_type: Literal['records', 'stats']
  'Whether to return aggregated statistics (stats), or individual rows for each record (records).\n\nNOTE: For stat_type "csat" or "dispositions", only "records" is supported.'
  group_by: NotRequired[Literal['date', 'group', 'user']]
  'This param is only applicable when the stat_type is specified as call. For call stats, group calls by user per day (default), get total metrics by day, or break down by department and call center (office only).'
  is_today: NotRequired[bool]
  'Whether or not the statistics are for the current day.\n\nNOTE: days_ago_start and days_ago_end are ignored if this is passed in.'
  office_id: NotRequired[int]
  'ID of the office to get statistics for.\n\nIf a target_id and target_type are passed in this value is ignored and instead the target is used.'
  stat_type: Literal[
    'calls', 'csat', 'dispositions', 'onduty', 'recordings', 'screenshare', 'texts', 'voicemails'
  ]
  'The type of statistics to be returned.\n\nNOTE: if the value is "csat" or "dispositions", target_id and target_type must be specified.'
  target_id: NotRequired[int]
  "The target's id."
  target_type: NotRequired[
    Literal[
      'callcenter',
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


class ProcessingProto(TypedDict):
  """Processing status."""

  already_started: NotRequired[bool]
  'A boolean indicating whether this request has already begun processing.'
  request_id: NotRequired[str]
  'The processing request ID.'


class StatsProto(TypedDict):
  """Stats export."""

  download_url: NotRequired[str]
  'The URL of the resulting stats file.'
  file_type: NotRequired[str]
  'The file format of the resulting stats file.'
  status: NotRequired[Literal['complete', 'failed', 'processing']]
  'The current status of the processing request.'
