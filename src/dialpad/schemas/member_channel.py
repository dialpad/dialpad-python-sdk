from typing_extensions import NotRequired, TypedDict


class AddChannelMemberMessage(TypedDict):
  """Input to add members to a channel"""

  user_id: int
  'The user id.'


class MembersProto(TypedDict):
  """Channel member."""

  id: NotRequired[int]
  'The user id.'
  name: NotRequired[str]
  '[single-line only]\n\nThe user name.'


class MembersCollection(TypedDict):
  """Collection of channel members."""

  cursor: NotRequired[str]
  'A token used to return the next page of results.'
  items: NotRequired[list[MembersProto]]
  'A list of membser from channels.'


class RemoveChannelMemberMessage(TypedDict):
  """Input to remove members from a channel"""

  user_id: int
  'The user id.'
