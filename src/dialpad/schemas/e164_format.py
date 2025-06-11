from typing_extensions import NotRequired, TypedDict


class FormatNumberResponse(TypedDict):
  """Formatted number."""

  area_code: NotRequired[str]
  'First portion of local formatted number. e.g. "(555)"'
  country_code: NotRequired[str]
  'Abbreviated country name in ISO 3166-1 alpha-2 format. e.g. "US"'
  e164_number: NotRequired[str]
  'Number in local format.\n\ne.g. "(555) 555-5555"'
  local_number: NotRequired[str]
  'Number in E.164 format. e.g. "+15555555555"'
