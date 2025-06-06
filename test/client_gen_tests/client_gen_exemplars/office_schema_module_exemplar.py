from typing import Optional, List, Dict, Union, Literal
from typing_extensions import TypedDict, NotRequired
from dialpad.schemas.group import RoutingOptions, VoiceIntelligence
from dialpad.schemas.plan import BillingContactMessage, BillingPointOfContactMessage, PlanProto


class E911Message(TypedDict):
  """E911 address."""

  address: Optional[str]
  '[single-line only]\n\nLine 1 of the E911 address.'
  address2: NotRequired[Optional[str]]
  '[single-line only]\n\nLine 2 of the E911 address.'
  city: Optional[str]
  '[single-line only]\n\nCity of the E911 address.'
  country: Optional[str]
  'Country of the E911 address.'
  state: Optional[str]
  '[single-line only]\n\nState or Province of the E911 address.'
  zip: Optional[str]
  '[single-line only]\n\nZip code of the E911 address.'


class CreateOfficeMessage(TypedDict):
  """Secondary Office creation."""

  annual_commit_monthly_billing: Optional[bool]
  "A flag indicating if the primary office's plan is categorized as annual commit monthly billing."
  auto_call_recording: NotRequired[Optional[bool]]
  'Whether or not automatically record all calls of this office. Default is False.'
  billing_address: Optional[BillingContactMessage]
  'The billing address of this created office.'
  billing_contact: NotRequired[Optional[BillingPointOfContactMessage]]
  'The billing contact information of this created office.'
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
  'The office country.'
  currency: Optional[Literal['AUD', 'CAD', 'EUR', 'GBP', 'JPY', 'NZD', 'USD']]
  "The office's billing currency."
  e911_address: NotRequired[Optional[E911Message]]
  'The emergency address of the created office.\n\nRequired for country codes of US, CA, AU, FR, GB, NZ.'
  first_action: NotRequired[Optional[Literal['menu', 'operators']]]
  'The desired action when the office receives a call.'
  friday_hours: NotRequired[Optional[list[str]]]
  'The Friday hours of operation. Default value is ["08:00", "18:00"].'
  group_description: NotRequired[Optional[str]]
  'The description of the office. Max 256 characters.'
  hours_on: NotRequired[Optional[bool]]
  'The time frame when the office wants to receive calls. Default value is false, which means the office will always take calls (24/7).'
  international_enabled: NotRequired[Optional[bool]]
  'A flag indicating if the primary office is able to make international phone calls.'
  invoiced: Optional[bool]
  'A flag indicating if the payment will be paid by invoice.'
  mainline_number: NotRequired[Optional[str]]
  'The mainline of the office.'
  monday_hours: NotRequired[Optional[list[str]]]
  'The Monday hours of operation. To specify when hours_on is set to True. e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM. Default value is ["08:00", "18:00"].'
  name: Optional[str]
  '[single-line only]\n\nThe office name.'
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
  'The action to take if there is no one available to answer calls.'
  plan_period: Optional[Literal['monthly', 'yearly']]
  'The frequency at which the company will be billed.'
  ring_seconds: NotRequired[Optional[int]]
  'The number of seconds to allow the group line to ring before going to voicemail. Choose from 10 seconds to 45 seconds.'
  routing_options: NotRequired[Optional[RoutingOptions]]
  'Call routing options for this group.'
  saturday_hours: NotRequired[Optional[list[str]]]
  'The Saturday hours of operation. Default is empty array.'
  sunday_hours: NotRequired[Optional[list[str]]]
  'The Sunday hours of operation. Default is empty array.'
  thursday_hours: NotRequired[Optional[list[str]]]
  'The Thursday hours of operation. Default value is ["08:00", "18:00"].'
  timezone: NotRequired[Optional[str]]
  'Timezone using a tz database name.'
  tuesday_hours: NotRequired[Optional[list[str]]]
  'The Tuesday hours of operation. Default value is ["08:00", "18:00"].'
  unified_billing: Optional[bool]
  'A flag indicating if to send a unified invoice.'
  use_same_address: NotRequired[Optional[bool]]
  'A flag indicating if the billing address and the emergency address are the same.'
  voice_intelligence: NotRequired[Optional[VoiceIntelligence]]
  'Configure voice intelligence.'
  wednesday_hours: NotRequired[Optional[list[str]]]
  'The Wednesday hours of operation. Default value is ["08:00", "18:00"].'


class E911GetProto(TypedDict):
  """E911 address."""

  address: NotRequired[Optional[str]]
  '[single-line only]\n\nLine 1 of the E911 address.'
  address2: NotRequired[Optional[str]]
  '[single-line only]\n\nLine 2 of the E911 address.'
  city: NotRequired[Optional[str]]
  '[single-line only]\n\nCity of the E911 address.'
  country: NotRequired[Optional[str]]
  'Country of the E911 address.'
  state: NotRequired[Optional[str]]
  '[single-line only]\n\nState or Province of the E911 address.'
  zip: NotRequired[Optional[str]]
  '[single-line only]\n\nZip code of the E911 address.'


