from typing import Literal, Union

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.breadcrumbs import ApiCallRouterBreadcrumb
from dialpad.schemas.userdevice import UserDeviceProto


class ActiveCallProto(TypedDict):
  """Active call."""

  call_state: NotRequired[str]
  'The current state of the call.'
  id: NotRequired[int]
  'A unique number ID automatically assigned to each call.'
  is_recording: NotRequired[bool]
  'A boolean indicating whether the call is currently being recorded.'


class AddCallLabelsMessage(TypedDict):
  """Create labels for a call"""

  labels: NotRequired[list[str]]
  'The list of labels to attach to the call'


class NumberTransferDestination(TypedDict):
  """TypedDict representation of the NumberTransferDestination schema."""

  number: str
  'The phone number which the call should be transferred to.'


class TargetTransferDestination(TypedDict):
  """TypedDict representation of the TargetTransferDestination schema."""

  target_id: int
  'The ID of the target that will be used to transfer the call.'
  target_type: Literal['callcenter', 'department', 'office', 'user']
  'Type of target that will be used to transfer the call.'


class AddParticipantMessage(TypedDict):
  """Add participant into a Call."""

  participant: Union[NumberTransferDestination, TargetTransferDestination]
  'New member of the call to add. Can be a number or a Target. In case of a target, it must have a primary number assigned.'


class CallContactProto(TypedDict):
  """Call contact."""

  email: NotRequired[str]
  'The primary email address of the contact.'
  id: NotRequired[str]
  'A unique number ID for the contact.'
  name: NotRequired[str]
  '[single-line only]\n\nName of contact.'
  phone: NotRequired[str]
  'The primary phone number of the contact.'
  type: NotRequired[str]
  'Type of the contact.'


class CallRecordingDetailsProto(TypedDict):
  """Call recording details."""

  duration: NotRequired[int]
  'The duration of the recording in milliseconds'
  id: NotRequired[str]
  'The recording ID'
  recording_type: NotRequired[Literal['admincallrecording', 'callrecording', 'voicemail']]
  'The recording type'
  start_time: NotRequired[int]
  'The recording start timestamp'
  url: NotRequired[str]
  'The access URL of the recording'


class CallProto(TypedDict):
  """Call."""

  admin_call_recording_share_links: NotRequired[list[str]]
  'A list of admin call recording share links.'
  call_id: NotRequired[int]
  'A unique number ID automatically assigned to each call.'
  call_recording_share_links: NotRequired[list[str]]
  'A list of call recording share links.'
  contact: NotRequired[CallContactProto]
  'This is the contact involved in the call.'
  csat_recording_urls: NotRequired[list[str]]
  'A list of CSAT urls related to the call.'
  csat_score: NotRequired[str]
  'CSAT score related to the call.'
  csat_transcriptions: NotRequired[list[str]]
  'A list of CSAT texts related to the call.'
  custom_data: NotRequired[str]
  'Any custom data.'
  date_connected: NotRequired[int]
  'Timestamp when Dialpad connected the call.'
  date_ended: NotRequired[int]
  'Timestamp when the call was hung up.'
  date_rang: NotRequired[int]
  'Timestamp when Dialpad first detects an inbound call toa mainline, department, or person.'
  date_started: NotRequired[int]
  'Timestamp when the call began in the Dialpad system before being connected.'
  direction: NotRequired[str]
  'Call direction. Indicates whether a call was outbound or inbound.'
  duration: NotRequired[float]
  'Duration of the call in milliseconds.'
  entry_point_call_id: NotRequired[int]
  'Call ID of the associated entry point call.'
  entry_point_target: NotRequired[CallContactProto]
  'Where a call initially dialed for inbound calls to Dialpad.'
  event_timestamp: NotRequired[int]
  'Timestamp of when this call event happened.'
  external_number: NotRequired[str]
  'The phone number external to your organization.'
  group_id: NotRequired[str]
  'Unique ID of the department, mainline, or call queue associated with the call.'
  internal_number: NotRequired[str]
  'The phone number internal to your organization.'
  is_transferred: NotRequired[bool]
  'Boolean indicating whether or not the call was transferred.'
  labels: NotRequired[list[str]]
  "The label's associated to this call."
  master_call_id: NotRequired[int]
  'The master id of the specified call.'
  mos_score: NotRequired[float]
  'Mean Opinion Score'
  operator_call_id: NotRequired[int]
  'The id of operator.'
  proxy_target: NotRequired[CallContactProto]
  'Caller ID used by the Dialpad user for outbound calls.'
  recording_details: NotRequired[list[CallRecordingDetailsProto]]
  'List of associated recording details.'
  routing_breadcrumbs: NotRequired[list[ApiCallRouterBreadcrumb]]
  'The routing breadcrumbs'
  screen_recording_urls: NotRequired[list[str]]
  'A list of screen recording urls.'
  state: NotRequired[str]
  'Current call state.'
  target: NotRequired[CallContactProto]
  'This is the target that the Dialpad user dials or receives a call from.'
  total_duration: NotRequired[float]
  'Duration of the call in milliseconds, including ring time.'
  transcription_text: NotRequired[str]
  'Text of call transcription.'
  voicemail_share_link: NotRequired[str]
  'Share link to the voicemail recording.'
  was_recorded: NotRequired[bool]
  'Boolean indicating whether or not the call was recorded.'


