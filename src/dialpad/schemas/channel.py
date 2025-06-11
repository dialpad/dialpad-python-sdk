from typing import Literal

from typing_extensions import NotRequired, TypedDict


class ChannelProto(TypedDict):
  """Channel."""

  id: NotRequired[int]
  'The channel id.'
  name: str
  '[single-line only]\n\nThe channel name.'


class ChannelCollection(TypedDict):
  """Collection of channels."""

  cursor: NotRequired[str]
  'A token used to return the next page of results.'
  items: NotRequired[list[ChannelProto]]
  'A list of channels.'


class CreateChannelMessage(TypedDict):
  """TypedDict representation of the CreateChannelMessage schema."""

  description: str
  'The description of the channel.'
  name: str
  '[single-line only]\n\nThe name of the channel.'
  privacy_type: Literal['private', 'public']
  'The privacy type of the channel.'
  user_id: NotRequired[int]
  'The ID of the user who owns the channel. Just for company level API key.'
