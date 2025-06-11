from typing import Literal, Union

from typing_extensions import NotRequired, TypedDict


class ReservedLineType(TypedDict):
  """Reserved number fax line assignment."""

  number: str
  'A phone number to assign. (e164-formatted)'
  type: str
  'Type of line.'


class SearchLineType(TypedDict):
  """Search fax line assignment."""

  area_code: str
  "An area code in which to find an available phone number for assignment. If there is no area code provided, office's area code will be used."
  type: str
  'Type of line.'


class Target(TypedDict):
  """TypedDict representation of the Target schema."""

  target_id: int
  'The ID of the target to assign the fax line to.'
  target_type: Literal['department', 'user']
  'Type of the target to assign the fax line to.'


class TollfreeLineType(TypedDict):
  """Tollfree fax line assignment."""

  type: str
  'Type of line.'


class CreateFaxNumberMessage(TypedDict):
  """TypedDict representation of the CreateFaxNumberMessage schema."""

  line: Union[ReservedLineType, SearchLineType, TollfreeLineType]
  'Line to assign.'
  target: Target
  'The target to assign the number to.'


class FaxNumberProto(TypedDict):
  """Fax number details."""

  area_code: NotRequired[str]
  'The area code of the number.'
  company_id: NotRequired[int]
  'The ID of the associated company.'
  number: str
  'A mock parameter for testing.'
  office_id: NotRequired[int]
  'The ID of the associate office.'
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
