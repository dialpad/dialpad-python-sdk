from typing_extensions import NotRequired, TypedDict


class CompanyCallLabels(TypedDict):
  """Company Labels."""

  labels: NotRequired[list[str]]
  'The labels associated to this company.'
