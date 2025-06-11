from typing_extensions import NotRequired, TypedDict


class AppSettingProto(TypedDict):
  """App settings object."""

  enabled: NotRequired[bool]
  'Whether or not the OAuth app is enabled for the target.'
  is_preferred_service: NotRequired[bool]
  'Whether or not Oauth app is preferred service for screen pop.'
  settings: NotRequired[dict]
  'A dynamic object that maps settings to their values.\n\nIt includes all standard settings, i.e. call_logging_enabled, call_recording_logging_enabled,\nvoicemail_logging_enabled and sms_logging_enabled, and any custom settings this OAuth app supports.'
