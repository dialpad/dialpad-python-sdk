from typing import Annotated, Literal

from typing_extensions import NotRequired, TypedDict


class CreateCustomIvrMessage(TypedDict):
  """TypedDict representation of the CreateCustomIvrMessage schema."""

  description: NotRequired[str]
  '[single-line only]\n\nThe description of the new IVR. Max 256 characters.'
  file: Annotated[str, 'base64']
  'An MP3 audio file. The file needs to be Base64-encoded.'
  ivr_type: Literal[
    'ASK_FIRST_OPERATOR_NOT_AVAILABLE',
    'AUTO_RECORDING',
    'CALLAI_AUTO_RECORDING',
    'CG_AUTO_RECORDING',
    'CLOSED',
    'CLOSED_DEPARTMENT_INTRO',
    'CLOSED_MENU',
    'CLOSED_MENU_OPTION',
    'CSAT_INTRO',
    'CSAT_OUTRO',
    'CSAT_PREAMBLE',
    'CSAT_QUESTION',
    'DEPARTMENT_INTRO',
    'GREETING',
    'HOLD_AGENT_READY',
    'HOLD_APPREC',
    'HOLD_CALLBACK_ACCEPT',
    'HOLD_CALLBACK_ACCEPTED',
    'HOLD_CALLBACK_CONFIRM',
    'HOLD_CALLBACK_CONFIRM_NUMBER',
    'HOLD_CALLBACK_DIFFERENT_NUMBER',
    'HOLD_CALLBACK_DIRECT',
    'HOLD_CALLBACK_FULFILLED',
    'HOLD_CALLBACK_INVALID_NUMBER',
    'HOLD_CALLBACK_KEYPAD',
    'HOLD_CALLBACK_REJECT',
    'HOLD_CALLBACK_REJECTED',
    'HOLD_CALLBACK_REQUEST',
    'HOLD_CALLBACK_REQUESTED',
    'HOLD_CALLBACK_SAME_NUMBER',
    'HOLD_CALLBACK_TRY_AGAIN',
    'HOLD_CALLBACK_UNDIALABLE',
    'HOLD_ESCAPE_VM_EIGHT',
    'HOLD_ESCAPE_VM_FIVE',
    'HOLD_ESCAPE_VM_FOUR',
    'HOLD_ESCAPE_VM_NINE',
    'HOLD_ESCAPE_VM_ONE',
    'HOLD_ESCAPE_VM_POUND',
    'HOLD_ESCAPE_VM_SEVEN',
    'HOLD_ESCAPE_VM_SIX',
    'HOLD_ESCAPE_VM_STAR',
    'HOLD_ESCAPE_VM_TEN',
    'HOLD_ESCAPE_VM_THREE',
    'HOLD_ESCAPE_VM_TWO',
    'HOLD_ESCAPE_VM_ZERO',
    'HOLD_INTERRUPT',
    'HOLD_INTRO',
    'HOLD_MUSIC',
    'HOLD_POSITION_EIGHT',
    'HOLD_POSITION_FIVE',
    'HOLD_POSITION_FOUR',
    'HOLD_POSITION_MORE',
    'HOLD_POSITION_NINE',
    'HOLD_POSITION_ONE',
    'HOLD_POSITION_SEVEN',
    'HOLD_POSITION_SIX',
    'HOLD_POSITION_TEN',
    'HOLD_POSITION_THREE',
    'HOLD_POSITION_TWO',
    'HOLD_POSITION_ZERO',
    'HOLD_WAIT',
    'MENU',
    'MENU_OPTION',
    'NEXT_TARGET',
    'VM_DROP_MESSAGE',
    'VM_UNAVAILABLE',
    'VM_UNAVAILABLE_CLOSED',
  ]
  'Type of IVR.'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the new IVR. Max 100 characters.'
  target_id: int
  'The ID of the target to which you want to assign this IVR.'
  target_type: Literal['callcenter', 'coachingteam', 'department', 'office', 'user']
  'The type of the target to which you want to assign this IVR.'


class CustomIvrDetailsProto(TypedDict):
  """Custom IVR details."""

  date_added: NotRequired[int]
  'Date when this IVR was added.'
  description: NotRequired[str]
  '[single-line only]\n\nThe description of the IVR.'
  id: NotRequired[int]
  'Id of this IVR.'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of this IVR.'
  selected: NotRequired[bool]
  'True if this IVR is selected for this type of IVR.'
  text: NotRequired[str]
  'The text for this IVR if there is no mp3.'


