from typing import Optional, List, Dict, Union, Literal
from typing_extensions import TypedDict, NotRequired


class E911Message(TypedDict):
  address: Optional[str]
  address2: NotRequired[Optional[str]]
  city: Optional[str]
  country: Optional[str]
  state: Optional[str]
  zip: Optional[str]


class CreateOfficeMessage(TypedDict):
  annual_commit_monthly_billing: Optional[bool]
  auto_call_recording: NotRequired[Optional[bool]]
  billing_address: Optional[BillingContactMessage]
  billing_contact: NotRequired[Optional[BillingPointOfContactMessage]]
  country: Optional[
    Literal[
      'AR',
      'AT',
      'AU',
      'BD',
      'BE',
      'BG',
      'BH',
      'BR',
      'CA',
      'CH',
      'CI',
      'CL',
      'CN',
      'CO',
      'CR',
      'CY',
      'CZ',
      'DE',
      'DK',
      'DO',
      'DP',
      'EC',
      'EE',
      'EG',
      'ES',
      'FI',
      'FR',
      'GB',
      'GH',
      'GR',
      'GT',
      'HK',
      'HR',
      'HU',
      'ID',
      'IE',
      'IL',
      'IN',
      'IS',
      'IT',
      'JP',
      'KE',
      'KH',
      'KR',
      'KZ',
      'LK',
      'LT',
      'LU',
      'LV',
      'MA',
      'MD',
      'MM',
      'MT',
      'MX',
      'MY',
      'NG',
      'NL',
      'NO',
      'NZ',
      'PA',
      'PE',
      'PH',
      'PK',
      'PL',
      'PR',
      'PT',
      'PY',
      'RO',
      'RU',
      'SA',
      'SE',
      'SG',
      'SI',
      'SK',
      'SV',
      'TH',
      'TR',
      'TW',
      'UA',
      'US',
      'UY',
      'VE',
      'VN',
      'ZA',
    ]
  ]
  currency: Optional[Literal['AUD', 'CAD', 'EUR', 'GBP', 'JPY', 'NZD', 'USD']]
  e911_address: NotRequired[Optional[E911Message]]
  first_action: NotRequired[Optional[Literal['menu', 'operators']]]
  friday_hours: NotRequired[Optional[list[str]]]
  group_description: NotRequired[Optional[str]]
  hours_on: NotRequired[Optional[bool]]
  international_enabled: NotRequired[Optional[bool]]
  invoiced: Optional[bool]
  mainline_number: NotRequired[Optional[str]]
  monday_hours: NotRequired[Optional[list[str]]]
  name: Optional[str]
  no_operators_action: NotRequired[
    Optional[
      Literal[
        'bridge_target',
        'company_directory',
        'department',
        'directory',
        'disabled',
        'extension',
        'menu',
        'message',
        'operator',
        'person',
        'scripted_ivr',
        'voicemail',
      ]
    ]
  ]
  plan_period: Optional[Literal['monthly', 'yearly']]
  ring_seconds: NotRequired[Optional[int]]
  routing_options: NotRequired[Optional[RoutingOptions]]
  saturday_hours: NotRequired[Optional[list[str]]]
  sunday_hours: NotRequired[Optional[list[str]]]
  thursday_hours: NotRequired[Optional[list[str]]]
  timezone: NotRequired[Optional[str]]
  tuesday_hours: NotRequired[Optional[list[str]]]
  unified_billing: Optional[bool]
  use_same_address: NotRequired[Optional[bool]]
  voice_intelligence: NotRequired[Optional[VoiceIntelligence]]
  wednesday_hours: NotRequired[Optional[list[str]]]


class E911GetProto(TypedDict):
  address: NotRequired[Optional[str]]
  address2: NotRequired[Optional[str]]
  city: NotRequired[Optional[str]]
  country: NotRequired[Optional[str]]
  state: NotRequired[Optional[str]]
  zip: NotRequired[Optional[str]]


class E911UpdateMessage(TypedDict):
  address: Optional[str]
  address2: NotRequired[Optional[str]]
  city: Optional[str]
  country: Optional[str]
  state: Optional[str]
  update_all: NotRequired[Optional[bool]]
  use_validated_option: NotRequired[Optional[bool]]
  zip: Optional[str]


class OffDutyStatusesProto(TypedDict):
  id: NotRequired[Optional[int]]
  off_duty_statuses: NotRequired[Optional[list[str]]]


class OfficeSettings(TypedDict):
  allow_device_guest_login: NotRequired[Optional[bool]]
  block_caller_id_disabled: NotRequired[Optional[bool]]
  bridged_target_recording_allowed: NotRequired[Optional[bool]]
  disable_desk_phone_self_provision: NotRequired[Optional[bool]]
  disable_ivr_voicemail: NotRequired[Optional[bool]]
  no_recording_message_on_user_calls: NotRequired[Optional[bool]]
  set_caller_id_disabled: NotRequired[Optional[bool]]


class OfficeProto(TypedDict):
  availability_status: NotRequired[
    Optional[Literal['closed', 'holiday_closed', 'holiday_open', 'open']]
  ]
  country: NotRequired[Optional[str]]
  e911_address: NotRequired[Optional[E911GetProto]]
  first_action: NotRequired[Optional[Literal['menu', 'operators']]]
  friday_hours: NotRequired[Optional[list[str]]]
  id: NotRequired[Optional[int]]
  is_primary_office: NotRequired[Optional[bool]]
  monday_hours: NotRequired[Optional[list[str]]]
  name: NotRequired[Optional[str]]
  no_operators_action: NotRequired[
    Optional[
      Literal[
        'bridge_target',
        'company_directory',
        'department',
        'directory',
        'disabled',
        'extension',
        'menu',
        'message',
        'operator',
        'person',
        'scripted_ivr',
        'voicemail',
      ]
    ]
  ]
  office_id: NotRequired[Optional[int]]
  office_settings: NotRequired[Optional[OfficeSettings]]
  phone_numbers: NotRequired[Optional[list[str]]]
  ring_seconds: NotRequired[Optional[int]]
  routing_options: NotRequired[Optional[RoutingOptions]]
  saturday_hours: NotRequired[Optional[list[str]]]
  state: NotRequired[Optional[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]]
  sunday_hours: NotRequired[Optional[list[str]]]
  thursday_hours: NotRequired[Optional[list[str]]]
  timezone: NotRequired[Optional[str]]
  tuesday_hours: NotRequired[Optional[list[str]]]
  wednesday_hours: NotRequired[Optional[list[str]]]


class OfficeCollection(TypedDict):
  cursor: NotRequired[Optional[str]]
  items: NotRequired[Optional[list[OfficeProto]]]


class OfficeUpdateResponse(TypedDict):
  office: NotRequired[Optional[OfficeProto]]
  plan: NotRequired[Optional[PlanProto]]
