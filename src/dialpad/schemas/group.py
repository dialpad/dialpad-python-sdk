from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.room import RoomProto
from dialpad.schemas.user import UserProto


class AddCallCenterOperatorMessage(TypedDict):
  """TypedDict representation of the AddCallCenterOperatorMessage schema."""

  keep_paid_numbers: NotRequired[bool]
  'Whether or not to keep phone numbers when switching to a support license.\n\nNote: Phone numbers require additional number licenses under a support license.'
  license_type: NotRequired[Literal['agents', 'lite_support_agents']]
  'The type of license to assign to the new operator if a license is required.\n(`agents` or `lite_support_agents`). Defaults to `agents`'
  role: NotRequired[Literal['admin', 'operator', 'supervisor']]
  'The role the user should assume.'
  skill_level: NotRequired[int]
  'Skill level of the operator. Integer value in range 1 - 100. Default 100.'
  user_id: int
  'The ID of the user.'


class AddOperatorMessage(TypedDict):
  """TypedDict representation of the AddOperatorMessage schema."""

  operator_id: int
  'ID of the operator to add.'
  operator_type: Literal['room', 'user']
  'Type of the operator to add. (`user` or `room`)'
  role: NotRequired[Literal['admin', 'operator']]
  'The role of the new operator. (`operator` or `admin`)'


class AutoCallRecording(TypedDict):
  """TypedDict representation of the AutoCallRecording schema."""

  allow_pause_recording: NotRequired[bool]
  'Allow agents to stop/restart a recording during a call. Default is False.'
  call_recording_inbound: NotRequired[bool]
  'Whether or not inbound calls to this call center get automatically recorded. Default is False.'
  call_recording_outbound: NotRequired[bool]
  'Whether or not outbound calls from this call center get automatically recorded. Default is False.'


class AdvancedSettings(TypedDict):
  """TypedDict representation of the AdvancedSettings schema."""

  auto_call_recording: NotRequired[AutoCallRecording]
  'Choose which calls to and from this call center get automatically recorded. Recordings are only available to administrators of this call center, which can be found in the Dialpad app and the Calls List.'
  max_wrap_up_seconds: NotRequired[int]
  'Include a post-call wrap-up time before agents can receive their next call. Default is 0.'


class Alerts(TypedDict):
  """TypedDict representation of the Alerts schema."""

  cc_service_level: NotRequired[int]
  'Alert supervisors when the service level drops below how many percent. Default is 95%.'
  cc_service_level_seconds: NotRequired[int]
  'Inbound calls should be answered within how many seconds. Default is 60.'


class AvailabilityStatusProto(TypedDict):
  """Availability Status for a Call Center."""

  name: NotRequired[str]
  '[single-line only]\n\nA descriptive name for the status. If the Call Center is within any holiday, it displays it.'
  status: str
  'Status of this Call Center. It can be open, closed, holiday_open or holiday_closed'


class HoldQueueCallCenter(TypedDict):
  """TypedDict representation of the HoldQueueCallCenter schema."""

  allow_queue_callback: NotRequired[bool]
  'Whether or not to allow callers to request a callback. Default is False.'
  announce_position: NotRequired[bool]
  'Whether or not to let callers know their place in the queue. This option is not available when a maximum queue wait time of less than 2 minutes is selected. Default is True.'
  announcement_interval_seconds: NotRequired[int]
  'Hold announcement interval wait time. Default is 2 min.'
  max_hold_count: NotRequired[int]
  'If all operators are busy on other calls, send callers to a hold queue. This is to specify your queue size. Choose from 1-1000. Default is 50.'
  max_hold_seconds: NotRequired[int]
  'Maximum queue wait time in seconds. Choose from 30s to 18000s (3 hours). Default is 900s (15 min).'
  queue_callback_dtmf: NotRequired[str]
  'Allow callers to request a callback when the queue has more than queue_callback_threshold number of calls by pressing one of the followings: [0,1,2,3,4,5,6,7,8,9,*,#]. Default is 9.'
  queue_callback_threshold: NotRequired[int]
  'Allow callers to request a callback when the queue has more than this number of calls. Default is 5.'
  queue_escape_dtmf: NotRequired[str]
  'Allow callers to exit the hold queue to voicemail by pressing one of the followings:\n[0,1,2,3,4,5,6,7,8,9,*,#]. Default is *.'
  stay_in_queue_after_closing: NotRequired[bool]
  'Whether or not to allow existing calls to stay in queue after the call center has closed. Default is False.'
  unattended_queue: NotRequired[bool]
  'Whether or not to allow callers to be placed in your hold queue when no agents are available. Default is False.'


