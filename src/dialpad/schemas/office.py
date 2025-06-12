from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.group import RoutingOptions, VoiceIntelligence
from dialpad.schemas.plan import BillingContactMessage, BillingPointOfContactMessage, PlanProto


class E911Message(TypedDict):
  """E911 address."""

  address: str
  '[single-line only]\n\nLine 1 of the E911 address.'
  address2: NotRequired[str]
  '[single-line only]\n\nLine 2 of the E911 address.'
  city: str
  '[single-line only]\n\nCity of the E911 address.'
  country: str
  'Country of the E911 address.'
  state: str
  '[single-line only]\n\nState or Province of the E911 address.'
  zip: str
  '[single-line only]\n\nZip code of the E911 address.'


class CreateOfficeMessage(TypedDict):
  """Secondary Office creation."""

  annual_commit_monthly_billing: bool
  "A flag indicating if the primary office's plan is categorized as annual commit monthly billing."
  auto_call_recording: NotRequired[bool]
  'Whether or not automatically record all calls of this office. Default is False.'
  billing_address: BillingContactMessage
  'The billing address of this created office.'
  billing_contact: NotRequired[BillingPointOfContactMessage]
  'The billing contact information of this created office.'
  country: Literal[
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
  'The office country.'
  currency: Literal['AUD', 'CAD', 'EUR', 'GBP', 'JPY', 'NZD', 'USD']
  "The office's billing currency."
  e911_address: NotRequired[E911Message]
  'The emergency address of the created office.\n\nRequired for country codes of US, CA, AU, FR, GB, NZ.'
  first_action: NotRequired[Literal['menu', 'operators']]
  'The desired action when the office receives a call.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"].'
  group_description: NotRequired[str]
  'The description of the office. Max 256 characters.'
  hours_on: NotRequired[bool]
  'The time frame when the office wants to receive calls. Default value is false, which means the office will always take calls (24/7).'
  international_enabled: NotRequired[bool]
  'A flag indicating if the primary office is able to make international phone calls.'
  invoiced: bool
  'A flag indicating if the payment will be paid by invoice.'
  mainline_number: NotRequired[str]
  'The mainline of the office.'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: str
  '[single-line only]\n\nThe office name.'
  no_operators_action: NotRequired[
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
  'The action to take if there is no one available to answer calls.'
  plan_period: Literal['monthly', 'yearly']
  'The frequency at which the company will be billed.'
  ring_seconds: NotRequired[int]
  'The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds.'
  routing_options: NotRequired[RoutingOptions]
  'Call routing options for this group.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation. Default is empty array.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"].'
  timezone: NotRequired[str]
  'Timezone using a tz database name.'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"].'
  unified_billing: bool
  'A flag indicating if to send a unified invoice.'
  use_same_address: NotRequired[bool]
  'A flag indicating if the billing address and the emergency address are the same.'
  voice_intelligence: NotRequired[VoiceIntelligence]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"].'


class E911GetProto(TypedDict):
  """E911 address."""

  address: NotRequired[str]
  '[single-line only]\n\nLine 1 of the E911 address.'
  address2: NotRequired[str]
  '[single-line only]\n\nLine 2 of the E911 address.'
  city: NotRequired[str]
  '[single-line only]\n\nCity of the E911 address.'
  country: NotRequired[str]
  'Country of the E911 address.'
  state: NotRequired[str]
  '[single-line only]\n\nState or Province of the E911 address.'
  zip: NotRequired[str]
  '[single-line only]\n\nZip code of the E911 address.'


class E911UpdateMessage(TypedDict):
  """TypedDict representation of the E911UpdateMessage schema."""

  address: str
  '[single-line only]\n\nLine 1 of the new E911 address.'
  address2: NotRequired[str]
  '[single-line only]\n\nLine 2 of the new E911 address.'
  city: str
  '[single-line only]\n\nCity of the new E911 address.'
  country: str
  'Country of the new E911 address.'
  state: str
  '[single-line only]\n\nState or Province of the new E911 address.'
  update_all: NotRequired[bool]
  'Update E911 for all users in this office.'
  use_validated_option: NotRequired[bool]
  'Whether to use the validated address option from our service.'
  zip: str
  '[single-line only]\n\nZip code of the new E911 address.'


class OffDutyStatusesProto(TypedDict):
  """Off-duty statuses."""

  id: NotRequired[int]
  'The office ID.'
  off_duty_statuses: NotRequired[list[str]]
  'The off-duty statuses configured for this office.'


class OfficeSettings(TypedDict):
  """TypedDict representation of the OfficeSettings schema."""

  allow_device_guest_login: NotRequired[bool]
  'Allows guests to use desk phones within the office.'
  block_caller_id_disabled: NotRequired[bool]
  'Whether the block-caller-ID option is disabled.'
  bridged_target_recording_allowed: NotRequired[bool]
  'Whether recordings are enabled for sub-groups of this office.\n(e.g. departments or call centers).'
  disable_desk_phone_self_provision: NotRequired[bool]
  'Whether desk-phone self-provisioning is disabled.'
  disable_ivr_voicemail: NotRequired[bool]
  'Whether the default IVR voicemail feature is disabled.'
  no_recording_message_on_user_calls: NotRequired[bool]
  'Whether recording of user calls should be disabled.'
  set_caller_id_disabled: NotRequired[bool]
  'Whether the caller-ID option is disabled.'


class OfficeProto(TypedDict):
  """Office."""

  availability_status: NotRequired[Literal['closed', 'holiday_closed', 'holiday_open', 'open']]
  'Availability status of the office.'
  country: NotRequired[str]
  'The country in which the office is situated.'
  e911_address: NotRequired[E911GetProto]
  'The e911 address of the office.'
  first_action: NotRequired[Literal['menu', 'operators']]
  'The desired action when the office receives a call.'
  friday_hours: NotRequired[list[str]]
  'The Friday hours of operation.'
  id: NotRequired[int]
  "The office's id."
  is_primary_office: NotRequired[bool]
  'A flag indicating if the office is a primary office of its company.'
  monday_hours: NotRequired[list[str]]
  'The Monday hours of operation.\n(e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM.)'
  name: NotRequired[str]
  '[single-line only]\n\nThe name of the office.'
  no_operators_action: NotRequired[
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
  'The action to take if there is no one available to answer calls.'
  office_id: NotRequired[int]
  "The office's id."
  office_settings: NotRequired[OfficeSettings]
  'Office-specific settings object.'
  phone_numbers: NotRequired[list[str]]
  'The phone number(s) assigned to this office.'
  ring_seconds: NotRequired[int]
  'The number of seconds to ring the main line before going to voicemail.\n(or an other-wise-specified no_operators_action).'
  routing_options: NotRequired[RoutingOptions]
  'Specific call routing action to take when the office is open or closed.'
  saturday_hours: NotRequired[list[str]]
  'The Saturday hours of operation.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The enablement-state of the office.'
  sunday_hours: NotRequired[list[str]]
  'The Sunday hours of operation.'
  thursday_hours: NotRequired[list[str]]
  'The Thursday hours of operation.'
  timezone: NotRequired[str]
  'Timezone of the office.'
  tuesday_hours: NotRequired[list[str]]
  'The Tuesday hours of operation.'
  wednesday_hours: NotRequired[list[str]]
  'The Wednesday hours of operation.'


class OfficeCollection(TypedDict):
  """Collection of offices."""

  cursor: NotRequired[str]
  'A token used to return the next page of results.'
  items: NotRequired[list[OfficeProto]]
  'A list of offices.'


class OfficeUpdateResponse(TypedDict):
  """Office update."""

  office: NotRequired[OfficeProto]
  'The updated office object.'
  plan: NotRequired[PlanProto]
  'The updated office plan object.'
