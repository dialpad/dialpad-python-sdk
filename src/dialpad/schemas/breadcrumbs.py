from typing import Literal

from typing_extensions import NotRequired, TypedDict


class ApiCallRouterBreadcrumb(TypedDict):
  """Call routing breadcrumb."""

  breadcrumb_type: NotRequired[Literal['callrouter', 'external_api']]
  'Breadcrumb type'
  date: NotRequired[int]
  'Date when this breadcrumb was added'
  request: NotRequired[dict]
  'The HTTP request payload associated with this breadcrumb'
  response: NotRequired[dict]
  'The HTTP response associated with this breadcrumb'
  target_id: NotRequired[int]
  'The target id'
  target_type: NotRequired[str]
  'The target type from call'
  url: NotRequired[str]
  'The URL that should be used to drive call routing decisions.'
