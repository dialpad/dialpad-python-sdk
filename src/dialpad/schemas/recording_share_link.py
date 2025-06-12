from typing import Literal

from typing_extensions import NotRequired, TypedDict


class CreateRecordingShareLink(TypedDict):
  """TypedDict representation of the CreateRecordingShareLink schema."""

  privacy: NotRequired[Literal['admin', 'company', 'owner', 'public']]
  'The privacy state of the recording share link.'
  recording_id: str
  "The recording entity's ID."
  recording_type: Literal['admincallrecording', 'callrecording', 'voicemail']
  'The type of the recording entity shared via the link.'


class RecordingShareLink(TypedDict):
  """Recording share link."""

  access_link: NotRequired[str]
  'The access link where recording can be listened or downloaded.'
  call_id: NotRequired[int]
  "The call's id."
  created_by_id: NotRequired[int]
  'The ID of the target who created the link.'
  date_added: NotRequired[str]
  'The date when the recording share link is created.'
  id: NotRequired[str]
  "The recording share link's ID."
  item_id: NotRequired[str]
  'The ID of the recording entity shared via the link.'
  privacy: NotRequired[Literal['admin', 'company', 'owner', 'public']]
  'The privacy state of the recording share link.'
  type: NotRequired[Literal['admincallrecording', 'callrecording', 'voicemail']]
  'The type of the recording entity shared via the link.'


class UpdateRecordingShareLink(TypedDict):
  """TypedDict representation of the UpdateRecordingShareLink schema."""

  privacy: Literal['admin', 'company', 'owner', 'public']
  'The privacy state of the recording share link.'
