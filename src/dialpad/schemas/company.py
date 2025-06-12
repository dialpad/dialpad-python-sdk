from typing import Literal

from typing_extensions import NotRequired, TypedDict


class CompanyProto(TypedDict):
  """Company."""

  account_type: NotRequired[Literal['enterprise', 'free', 'pro', 'standard']]
  'Company pricing tier.'
  admin_email: NotRequired[str]
  'Email address of the company administrator.'
  country: NotRequired[str]
  'Primary country of the company.'
  domain: NotRequired[str]
  '[single-line only]\n\nDomain name of user emails.'
  id: NotRequired[int]
  "The company's id."
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the company.'
  office_count: NotRequired[int]
  'The number of offices belonging to this company'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'Enablement state of the company.'