class CallCollection(TypedDict):
  """Collection of calls."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[CallProto]]
  'A list of calls.'


class CallTransferDestination(TypedDict):
  """TypedDict representation of the CallTransferDestination schema."""

  call_id: int
  'The id of the ongoing call which the call should be transferred to.'


class CallbackMessage(TypedDict):
  """TypedDict representation of the CallbackMessage schema."""

  call_center_id: NotRequired[int]
  'The ID of a call center that will be used to fulfill the callback.'
  phone_number: NotRequired[str]
  'The e164-formatted number to call back'


class CallbackProto(TypedDict):
  """Note: Position indicates the new callback request's position in the queue, with 1 being at the front."""

  position: NotRequired[int]
  "Indicates the new callback request's position in the queue, with 1 being at the front."


class InitiateCallMessage(TypedDict):
  """TypedDict representation of the InitiateCallMessage schema."""

  custom_data: NotRequired[str]
  'Extra data to associate with the call. This will be passed through to any subscribed call events.'
  group_id: NotRequired[int]
  'The ID of a group that will be used to initiate the call.'
  group_type: NotRequired[Literal['callcenter', 'department', 'office']]
  'The type of a group that will be used to initiate the call.'
  outbound_caller_id: NotRequired[str]
  'The e164-formatted number shown to the call recipient (or "blocked").\n\nIf set to "blocked", the recipient will receive a call from "unknown caller". The number can be the caller\'s number, or the caller\'s group number if the group is provided,\nor the caller\'s company reserved number.'
  phone_number: NotRequired[str]
  'The e164-formatted number to call.'


class InitiatedCallProto(TypedDict):
  """Initiated call."""

  device: NotRequired[UserDeviceProto]
  'The device used to initiate the call.'


class InitiatedIVRCallProto(TypedDict):
  """Initiated IVR call."""

  call_id: int
  'The ID of the initiated call.'


class OutboundIVRMessage(TypedDict):
  """TypedDict representation of the OutboundIVRMessage schema."""

  custom_data: NotRequired[str]
  'Extra data to associate with the call. This will be passed through to any subscribed call events.'
  outbound_caller_id: NotRequired[str]
  'The e164-formatted number shown to the call recipient (or "blocked").'
  phone_number: str
  'The e164-formatted number to call.'
  target_id: int
  'The ID of a group that will be used to initiate the call.'
  target_type: Literal['callcenter', 'department', 'office']
  'The type of a group that will be used to initiate the call.'


