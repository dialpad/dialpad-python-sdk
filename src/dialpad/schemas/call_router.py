from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.signature import SignatureProto


class ApiCallRouterProto(TypedDict):
  """API call router."""

  default_target_id: NotRequired[int]
  'The ID of the target that should be used as a fallback destination for calls if the call router is disabled or fails.'
  default_target_type: NotRequired[
    Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ]
  ]
  'The entity type of the default target.'
  enabled: NotRequired[bool]
  'If set to False, the call router will skip the routing url and instead forward calls straight to the default target.'
  id: NotRequired[int]
  "The API call router's ID."
  name: NotRequired[str]
  '[single-line only]\n\nA human-readable display name for the router.'
  office_id: NotRequired[int]
  'The ID of the office to which this router belongs.'
  phone_numbers: NotRequired[list[str]]
  'The phone numbers that will cause inbound calls to hit this call router.'
  routing_url: NotRequired[str]
  'The URL that should be used to drive call routing decisions.'
  signature: NotRequired[SignatureProto]
  'The signature that will be used to sign JWTs for routing requests.'


class ApiCallRouterCollection(TypedDict):
  """Collection of API call routers."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[ApiCallRouterProto]]
  'A list of call routers.'


class CreateApiCallRouterMessage(TypedDict):
  """TypedDict representation of the CreateApiCallRouterMessage schema."""

  default_target_id: int
  'The ID of the target that should be used as a fallback destination for calls if the call router is disabled or fails.'
  default_target_type: Literal[
    'callcenter',
    'callrouter',
    'channel',
    'coachinggroup',
    'coachingteam',
    'department',
    'office',
    'room',
    'staffgroup',
    'unknown',
    'user',
  ]
  'The entity type of the default target.'
  enabled: NotRequired[bool]
  'If set to False, the call router will skip the routing url and instead forward calls straight to the default target.'
  name: str
  '[single-line only]\n\nA human-readable display name for the router.'
  office_id: int
  'The ID of the office to which this router belongs.'
  routing_url: str
  'The URL that should be used to drive call routing decisions.'
  secret: NotRequired[str]
  "[single-line only]\n\nThe call router's signature secret. This is a plain text string that you should generate with a minimum length of 32 characters."


class UpdateApiCallRouterMessage(TypedDict):
  """TypedDict representation of the UpdateApiCallRouterMessage schema."""

  default_target_id: NotRequired[int]
  'The ID of the target that should be used as a fallback destination for calls if the call router is disabled or fails.'
  default_target_type: NotRequired[
    Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ]
  ]
  'The entity type of the default target.'
  enabled: NotRequired[bool]
  'If set to False, the call router will skip the routing url and instead forward calls straight to the default target.'
  name: NotRequired[str]
  '[single-line only]\n\nA human-readable display name for the router.'
  office_id: NotRequired[int]
  'The ID of the office to which this router belongs.'
  reset_error_count: NotRequired[bool]
  'Sets the auto-disablement routing error count back to zero.\n\nCall routers maintain a count of the number of errors that have occured within the past hour, and automatically become disabled when that count exceeds 10.\n\nSetting enabled to true via the API will not reset that count, which means that the router will likely become disabled again after one more error. In most cases, this will be useful for testing fixes in your routing API, but in some circumstances it may be desirable to reset that counter.'
  routing_url: NotRequired[str]
  'The URL that should be used to drive call routing decisions.'
  secret: NotRequired[str]
  "[single-line only]\n\nThe call router's signature secret. This is a plain text string that you should generate with a minimum length of 32 characters."
