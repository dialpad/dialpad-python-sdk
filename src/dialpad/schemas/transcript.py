from typing import Literal

from typing_extensions import NotRequired, TypedDict


class TranscriptLineProto(TypedDict):
  """Transcript line."""

  contact_id: NotRequired[str]
  'The ID of the contact who was speaking.'
  content: NotRequired[str]
  'The transcribed text.'
  name: NotRequired[str]
  'The name of the call participant who was speaking.'
  time: NotRequired[str]
  'The time at which the line was spoken.'
  type: NotRequired[
    Literal['ai_question', 'custom_moment', 'moment', 'real_time_moment', 'transcript']
  ]
  'Either "moment" or "transcript".'
  user_id: NotRequired[int]
  'The ID of the user who was speaking.'


class TranscriptProto(TypedDict):
  """Transcript."""

  call_id: NotRequired[int]
  "The call's id."
  lines: NotRequired[list[TranscriptLineProto]]
  'An array of individual lines of the transcript.'


class TranscriptUrlProto(TypedDict):
  """Transcript URL."""

  call_id: NotRequired[int]
  "The call's id."
  url: NotRequired[str]
  'The url with which the call transcript can be accessed.'
