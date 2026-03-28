from typing import Literal

from typing_extensions import NotRequired, TypedDict


class ToggleOAuthAppMessage(TypedDict):
  """Request body for enabling or disabling an OAuth app for a given target."""

  enable: bool
  'Whether or not the OAuth app should be enabled.'
  target_id: NotRequired[int]
  'The id of the target that the OAuth app should be toggled for.'
  target_type: NotRequired[
    Literal['callcenter', 'company', 'department', 'office', 'user']
  ]
  'The type of the target that the OAuth app should be toggled for.'


class ToggleOAuthAppProto(TypedDict):
  """OAuth app toggle state."""

  oauth_app_id: NotRequired[str]
  "The OAuth app's id."
  target_id: NotRequired[int]
  'The id of the target that the OAuth app is connected.'
  target_type: NotRequired[str]
  'The type of the target that the OAuth app is connected.'
  is_enabled: NotRequired[bool]
  'Whether or not OAuth app is enabled.'