class E911UpdateMessage(TypedDict):
  """TypedDict representation of the E911UpdateMessage schema."""

  address: Optional[str]
  '[single-line only]\n\nLine 1 of the new E911 address.'
  address2: NotRequired[Optional[str]]
  '[single-line only]\n\nLine 2 of the new E911 address.'
  city: Optional[str]
  '[single-line only]\n\nCity of the new E911 address.'
  country: Optional[str]
  'Country of the new E911 address.'
  state: Optional[str]
  '[single-line only]\n\nState or Province of the new E911 address.'
  update_all: NotRequired[Optional[bool]]
  'Update E911 for all users in this office.'
  use_validated_option: NotRequired[Optional[bool]]
  'Whether to use the validated address option from our service.'
  zip: Optional[str]
  '[single-line only]\n\nZip code of the new E911 address.'


class OffDutyStatusesProto(TypedDict):
  """Off-duty statuses."""

  id: NotRequired[Optional[int]]
  'The office ID.'
  off_duty_statuses: NotRequired[Optional[list[str]]]
  'The off-duty statuses configured for this office.'


class OfficeSettings(TypedDict):
  """TypedDict representation of the OfficeSettings schema."""

  allow_device_guest_login: NotRequired[Optional[bool]]
  'Allows guests to use desk phones within the office.'
  block_caller_id_disabled: NotRequired[Optional[bool]]
  'Whether the block-caller-ID option is disabled.'
  bridged_target_recording_allowed: NotRequired[Optional[bool]]
  'Whether recordings are enabled for sub-groups of this office.\n(e.g. departments or call centers).'
  disable_desk_phone_self_provision: NotRequired[Optional[bool]]
  'Whether desk-phone self-provisioning is disabled.'
  disable_ivr_voicemail: NotRequired[Optional[bool]]
  'Whether the default IVR voicemail feature is disabled.'
  no_recording_message_on_user_calls: NotRequired[Optional[bool]]
  'Whether recording of user calls should be disabled.'
  set_caller_id_disabled: NotRequired[Optional[bool]]
  'Whether the caller-ID option is disabled.'


class OfficeProto(TypedDict):
  """Office."""

  availability_status: NotRequired[
    Optional[Literal['closed', 'holiday_closed', 'holiday_open', 'open']]
  ]
  'Availability status of the office.'
  country: NotRequired[Optional[str]]
  'The country in which the office is situated.'
  e911_address: NotRequired[Optional[E911GetProto]]
  'The e911 address of the office.'
  first_action: NotRequired[Optional[Literal['menu', 'operators']]]
  'The desired action when the office receives a call.'
  friday_hours: NotRequired[Optional[list[str]]]
  'The Friday hours of operation.'
  id: NotRequired[Optional[int]]
  "The office's id."
  is_primary_office: NotRequired[Optional[bool]]
  'A flag indicating if the office is a primary office of its company.'
  monday_hours: NotRequired[Optional[list[str]]]
  'The Monday hours of operation.\n(e.g. ["08:00", "12:00", "14:00", "18:00"] => open from 8AM to Noon, and from 2PM to 6PM.)'
  name: NotRequired[Optional[str]]
  '[single-line only]\n\nThe name of the office.'
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
  'The action to take if there is no one available to answer calls.'
  office_id: NotRequired[Optional[int]]
  "The office's id."
  office_settings: NotRequired[Optional[OfficeSettings]]
  'Office-specific settings object.'
  phone_numbers: NotRequired[Optional[list[str]]]
  'The phone number(s) assigned to this office.'
  ring_seconds: NotRequired[Optional[int]]
  'The number of seconds to ring the main line before going to voicemail.\n(or an other-wise-specified no_operators_action).'
  routing_options: NotRequired[Optional[RoutingOptions]]
  'Specific call routing action to take when the office is open or closed.'
  saturday_hours: NotRequired[Optional[list[str]]]
  'The Saturday hours of operation.'
  state: NotRequired[Optional[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]]
  'The enablement-state of the office.'
  sunday_hours: NotRequired[Optional[list[str]]]
  'The Sunday hours of operation.'
  thursday_hours: NotRequired[Optional[list[str]]]
  'The Thursday hours of operation.'
  timezone: NotRequired[Optional[str]]
  'Timezone of the office.'
  tuesday_hours: NotRequired[Optional[list[str]]]
  'The Tuesday hours of operation.'
  wednesday_hours: NotRequired[Optional[list[str]]]
  'The Wednesday hours of operation.'


class OfficeCollection(TypedDict):
  """Collection of offices."""

  cursor: NotRequired[Optional[str]]
  'A token used to return the next page of results.'
  items: NotRequired[Optional[list[OfficeProto]]]
  'A list of offices.'


class OfficeUpdateResponse(TypedDict):
  """Office update."""

  office: NotRequired[Optional[OfficeProto]]
  'The updated office object.'
  plan: NotRequired[Optional[PlanProto]]
  'The updated office plan object.'
