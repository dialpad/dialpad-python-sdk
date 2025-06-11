from typing import Literal, Union

from typing_extensions import NotRequired, TypedDict


class AreaCodeSwap(TypedDict):
  """Swap number with a number in the specified area code."""

  area_code: NotRequired[str]
  'An area code in which to find an available phone number for assignment.'
  type: str
  'Type of swap.'


class AssignNumberMessage(TypedDict):
  """TypedDict representation of the AssignNumberMessage schema."""

  area_code: NotRequired[str]
  'An area code in which to find an available phone number for assignment.'
  number: NotRequired[str]
  'A phone number to assign. (e164-formatted)'
  primary: NotRequired[bool]
  'A boolean indicating whether this should become the primary phone number.'


class AssignNumberTargetGenericMessage(TypedDict):
  """TypedDict representation of the AssignNumberTargetGenericMessage schema."""

  area_code: NotRequired[str]
  'An area code in which to find an available phone number for assignment.'
  number: NotRequired[str]
  'A phone number to assign. (e164-formatted)'
  primary: NotRequired[bool]
  "A boolean indicating whether this should become the target's primary phone number."
  target_id: int
  'The ID of the target to reassign this number to.'
  target_type: Literal[
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
  'The type of the target.'


class AssignNumberTargetMessage(TypedDict):
  """TypedDict representation of the AssignNumberTargetMessage schema."""

  primary: NotRequired[bool]
  "A boolean indicating whether this should become the target's primary phone number."
  target_id: int
  'The ID of the target to reassign this number to.'
  target_type: Literal[
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
  'The type of the target.'


class AutoSwap(TypedDict):
  """Swap number with an auto-assigned number."""

  type: str
  'Type of swap.'


class NumberProto(TypedDict):
  """Number details."""

  area_code: NotRequired[str]
  'The area code of the number.'
  company_id: NotRequired[int]
  'The ID of the associated company.'
  deleted: NotRequired[bool]
  'A boolean indicating whether this number has been ported out of Dialpad.'
  number: NotRequired[str]
  'The e164-formatted number.'
  office_id: NotRequired[int]
  'The ID of the associate office.'
  status: NotRequired[
    Literal[
      'available',
      'call_center',
      'call_router',
      'department',
      'dynamic_caller',
      'office',
      'pending',
      'porting',
      'room',
      'user',
    ]
  ]
  'The current assignment status of this number.'
  target_id: NotRequired[int]
  'The ID of the target to which this number is assigned.'
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
  'The type of the target to which this number is assigned.'
  type: NotRequired[Literal['free', 'local', 'mobile', 'softbank', 'tollfree']]
  'The number type.'


class NumberCollection(TypedDict):
  """Collection of numbers."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[NumberProto]]
  'A list of phone numbers.'


class ProvidedNumberSwap(TypedDict):
  """Swap number with provided number."""

  number: NotRequired[str]
  'A phone number to swap. (e164-formatted)'
  type: str
  'Type of swap.'


class Target(TypedDict):
  """TypedDict representation of the Target schema."""

  target_id: int
  'The ID of the target to swap number.'
  target_type: Literal[
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
  'The type of the target.'


class SwapNumberMessage(TypedDict):
  """TypedDict representation of the SwapNumberMessage schema."""

  swap_details: NotRequired[Union[AreaCodeSwap, AutoSwap, ProvidedNumberSwap]]
  'Type of number swap (area_code, auto, provided_number).'
  target: Target
  'The target for swap number.'


class UnassignNumberMessage(TypedDict):
  """TypedDict representation of the UnassignNumberMessage schema."""

  number: str
  'A phone number to unassign. (e164-formatted)'
