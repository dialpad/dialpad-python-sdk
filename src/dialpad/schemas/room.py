from typing import Literal

from typing_extensions import NotRequired, TypedDict


class CreateInternationalPinProto(TypedDict):
  """Input to create a PIN for protected international calls from room."""

  customer_ref: NotRequired[str]
  '[single-line only]\n\nAn identifier to be printed in the usage summary. Typically used for identifying the person who requested the PIN.'


class CreateRoomMessage(TypedDict):
  """TypedDict representation of the CreateRoomMessage schema."""

  name: str
  '[single-line only]\n\nThe name of the room.'
  office_id: int
  'The office in which this room resides.'


class InternationalPinProto(TypedDict):
  """Full response body for get pin operation."""

  customer_ref: NotRequired[str]
  '[single-line only]\n\nAn identifier to be printed in the usage summary. Typically used for identifying the person who requested the PIN.'
  expires_on: NotRequired[str]
  'A time after which the PIN will no longer be valid.'
  pin: NotRequired[str]
  'A PIN that must be entered to make international calls.'


class RoomProto(TypedDict):
  """Room."""

  company_id: NotRequired[int]
  "The ID of this room's company."
  country: NotRequired[str]
  'The country in which the room resides.'
  id: NotRequired[int]
  'The ID of the room.'
  image_url: NotRequired[str]
  'The profile image to use when displaying this room in the Dialpad app.'
  is_free: NotRequired[bool]
  'A boolean indicating whether this room is consuming a license with an associated cost.'
  is_on_duty: NotRequired[bool]
  'A boolean indicating whether this room is actively acting as an operator.'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the room.'
  office_id: NotRequired[int]
  "The ID of this room's office."
  phone_numbers: NotRequired[list[str]]
  'The phone numbers assigned to this room.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The current enablement state of this room.'


class RoomCollection(TypedDict):
  """Collection of rooms."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[RoomProto]]
  'A list of rooms.'


class UpdateRoomMessage(TypedDict):
  """TypedDict representation of the UpdateRoomMessage schema."""

  name: NotRequired[str]
  '[single-line only]\n\nThe name of the room.'
  phone_numbers: NotRequired[list[str]]
  'A list of all phone numbers assigned to the room.\n\nNumbers can be re-ordered or removed from this list to unassign them.'
