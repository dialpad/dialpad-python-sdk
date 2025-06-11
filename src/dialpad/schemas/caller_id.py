from typing_extensions import NotRequired, TypedDict


class GroupProto(TypedDict):
  """Group caller ID."""

  caller_id: NotRequired[str]
  'A caller id from the operator group. (e164-formatted)'
  display_name: NotRequired[str]
  '[single-line only]\n\nThe operator group display name'


class CallerIdProto(TypedDict):
  """Caller ID."""

  caller_id: NotRequired[str]
  'The caller id number for the user'
  forwarding_numbers: NotRequired[list[str]]
  "A list of phone numbers that should be dialed in addition to the user's Dialpad number(s)\nupon receiving a call."
  groups: NotRequired[list[GroupProto]]
  'The groups from the user'
  id: int
  'The ID of the user.'
  office_main_line: NotRequired[str]
  'The office main line number'
  phone_numbers: NotRequired[list[str]]
  'A list of phone numbers belonging to this user.'
  primary_phone: NotRequired[str]
  'The user primary phone number'


class SetCallerIdMessage(TypedDict):
  """TypedDict representation of the SetCallerIdMessage schema."""

  caller_id: str
  "Phone number (e164 formatted) that will be defined as a Caller ID for the target. Use 'blocked' to block the Caller ID."
