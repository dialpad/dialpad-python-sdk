from typing_extensions import NotRequired, TypedDict


class RoomProto(TypedDict):
  """Public API representation of an UberConference room."""

  company_name: NotRequired[str]
  'The name of the company that owns the room.'
  display_name: NotRequired[str]
  'The name of the room.'
  email: NotRequired[str]
  'The email associated with the room owner.'
  id: NotRequired[str]
  'The ID of the meeting room.'
  number: NotRequired[str]
  'The e164-formatted dial-in number for the room.'
  path: NotRequired[str]
  'The access URL for the meeting room.'


class RoomCollection(TypedDict):
  """Collection of rooms for get all room operations."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request.\n\nUse the cursor provided in the previous response.'
  items: NotRequired[list[RoomProto]]
  'A list of meeting rooms.'
