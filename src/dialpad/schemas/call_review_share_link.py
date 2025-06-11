from typing import Literal

from typing_extensions import NotRequired, TypedDict


class CallReviewShareLink(TypedDict):
  """Reponse for the call review share link."""

  access_link: NotRequired[str]
  'The access link where the call review can be listened or downloaded.'
  call_id: NotRequired[int]
  "The call's id."
  id: NotRequired[str]
  "The call review share link's ID."
  privacy: NotRequired[Literal['company', 'public']]
  'The privacy state of the call review sharel link.'


class CreateCallReviewShareLink(TypedDict):
  """Input for POST request to create a call review share link."""

  call_id: NotRequired[int]
  "The call's id."
  privacy: NotRequired[Literal['company', 'public']]
  "The privacy state of the recording share link, 'company' will be set as default."


class UpdateCallReviewShareLink(TypedDict):
  """Input for PUT request to update a call review share link."""

  privacy: Literal['company', 'public']
  'The privacy state of the recording share link'