class DtmfOptions(TypedDict):
  """DTMF routing options."""

  action: NotRequired[
    Literal[
      'bridge_target',
      'company_directory',
      'department',
      'directory',
      'disabled',
      'extension',
      'menu',
      'message',
      'operator',
      'person',
      'scripted_ivr',
      'voicemail',
    ]
  ]
  'The routing action type.'
  action_target_id: NotRequired[int]
  'The ID of the target that should be dialed.'
  action_target_type: NotRequired[
    Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'contact',
      'contactgroup',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ]
  ]
  'The type of the target that should be dialed.'


class DtmfMapping(TypedDict):
  """TypedDict representation of the DtmfMapping schema."""

  input: NotRequired[str]
  'The DTMF key associated with this menu item. (0-9)'
  options: NotRequired[DtmfOptions]
  'The action that should be taken if the input key is pressed.'


class RoutingOptionsInner(TypedDict):
  """Group routing options for open or closed states."""

  action: Literal[
    'bridge_target',
    'company_directory',
    'department',
    'directory',
    'disabled',
    'extension',
    'menu',
    'message',
    'operator',
    'person',
    'scripted_ivr',
    'voicemail',
  ]
  'The action that should be taken if no operators are available.'
  action_target_id: NotRequired[int]
  'The ID of the Target that inbound calls should be routed to.'
  action_target_type: NotRequired[
    Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'contact',
      'contactgroup',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ]
  ]
  'The type of the Target that inbound calls should be routed to.'
  dtmf: NotRequired[list[DtmfMapping]]
  'DTMF menu options.'
  operator_routing: NotRequired[
    Literal['fixedorder', 'longestidle', 'mostskilled', 'random', 'roundrobin', 'simultaneous']
  ]
  'The routing strategy that should be used when dialing operators.'
  try_dial_operators: bool
  'Whether operators should be dialed on inbound calls.'


class RoutingOptions(TypedDict):
  """Group routing options."""

  closed: RoutingOptionsInner
  'Routing options to use during off hours.'
  open: RoutingOptionsInner
  'Routing options to use during open hours.'


class VoiceIntelligence(TypedDict):
  """TypedDict representation of the VoiceIntelligence schema."""

  allow_pause: NotRequired[bool]
  'Allow individual users to start and stop Vi during calls. Default is True.'
  auto_start: NotRequired[bool]
  'Auto start Vi for this call center. Default is True.'


class CallCenterProto(TypedDict):
  """Call center."""

  advanced_settings: NotRequired[AdvancedSettings]
  'Configure call center advanced settings.'
  alerts: NotRequired[Alerts]
  'Set when alerts will be triggered.'
  availability_status: NotRequired[Literal['closed', 'holiday_closed', 'holiday_open', 'open']]
  'Availability status of the group.'
  country: NotRequired[str]
  'The country in which the user group resides.'
  first_action: NotRequired[Literal['menu', 'operators']]
  'The initial action to take upon receiving a new call.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"]'
  group_description: NotRequired[str]
  'The description of the call center.'
  hold_queue: NotRequired[HoldQueueCallCenter]
  'Configure how the calls are sent to a hold queue when all operators are busy on other calls.'
  hours_on: NotRequired[bool]
  'The time frame when the call center wants to receive calls. Default value is false, which means the call center will always take calls (24/7).'
  id: NotRequired[int]
  'The ID of the group entity.'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the group.'
  no_operators_action: NotRequired[
    Literal[
      'bridge_target',
      'company_directory',
      'department',
      'directory',
      'disabled',
      'extension',
      'menu',
      'message',
      'operator',
      'person',
      'scripted_ivr',
      'voicemail',
    ]
  ]
  'The action to take if there are no operators available to accept an inbound call.'
  office_id: NotRequired[int]
  'The ID of the office in which this group resides.'
  phone_numbers: NotRequired[list[str]]
  'A list of phone numbers belonging to this group.'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The current enablement state of this group.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"]'
  timezone: NotRequired[str]
  'The timezone of the group.'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"]'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"]'


class CallCenterCollection(TypedDict):
  """Collection of call centers."""

  cursor: NotRequired[str]
  'A cursor string that can be used to fetch the subsequent page.'
  items: NotRequired[list[CallCenterProto]]
  'A list containing the first page of results.'