class CustomIvrProto(TypedDict):
  """Custom IVR."""

  ivr_type: NotRequired[
    Literal[
      'ASK_FIRST_OPERATOR_NOT_AVAILABLE',
      'AUTO_RECORDING',
      'CALLAI_AUTO_RECORDING',
      'CG_AUTO_RECORDING',
      'CLOSED',
      'CLOSED_DEPARTMENT_INTRO',
      'CLOSED_MENU',
      'CLOSED_MENU_OPTION',
      'CSAT_INTRO',
      'CSAT_OUTRO',
      'CSAT_PREAMBLE',
      'CSAT_QUESTION',
      'DEPARTMENT_INTRO',
      'GREETING',
      'HOLD_AGENT_READY',
      'HOLD_APPREC',
      'HOLD_CALLBACK_ACCEPT',
      'HOLD_CALLBACK_ACCEPTED',
      'HOLD_CALLBACK_CONFIRM',
      'HOLD_CALLBACK_CONFIRM_NUMBER',
      'HOLD_CALLBACK_DIFFERENT_NUMBER',
      'HOLD_CALLBACK_DIRECT',
      'HOLD_CALLBACK_FULFILLED',
      'HOLD_CALLBACK_INVALID_NUMBER',
      'HOLD_CALLBACK_KEYPAD',
      'HOLD_CALLBACK_REJECT',
      'HOLD_CALLBACK_REJECTED',
      'HOLD_CALLBACK_REQUEST',
      'HOLD_CALLBACK_REQUESTED',
      'HOLD_CALLBACK_SAME_NUMBER',
      'HOLD_CALLBACK_TRY_AGAIN',
      'HOLD_CALLBACK_UNDIALABLE',
      'HOLD_ESCAPE_VM_EIGHT',
      'HOLD_ESCAPE_VM_FIVE',
      'HOLD_ESCAPE_VM_FOUR',
      'HOLD_ESCAPE_VM_NINE',
      'HOLD_ESCAPE_VM_ONE',
      'HOLD_ESCAPE_VM_POUND',
      'HOLD_ESCAPE_VM_SEVEN',
      'HOLD_ESCAPE_VM_SIX',
      'HOLD_ESCAPE_VM_STAR',
      'HOLD_ESCAPE_VM_TEN',
      'HOLD_ESCAPE_VM_THREE',
      'HOLD_ESCAPE_VM_TWO',
      'HOLD_ESCAPE_VM_ZERO',
      'HOLD_INTERRUPT',
      'HOLD_INTRO',
      'HOLD_MUSIC',
      'HOLD_POSITION_EIGHT',
      'HOLD_POSITION_FIVE',
      'HOLD_POSITION_FOUR',
      'HOLD_POSITION_MORE',
      'HOLD_POSITION_NINE',
      'HOLD_POSITION_ONE',
      'HOLD_POSITION_SEVEN',
      'HOLD_POSITION_SIX',
      'HOLD_POSITION_TEN',
      'HOLD_POSITION_THREE',
      'HOLD_POSITION_TWO',
      'HOLD_POSITION_ZERO',
      'HOLD_WAIT',
      'MENU',
      'MENU_OPTION',
      'NEXT_TARGET',
      'VM_DROP_MESSAGE',
      'VM_UNAVAILABLE',
      'VM_UNAVAILABLE_CLOSED',
    ]
  ]
  'Type of IVR.'
  ivrs: NotRequired[list[CustomIvrDetailsProto]]
  'A list of IVR detail objects.'


class CustomIvrCollection(TypedDict):
  """Collection of Custom IVRs."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[CustomIvrProto]]
  'A list of IVRs.'


class UpdateCustomIvrDetailsMessage(TypedDict):
  """TypedDict representation of the UpdateCustomIvrDetailsMessage schema."""

  description: NotRequired[str]
  '[single-line only]\n\nThe description of the IVR.'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of this IVR.'


class UpdateCustomIvrMessage(TypedDict):
  """TypedDict representation of the UpdateCustomIvrMessage schema."""

  ivr_id: int
  'The id of the ivr that you want to use for the ivr type.'
  select_option: NotRequired[Literal['inbound', 'outbound']]
  'For call center auto call recording only. Set ivr for inbound or outbound. Default is both.'
