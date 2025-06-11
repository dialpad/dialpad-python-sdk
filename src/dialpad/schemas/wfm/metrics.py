from typing import Optional, List, Dict, Union, Literal
from typing_extensions import TypedDict, NotRequired


class ActivityType(TypedDict):
  """Type information for an activity."""

  name: NotRequired[str]
  'The display name of the activity.'
  type: NotRequired[str]
  'The type of the activity, could be task or break.'


class TimeInterval(TypedDict):
  """Represents a time period with start and end timestamps."""

  end: NotRequired[str]
  'The end timestamp (exclusive) in ISO-8601 format.'
  start: NotRequired[str]
  'The start timestamp (inclusive) in ISO-8601 format.'


class ActivityMetrics(TypedDict):
  """Activity-level metrics for an agent."""

  activity: NotRequired[ActivityType]
  'The activity this metrics data represents.'
  adherence_score: NotRequired[float]
  "The agent's schedule adherence score (as a percentage)."
  average_conversation_time: NotRequired[float]
  'The average time spent on each conversation in minutes.'
  average_interaction_time: NotRequired[float]
  'The average time spent on each interaction in minutes.'
  conversations_closed: NotRequired[int]
  'The number of conversations closed during this period.'
  conversations_closed_per_hour: NotRequired[float]
  'The rate of conversation closure per hour.'
  conversations_commented_on: NotRequired[int]
  'The number of conversations commented on during this period.'
  conversations_on_hold: NotRequired[int]
  'The number of conversations placed on hold during this period.'
  conversations_opened: NotRequired[int]
  'The number of conversations opened during this period.'
  interval: NotRequired[TimeInterval]
  'The time period these metrics cover.'
  scheduled_hours: NotRequired[float]
  'The number of hours scheduled for this activity.'
  time_in_adherence: NotRequired[int]
  'Time (in seconds) the agent spent in adherence with their schedule.'
  time_in_exception: NotRequired[int]
  'Time (in seconds) the agent spent in adherence exceptions.'
  time_on_task: NotRequired[float]
  'The proportion of time spent on task (between 0 and 1).'
  time_out_of_adherence: NotRequired[int]
  'Time (in seconds) the agent spent out of adherence with their schedule.'
  wrong_task_snapshots: NotRequired[int]
  'The number of wrong task snapshots recorded.'


class ActivityMetricsResponse(TypedDict):
  """Response containing a collection of activity metrics."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request.\n\nUse the cursor provided in the previous response.'
  items: list[ActivityMetrics]
  'A list of activity metrics entries.'


class AgentInfo(TypedDict):
  """Information about an agent."""

  email: NotRequired[str]
  'The email address of the agent.'
  name: NotRequired[str]
  'The display name of the agent.'


class OccupancyInfo(TypedDict):
  """Information about occupancy metrics."""

  percentage: NotRequired[float]
  'The occupancy percentage (between 0 and 1).'
  seconds_lost: NotRequired[int]
  'The number of seconds lost.'


class StatusTimeInfo(TypedDict):
  """Information about time spent in a specific status."""

  percentage: NotRequired[float]
  'The percentage of time spent in this status (between 0 and 1).'
  seconds: NotRequired[int]
  'The number of seconds spent in this status.'


class DialpadTimeInStatus(TypedDict):
  """Breakdown of time spent in different Dialpad statuses."""

  available: NotRequired[StatusTimeInfo]
  'Time spent in available status.'
  busy: NotRequired[StatusTimeInfo]
  'Time spent in busy status.'
  occupied: NotRequired[StatusTimeInfo]
  'Time spent in occupied status.'
  unavailable: NotRequired[StatusTimeInfo]
  'Time spent in unavailable status.'
  wrapup: NotRequired[StatusTimeInfo]
  'Time spent in wrapup status.'


class AgentMetrics(TypedDict):
  """Agent-level performance metrics."""

  actual_occupancy: NotRequired[OccupancyInfo]
  "Information about the agent's actual occupancy."
  adherence_score: NotRequired[float]
  "The agent's schedule adherence score (as a percentage)."
  agent: NotRequired[AgentInfo]
  'Information about the agent these metrics belong to.'
  conversations_closed_per_hour: NotRequired[float]
  'The number of conversations closed per hour.'
  conversations_closed_per_service_hour: NotRequired[float]
  'The numbers of conversations closed per service hour.'
  dialpad_availability: NotRequired[OccupancyInfo]
  "Information about the agent's availability in Dialpad."
  dialpad_time_in_status: NotRequired[DialpadTimeInStatus]
  'Breakdown of time spent in different Dialpad statuses.'
  interval: NotRequired[TimeInterval]
  'The time period these metrics cover.'
  occupancy: NotRequired[float]
  "The agent's occupancy rate (between 0 and 1)."
  planned_occupancy: NotRequired[OccupancyInfo]
  "Information about the agent's planned occupancy."
  scheduled_hours: NotRequired[float]
  'The number of hours scheduled for the agent.'
  time_in_adherence: NotRequired[int]
  'Time (in seconds) the agent spent in adherence with their schedule.'
  time_in_exception: NotRequired[int]
  'Time (in seconds) the agent spent in adherence exceptions.'
  time_on_task: NotRequired[float]
  'The proportion of time spent on task (between 0 and 1).'
  time_out_of_adherence: NotRequired[int]
  'Time (in seconds) the agent spent out of adherence with their schedule.'
  total_conversations_closed: NotRequired[int]
  'The total number of conversations closed by the agent.'
  utilisation: NotRequired[float]
  "The agent's utilization rate (between 0 and 1)."


class AgentMetricsResponse(TypedDict):
  """Response containing a collection of agent metrics."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request.\n\nUse the cursor provided in the previous response.'
  items: list[AgentMetrics]
  'A list of agent metrics entries.'