class CallCenterStatusProto(TypedDict):
  """Status information for a Call Center."""

  availability: AvailabilityStatusProto
  'Availability of the Call Center.'
  capacity: int
  'The number of available operators.'
  longest_call_wait_time: int
  'The longest queued call, in seconds.'
  on_duty_operators: int
  'The amount of operators On Duty'
  pending: int
  'The number of on-hold calls.'


class CreateCallCenterMessage(TypedDict):
  """TypedDict representation of the CreateCallCenterMessage schema."""

  advanced_settings: NotRequired[AdvancedSettings]
  'Configure advanced call center settings.'
  alerts: NotRequired[Alerts]
  'Set when alerts will be triggered.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"].'
  group_description: NotRequired[str]
  'The description of the call center. Max 256 characters.'
  hold_queue: NotRequired[HoldQueueCallCenter]
  'Configure how the calls are sent to a hold queue when all operators are busy on other calls.'
  hours_on: NotRequired[bool]
  'The time frame when the call center wants to receive calls. Default value is false, which means the call center will always take calls (24/7).'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: str
  '[single-line only]\n\nThe name of the call center. Max 100 characters.'
  office_id: int
  'The id of the office to which the call center belongs..'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"].'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"].'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"].'


class HoldQueueDepartment(TypedDict):
  """TypedDict representation of the HoldQueueDepartment schema."""

  allow_queuing: NotRequired[bool]
  'Whether or not send callers to a hold queue, if all operators are busy on other calls. Default is False.'
  max_hold_count: NotRequired[int]
  'If all operators are busy on other calls, send callers to a hold queue. This is to specify your queue size. Choose from 1-50. Default is 50.'
  max_hold_seconds: NotRequired[int]
  'Maximum queue wait time in seconds. Choose from 30s to 18000s (3 hours). Default is 900s (15 min).'


class CreateDepartmentMessage(TypedDict):
  """TypedDict representation of the CreateDepartmentMessage schema."""

  auto_call_recording: NotRequired[bool]
  'Whether or not automatically record all calls of this department. Default is False.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"].'
  group_description: NotRequired[str]
  'The description of the department. Max 256 characters.'
  hold_queue: NotRequired[HoldQueueDepartment]
  'Configure how the calls are sent to a hold queue when all operators are busy on other calls.'
  hours_on: NotRequired[bool]
  'The time frame when the department wants to receive calls. Default value is false, which means the call center will always take calls (24/7).'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: str
  '[single-line only]\n\nThe name of the department. Max 100 characters.'
  office_id: int
  'The id of the office to which the department belongs..'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"].'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"].'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"].'


class DepartmentProto(TypedDict):
  """Department."""

  auto_call_recording: NotRequired[bool]
  'Whether or not automatically record all calls of this department. Default is False.'
  availability_status: NotRequired[Literal['closed', 'holiday_closed', 'holiday_open', 'open']]
  'Availability status of the group.'
  country: NotRequired[str]
  'The country in which the user group resides.'
  first_action: NotRequired[Literal['menu', 'operators']]
  'The initial action to take upon receiving a new call.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"]'
  group_description: NotRequired[str]
  'The description of the call center.'
  hold_queue: NotRequired[HoldQueueDepartment]
  'Configure how the calls are sent to a hold queue when all operators are busy on other calls.'
  hours_on: NotRequired[bool]
  'The time frame when the call center wants to receive calls. Default value is false, which means the call center will always take calls (24/7).'
  id: NotRequired[int]
  'The ID of the group entity.'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the group.'
  no_operators_action: NotRequired[
    Literal[
      'bridge_target',
      'company_directory',
      'department',
      'directory',
      'disabled',
      'extension',
      'menu',
      'message',
      'operator',
      'person',
      'scripted_ivr',
      'voicemail',
    ]
  ]
  'The action to take if there are no operators available to accept an inbound call.'
  office_id: NotRequired[int]
  'The ID of the office in which this group resides.'
  phone_numbers: NotRequired[list[str]]
  'A list of phone numbers belonging to this group.'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The current enablement state of this group.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"]'
  timezone: NotRequired[str]
  'The timezone of the group.'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"]'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"]'


class DepartmentCollection(TypedDict):
  """Collection of departments."""

  cursor: NotRequired[str]
  'A cursor string that can be used to fetch the subsequent page.'
  items: NotRequired[list[DepartmentProto]]
  'A list containing the first page of results.'


