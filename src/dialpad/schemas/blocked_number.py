from typing_extensions import NotRequired, TypedDict


class AddBlockedNumbersProto(TypedDict):
  """TypedDict representation of the AddBlockedNumbersProto schema."""

  numbers: NotRequired[list[str]]
  'A list of E164 formatted numbers.'


class BlockedNumber(TypedDict):
  """Blocked number."""

  number: NotRequired[str]
  'A phone number (e164 format).'


class BlockedNumberCollection(TypedDict):
  """Collection of blocked numbers."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[BlockedNumber]]
  'A list of blocked numbers.'


class RemoveBlockedNumbersProto(TypedDict):
  """TypedDict representation of the RemoveBlockedNumbersProto schema."""

  numbers: NotRequired[list[str]]
  'A list of E164 formatted numbers.'
