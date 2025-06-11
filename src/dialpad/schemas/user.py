from typing import Literal

from typing_extensions import NotRequired, TypedDict


class CreateUserMessage(TypedDict):
  """TypedDict representation of the CreateUserMessage schema."""

  auto_assign: NotRequired[bool]
  'If set to true, a number will be automatically assigned.'
  email: str
  "The user's email."
  first_name: NotRequired[str]
  "[single-line only]\n\nThe user's first name."
  last_name: NotRequired[str]
  "[single-line only]\n\nThe user's last name."
  license: NotRequired[
    Literal[
      'admins',
      'agents',
      'dpde_all',
      'dpde_one',
      'lite_lines',
      'lite_support_agents',
      'magenta_lines',
      'talk',
    ]
  ]
  "The user's license type. This affects billing for the user."
  office_id: int
  "The user's office id."


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
  use_validated_option: NotRequired[bool]
  'Whether to use the validated address option from our service.'
  zip: str
  '[single-line only]\n\nZip of the new E911 address.'


class GroupDetailsProto(TypedDict):
  """TypedDict representation of the GroupDetailsProto schema."""

  do_not_disturb: NotRequired[bool]
  'Whether the user is currently in do-not-disturb mode for this group.'
  group_id: NotRequired[int]
  'The ID of the group.'
  group_type: NotRequired[
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
  'The group type.'
  role: NotRequired[Literal['admin', 'operator', 'supervisor']]
  "The user's role in the group."


class MoveOfficeMessage(TypedDict):
  """TypedDict representation of the MoveOfficeMessage schema."""

  office_id: NotRequired[int]
  "The user's office id. When provided, the user will be moved to this office."


class PersonaProto(TypedDict):
  """Persona."""

  caller_id: NotRequired[str]
  'Persona caller ID shown to receivers of calls from this persona.'
  id: NotRequired[int]
  "The user's id."
  image_url: NotRequired[str]
  'Persona image URL.'
  name: NotRequired[str]
  '[single-line only]\n\nPersona name.'
  phone_numbers: NotRequired[list[str]]
  'List of persona phone numbers.'
  type: NotRequired[str]
  'Persona type.\n\n(corresponds to a target type)'


class PersonaCollection(TypedDict):
  """Collection of personas."""

  items: NotRequired[list[PersonaProto]]
  'A list of user personas.'


class PresenceStatus(TypedDict):
  """TypedDict representation of the PresenceStatus schema."""

  message: NotRequired[str]
  'The presence status message to be updated.'
  provider: NotRequired[str]
  'The provider requesting the presence status update.'
  type: NotRequired[Literal['conference', 'default']]
  'Predefined templates will be only used for the supported types.\n\nAccepts the following types:\n- `default` -- status message template: "{provider}: {message}"\n- `conference` -- status message template: "On {provider}: in the {message} meeting"\n\n`provider` and `message` should be chosen with the message template in mind.'


class SetStatusMessage(TypedDict):
  """TypedDict representation of the SetStatusMessage schema."""

  expiration: NotRequired[int]
  'The expiration of this status. None for no expiration.'
  status_message: NotRequired[str]
  'The status message for the user.'


class SetStatusProto(TypedDict):
  """Set user status."""

  expiration: NotRequired[int]
  'The expiration of this status. None for no expiration.'
  id: NotRequired[int]
  "The user's id.\n\n('me' can be used if you are using a user level API key)"
  status_message: NotRequired[str]
  'The status message for the user.'


class ToggleDNDMessage(TypedDict):
  """TypedDict representation of the ToggleDNDMessage schema."""

  do_not_disturb: bool
  'Determines if DND is ON or OFF.'
  group_id: NotRequired[int]
  "The ID of the group which the user's DND status will be updated for."
  group_type: NotRequired[Literal['callcenter', 'department', 'office']]
  "The type of the group which the user's DND status will be updated for."


class ToggleDNDProto(TypedDict):
  """DND toggle."""

  do_not_disturb: NotRequired[bool]
  'Boolean to tell if the user is on DND.'
  group_id: NotRequired[int]
  "The ID of the group which the user's DND status will be updated for."
  group_type: NotRequired[Literal['callcenter', 'department', 'office']]
  "The type of the group which the user's DND status will be updated for."
  id: NotRequired[int]
  "The user's id.\n\n('me' can be used if you are using a user level API key)"


class UpdateUserMessage(TypedDict):
  """TypedDict representation of the UpdateUserMessage schema."""

  admin_office_ids: NotRequired[list[int]]
  'The list of admin office IDs.\n\nThis is used to set the user as an office admin for the offices with the provided IDs.'
  emails: NotRequired[list[str]]
  "The user's emails.\n\nThis can be used to add, remove, or re-order emails. The first email in the list is the user's primary email."
  extension: NotRequired[str]
  "The user's new extension number.\n\nExtensions are optional in Dialpad and turned off by default. If you want extensions please contact support to enable them."
  first_name: NotRequired[str]
  "[single-line only]\n\nThe user's first name."
  forwarding_numbers: NotRequired[list[str]]
  "A list of phone numbers that should be dialed in addition to the user's Dialpad number(s)\nupon receiving a call."
  international_dialing_enabled: NotRequired[bool]
  'Whether or not the user is enabled to dial internationally.'
  is_super_admin: NotRequired[bool]
  'Whether or not the user is a super admin. (company level administrator)'
  job_title: NotRequired[str]
  "[single-line only]\n\nThe user's job title."
  keep_paid_numbers: NotRequired[bool]
  'Whether or not to keep phone numbers when switching to a support license.\n\nNote: Phone numbers require additional number licenses under a support license.'
  last_name: NotRequired[str]
  "[single-line only]\n\nThe user's last name."
  license: NotRequired[
    Literal[
      'admins',
      'agents',
      'dpde_all',
      'dpde_one',
      'lite_lines',
      'lite_support_agents',
      'magenta_lines',
      'talk',
    ]
  ]
  "The user's license type.\n\nChanging this affects billing for the user. For a Sell license, specify the type as `agents`. For a Support license, specify the type as `support`."
  office_id: NotRequired[int]
  "The user's office id.\n\nIf provided, the user will be moved to this office. For international offices, the user must not have phone numbers assigned. Once the transfer is complete, your admin can add the phone numbers via the user assign number API. Only supported on paid accounts and there must be enough licenses to transfer the user to the destination office."
  phone_numbers: NotRequired[list[str]]
  'A list of the phone number(s) assigned to this user.\n\nThis can be used to re-order or remove numbers. To assign a new number, use the assign number API instead.'
  presence_status: NotRequired[PresenceStatus]
  'The presence status can be seen when you hover your mouse over the presence state indicator.\n\nNOTE: this is only used for Highfive and will be deprecated soon.\n\nPresence status will be set to "{provider}: {message}" when both are provided. Otherwise,\npresence status will be set to "{provider}".\n\n"type" is optional and presence status will only include predefined templates when "type" is provided. Please refer to the "type" parameter to check the supported types.\n\nTo clear the presence status, make an api call with the "presence_status" param set to empty or null. ex: `"presence_status": {}` or `"presence_status": null`\n\nTranslations will be available for the text in predefined templates. Translations for others should be provided.'
  state: NotRequired[Literal['active', 'suspended']]
  "The user's state.\n\nThis is used to suspend or re-activate a user."


class UserProto(TypedDict):
  """User."""

  admin_office_ids: NotRequired[list[int]]
  'A list of office IDs for which this user has admin privilages.'
  company_id: NotRequired[int]
  "The id of the user's company."
  country: NotRequired[str]
  'The country in which the user resides.'
  date_active: NotRequired[str]
  'The date when the user activated their Dialpad account.'
  date_added: NotRequired[str]
  'A timestamp indicating when this user was created.'
  date_first_login: NotRequired[str]
  'A timestamp indicating the first time that this user logged in to Dialpad.'
  display_name: NotRequired[str]
  "The user's name, for display purposes."
  do_not_disturb: NotRequired[bool]
  'A boolean indicating whether the user is currently in "Do not disturb" mode.'
  duty_status_reason: NotRequired[str]
  '[single-line only]\n\nA description of this status.'
  duty_status_started: NotRequired[str]
  'The timestamp, in UTC, when the current on duty status changed.'
  emails: NotRequired[list[str]]
  'A list of email addresses belonging to this user.'
  extension: NotRequired[str]
  'The extension that should be associated with this user in the company or office IVR directory.'
  first_name: NotRequired[str]
  '[single-line only]\n\nThe given name of the user.'
  forwarding_numbers: NotRequired[list[str]]
  "A list of phone numbers that should be dialed in addition to the user's Dialpad number(s)\nupon receiving a call."
  group_details: NotRequired[list[GroupDetailsProto]]
  'Details regarding the groups that this user is a member of.'
  id: NotRequired[int]
  "The user's id."
  image_url: NotRequired[str]
  "The url of the user's profile image."
  international_dialing_enabled: NotRequired[bool]
  'Whether or not the user is enabled to dial internationally.'
  is_admin: NotRequired[bool]
  'A boolean indicating whether this user has administor privilages.'
  is_available: NotRequired[bool]
  'A boolean indicating whether the user is not currently on a call.'
  is_on_duty: NotRequired[bool]
  'A boolean indicating whether this user is currently acting as an operator.'
  is_online: NotRequired[bool]
  'A boolean indicating whether the user currently has an active Dialpad device.'
  is_super_admin: NotRequired[bool]
  'A boolean indicating whether this user has company-wide administor privilages.'
  job_title: NotRequired[str]
  "[single-line only]\n\nThe user's job title."
  language: NotRequired[str]
  'The preferred spoken language of the user.'
  last_name: NotRequired[str]
  '[single-line only]\n\nThe family name of the user.'
  license: NotRequired[
    Literal[
      'admins',
      'agents',
      'dpde_all',
      'dpde_one',
      'lite_lines',
      'lite_support_agents',
      'magenta_lines',
      'talk',
    ]
  ]
  'The license type that has been allocated to this user.'
  location: NotRequired[str]
  '[single-line only]\n\nThe self-reported location of the user.'
  muted: NotRequired[bool]
  'A boolean indicating whether the user has muted thier microphone.'
  office_id: NotRequired[int]
  "The ID of the user's office."
  on_duty_started: NotRequired[str]
  'The timestamp, in UTC, when this operator became available for contact center calls.'
  on_duty_status: NotRequired[
    Literal['available', 'busy', 'occupied', 'occupied-end', 'unavailable', 'wrapup', 'wrapup-end']
  ]
  "A description of operator's on duty status."
  phone_numbers: NotRequired[list[str]]
  'A list of phone numbers belonging to this user.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The current enablement state of the user.'
  status_message: NotRequired[str]
  '[single-line only]\n\nA message indicating the activity that the user is currently engaged in.'
  timezone: NotRequired[str]
  'The timezone that this user abides by.'


class UserCollection(TypedDict):
  """Collection of users."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[UserProto]]
  'A list of users.'