class OperatorCollection(TypedDict):
  """Operators can be users or rooms."""

  rooms: NotRequired[list[RoomProto]]
  'A list of rooms that can currently act as operators for this group.'
  users: NotRequired[list[UserProto]]
  'A list of users who are currently operators of this group.'


class OperatorDutyStatusProto(TypedDict):
  """TypedDict representation of the OperatorDutyStatusProto schema."""

  duty_status_reason: NotRequired[str]
  '[single-line only]\n\nA description of this status.'
  duty_status_started: NotRequired[int]
  'The time stamp, in UTC, when the current on duty status changed.'
  on_duty: NotRequired[bool]
  'Whether the operator is currently on duty or off duty.'
  on_duty_started: NotRequired[int]
  'The time stamp, in UTC, when this operator became available for contact center calls.'
  on_duty_status: NotRequired[
    Literal['available', 'busy', 'occupied', 'occupied-end', 'unavailable', 'wrapup', 'wrapup-end']
  ]
  "A description of operator's on duty status."
  user_id: NotRequired[int]
  'The ID of the operator.'


class OperatorSkillLevelProto(TypedDict):
  """TypedDict representation of the OperatorSkillLevelProto schema."""

  call_center_id: NotRequired[int]
  "The call center's id."
  skill_level: NotRequired[int]
  'New skill level of the operator.'
  user_id: NotRequired[int]
  'The ID of the operator.'


class RemoveCallCenterOperatorMessage(TypedDict):
  """TypedDict representation of the RemoveCallCenterOperatorMessage schema."""

  user_id: int
  'ID of the operator to remove.'


class RemoveOperatorMessage(TypedDict):
  """TypedDict representation of the RemoveOperatorMessage schema."""

  operator_id: int
  'ID of the operator to remove.'
  operator_type: Literal['room', 'user']
  'Type of the operator to remove (`user` or `room`).'


class UpdateCallCenterMessage(TypedDict):
  """TypedDict representation of the UpdateCallCenterMessage schema."""

  advanced_settings: NotRequired[AdvancedSettings]
  'Configure advanced call center settings.'
  alerts: NotRequired[Alerts]
  'Set when alerts will be triggered.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"].'
  group_description: NotRequired[str]
  'The description of the call center. Max 256 characters.'
  hold_queue: NotRequired[HoldQueueCallCenter]
  'Configure how the calls are sent to a hold queue when all operators are busy on other calls.'
  hours_on: NotRequired[bool]
  'The time frame when the call center wants to receive calls. Default value is false, which means the call center will always take calls (24/7).'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the call center. Max 100 characters.'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"].'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"].'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"].'


class UpdateDepartmentMessage(TypedDict):
  """TypedDict representation of the UpdateDepartmentMessage schema."""

  auto_call_recording: NotRequired[bool]
  'Whether or not automatically record all calls of this department. Default is False.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"].'
  group_description: NotRequired[str]
  'The description of the department. Max 256 characters.'
  hold_queue: NotRequired[HoldQueueDepartment]
  'Configure how the calls are sent to a hold queue when all operators are busy on other calls.'
  hours_on: NotRequired[bool]
  'The time frame when the department wants to receive calls. Default value is false, which means the call center will always take calls (24/7).'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the department. Max 100 characters.'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds. Default is 30 seconds.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"].'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"].'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"].'


class UpdateOperatorDutyStatusMessage(TypedDict):
  """TypedDict representation of the UpdateOperatorDutyStatusMessage schema."""

  duty_status_reason: NotRequired[str]
  '[single-line only]\n\nA description of this status.'
  on_duty: bool
  'True if this status message indicates an "on-duty" status.'


class UpdateOperatorSkillLevelMessage(TypedDict):
  """TypedDict representation of the UpdateOperatorSkillLevelMessage schema."""

  skill_level: int
  'New skill level to set the operator in the call center. It must be an integer value between 0 and 100.'


class UserOrRoomProto(TypedDict):
  """Operator."""

  company_id: NotRequired[int]
  'The company to which this entity belongs.'
  country: NotRequired[str]
  'The country in which the entity resides.'
  id: NotRequired[int]
  'The ID of this entity.'
  image_url: NotRequired[str]
  "The url of this entity's profile image."
  is_on_duty: NotRequired[bool]
  'Whether the entity is currently acting as an operator.'
  name: NotRequired[str]
  "[single-line only]\n\nThe entity's name."
  office_id: NotRequired[int]
  'The office in which this entity resides.'
  phone_numbers: NotRequired[list[str]]
  'The phone numbers associated with this entity.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The current enablement state of this entity.'
