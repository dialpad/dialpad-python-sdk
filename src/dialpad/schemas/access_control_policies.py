from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.user import UserProto


class AssignmentPolicyMessage(TypedDict):
  """Policy assignment message."""

  target_id: NotRequired[int]
  'Required if the policy is associated with a target (Office or Contact Center). Not required for a company level policy.'
  target_type: NotRequired[Literal['callcenter', 'company', 'office']]
  'Policy permissions applied at this target level. Defaults to company target type.'
  user_id: int
  "The user's id to be assigned to the policy."


class CreatePolicyMessage(TypedDict):
  """Create access control policy message."""

  description: NotRequired[str]
  '[single-line only]\n\nOptional description for the policy. Max 200 characters.'
  name: str
  '[single-line only]\n\nA human-readable display name for the policy. Max 50 characters.'
  owner_id: int
  'Owner for this policy i.e company admin.'
  permission_sets: list[
    Literal[
      'agent_settings_write',
      'agents_admins_manage_agents_settings_write',
      'agents_admins_skill_level_write',
      'auto_call_recording_and_transcription_settings_write',
      'business_hours_write',
      'call_blocking_spam_prevention_settings_write',
      'call_dispositions_settings_write',
      'call_routing_hours_settings_write',
      'cc_call_settings_write',
      'chrome_extension_compliance_settings_write',
      'csat_surveys_write',
      'dashboard_and_alerts_write',
      'dialpad_ai_settings_write',
      'holiday_hours_settings_write',
      'integrations_settings_write',
      'name_language_description_settings_write',
      'number_settings_write',
      'supervisor_settings_write',
    ]
  ]
  'List of permission associated with this policy.'
  target_type: NotRequired[Literal['callcenter', 'company', 'office']]
  'Policy permissions applied at this target level. Defaults to company target type.'


class PolicyProto(TypedDict):
  """API custom access control policy proto definition."""

  company_id: int
  "The company's id to which this policy belongs to."
  date_created: NotRequired[str]
  'A timestamp indicating when this custom policy was created.'
  date_updated: NotRequired[str]
  'A timestamp indicating when this custom policy was last modified.'
  description: NotRequired[str]
  '[single-line only]\n\nDescription for the custom policy.'
  id: int
  'The API custom policy ID.'
  name: str
  '[single-line only]\n\nA human-readable display name for the custom policy name.'
  owner_id: int
  'Target that created this policy i.e company admin.'
  permission_sets: list[
    Literal[
      'agent_settings_read',
      'agent_settings_write',
      'agents_admins_manage_agents_settings_read',
      'agents_admins_manage_agents_settings_write',
      'agents_admins_skill_level_read',
      'agents_admins_skill_level_write',
      'auto_call_recording_and_transcription_settings_read',
      'auto_call_recording_and_transcription_settings_write',
      'business_hours_read',
      'business_hours_write',
      'call_blocking_spam_prevention_settings_read',
      'call_blocking_spam_prevention_settings_write',
      'call_dispositions_settings_read',
      'call_dispositions_settings_write',
      'call_routing_hours_settings_read',
      'call_routing_hours_settings_write',
      'cc_call_settings_read',
      'cc_call_settings_write',
      'chrome_extension_compliance_settings_read',
      'chrome_extension_compliance_settings_write',
      'csat_surveys_read',
      'csat_surveys_write',
      'dashboard_and_alerts_read',
      'dashboard_and_alerts_write',
      'dialpad_ai_settings_read',
      'dialpad_ai_settings_write',
      'holiday_hours_settings_read',
      'holiday_hours_settings_write',
      'integrations_settings_read',
      'integrations_settings_write',
      'name_language_description_settings_read',
      'name_language_description_settings_write',
      'number_settings_read',
      'number_settings_write',
      'supervisor_settings_read',
      'supervisor_settings_write',
    ]
  ]
  'List of permission associated with this custom policy.'
  state: Literal['active', 'deleted']
  'Policy state. ex. active or deleted.'
  target_type: NotRequired[Literal['callcenter', 'company', 'office']]
  'Target level at which the policy permissions are applied. Defaults to company'


class PoliciesCollection(TypedDict):
  """Collection of custom policies."""

  cursor: NotRequired[str]
  'A cursor string that can be used to fetch the subsequent page.'
  items: NotRequired[list[PolicyProto]]
  'A list containing the first page of results.'


class PolicyTargetProto(TypedDict):
  """TypedDict representation of the PolicyTargetProto schema."""

  target_id: int
  'All targets associated with the policy.'
  target_type: NotRequired[Literal['callcenter', 'company', 'office']]
  'Policy permissions applied at this target level. Defaults to company target type.'


class PolicyAssignmentProto(TypedDict):
  """TypedDict representation of the PolicyAssignmentProto schema."""

  policy_targets: NotRequired[list[PolicyTargetProto]]
  'Policy targets associated with the role.'
  user: NotRequired[UserProto]
  'The user associated to the role.'


class PolicyAssignmentCollection(TypedDict):
  """Collection of policy assignments."""

  cursor: NotRequired[str]
  'A cursor string that can be used to fetch the subsequent page.'
  items: NotRequired[list[PolicyAssignmentProto]]
  'A list containing the first page of results.'


class UnassignmentPolicyMessage(TypedDict):
  """Policy unassignment message."""

  target_id: NotRequired[int]
  'Required if the policy is associated with a target (Office or Contact Center). Not required for a company level policy or if unassign_all is True.'
  target_type: NotRequired[Literal['callcenter', 'company', 'office']]
  'Policy permissions applied at this target level. Defaults to company target type.'
  unassign_all: NotRequired[bool]
  'Unassign all associated target groups from the user for a policy.'
  user_id: int
  "The user's id to be assigned to the policy."


class UpdatePolicyMessage(TypedDict):
  """Update policy message."""

  description: NotRequired[str]
  '[single-line only]\n\nOptional description for the policy.'
  name: NotRequired[str]
  '[single-line only]\n\nA human-readable display name for the policy.'
  permission_sets: NotRequired[
    list[
      Literal[
        'agent_settings_write',
        'agents_admins_manage_agents_settings_write',
        'agents_admins_skill_level_write',
        'auto_call_recording_and_transcription_settings_write',
        'business_hours_write',
        'call_blocking_spam_prevention_settings_write',
        'call_dispositions_settings_write',
        'call_routing_hours_settings_write',
        'cc_call_settings_write',
        'chrome_extension_compliance_settings_write',
        'csat_surveys_write',
        'dashboard_and_alerts_write',
        'dialpad_ai_settings_write',
        'holiday_hours_settings_write',
        'integrations_settings_write',
        'name_language_description_settings_write',
        'number_settings_write',
        'supervisor_settings_write',
      ]
    ]
  ]
  'List of permission associated with this policy.'
  state: NotRequired[Literal['active']]
  'Restore a deleted policy.'
  user_id: NotRequired[int]
  'user id updating this policy. Must be a company admin'
