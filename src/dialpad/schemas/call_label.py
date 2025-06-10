from typing import Optional, List, Dict, Union, Literal
from typing_extensions import TypedDict, NotRequired


class CompanyCallLabels(TypedDict):
  """Company Labels."""

  labels: NotRequired[list[str]]
  'The labels associated to this company.'