class RingCallMessage(TypedDict):
  """TypedDict representation of the RingCallMessage schema."""

  custom_data: NotRequired[str]
  'Extra data to associate with the call. This will be passed through to any subscribed call events.'
  device_id: NotRequired[str]
  "The device's id."
  group_id: NotRequired[int]
  'The ID of a group that will be used to initiate the call.'
  group_type: NotRequired[Literal['callcenter', 'department', 'office']]
  'The type of a group that will be used to initiate the call.'
  is_consult: NotRequired[bool]
  'Enables the creation of a second call. If there is an ongoing call, it puts it on hold.'
  outbound_caller_id: NotRequired[str]
  'The e164-formatted number shown to the call recipient (or "blocked").\n\nIf set to "blocked", the recipient will receive a call from "unknown caller". The number can be the caller\'s number, or the caller\'s group number if the group is provided, or the caller\'s company reserved number.'
  phone_number: str
  'The e164-formatted number to call.'
  user_id: int
  'The id of the user who should make the outbound call.'


class RingCallProto(TypedDict):
  """Ringing call."""

  call_id: NotRequired[int]
  'The ID of the created call.'


class ToggleViMessage(TypedDict):
  """TypedDict representation of the ToggleViMessage schema."""

  enable_vi: NotRequired[bool]
  'Whether or not call vi should be enabled.'
  vi_locale: NotRequired[
    Literal[
      'en-au',
      'en-ca',
      'en-de',
      'en-fr',
      'en-gb',
      'en-it',
      'en-jp',
      'en-mx',
      'en-nl',
      'en-nz',
      'en-pt',
      'en-us',
      'es-au',
      'es-ca',
      'es-de',
      'es-es',
      'es-fr',
      'es-gb',
      'es-it',
      'es-jp',
      'es-mx',
      'es-nl',
      'es-nz',
      'es-pt',
      'es-us',
      'fr-au',
      'fr-ca',
      'fr-de',
      'fr-es',
      'fr-fr',
      'fr-gb',
      'fr-it',
      'fr-jp',
      'fr-mx',
      'fr-nl',
      'fr-nz',
      'fr-pt',
      'fr-us',
    ]
  ]
  'The locale to use for vi.'


class ToggleViProto(TypedDict):
  """VI state."""

  call_state: NotRequired[str]
  'Current call state.'
  enable_vi: NotRequired[bool]
  'Whether vi is enabled.'
  id: NotRequired[int]
  'The id of the toggled call.'
  vi_locale: NotRequired[str]
  'The locale used for vi.'


class TransferCallMessage(TypedDict):
  """TypedDict representation of the TransferCallMessage schema."""

  custom_data: NotRequired[str]
  'Extra data to associate with the call. This will be passed through to any subscribed call events.'
  to: NotRequired[
    Union[CallTransferDestination, NumberTransferDestination, TargetTransferDestination]
  ]
  'Destination of the call that will be transfer. It can be a single option between a number, \nan existing call or a target'
  transfer_state: NotRequired[Literal['hold', 'parked', 'preanswer', 'voicemail']]
  "The state which the call should take when it's transferred to."


class TransferredCallProto(TypedDict):
  """Transferred call."""

  call_id: NotRequired[int]
  "The call's id."
  transferred_to_number: NotRequired[str]
  'The phone number which the call has been transferred to.'
  transferred_to_state: NotRequired[Literal['hold', 'parked', 'preanswer', 'voicemail']]
  'The state which the call has been transferred to.'


class UnparkCallMessage(TypedDict):
  """TypedDict representation of the UnparkCallMessage schema."""

  user_id: int
  'The id of the user who should unpark the call.'


class UpdateActiveCallMessage(TypedDict):
  """TypedDict representation of the UpdateActiveCallMessage schema."""

  is_recording: NotRequired[bool]
  'Whether or not recording should be enabled.'
  play_message: NotRequired[bool]
  'Whether or not to play a message to indicate the call is being recorded (or recording has stopped).'
  recording_type: NotRequired[Literal['all', 'group', 'user']]
  'Whether or not to toggle recording for the operator call (personal recording),\nthe group call (department recording), or both.\n\nOnly applicable for group calls (call centers, departments, etc.)'


class ValidateCallbackProto(TypedDict):
  """Callback (validation)."""

  success: NotRequired[bool]
  'Whether the callback request would have been queued successfully.'
