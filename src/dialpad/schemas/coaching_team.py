from typing import Literal

from typing_extensions import NotRequired, TypedDict


class CoachingTeamProto(TypedDict):
  """Coaching team."""

  allow_trainee_eavesdrop: NotRequired[bool]
  'The boolean to tell if trainees are allowed to eavesdrop.'
  company_id: NotRequired[int]
  "The company's id."
  country: NotRequired[str]
  'The country in which the coaching team is situated.'
  id: NotRequired[int]
  'Id of the coaching team.'
  name: NotRequired[str]
  '[single-line only]\n\nName of the coaching team.'
  office_id: NotRequired[int]
  "The office's id."
  phone_numbers: NotRequired[list[str]]
  'The phone number(s) assigned to this coaching team.'
  ring_seconds: NotRequired[int]
  'The number of seconds to ring the main line before going to voicemail.\n\n(or an other-wise-specified no_operators_action).'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The enablement state of the team.'
  team_description: NotRequired[str]
  'Description of the coaching team.'


class CoachingTeamCollection(TypedDict):
  """Collection of coaching team."""

  cursor: NotRequired[str]
  'A token used to return the next page of results.'
  items: NotRequired[list[CoachingTeamProto]]
  'A list of coaching teams.'


class CoachingTeamMemberProto(TypedDict):
  """Coaching team member."""

  admin_office_ids: NotRequired[list[int]]
  'The list of ids of offices where the user is an admin.'
  company_id: NotRequired[int]
  "The id of user's company."
  country: NotRequired[str]
  'Country of the user.'
  date_active: NotRequired[str]
  'The date when the user is activated.'
  date_added: NotRequired[str]
  'The date when the user is added.'
  date_first_login: NotRequired[str]
  'The date when the user is logged in first time.'
  do_not_disturb: NotRequired[bool]
  'Boolean to tell if the user is on DND.'
  emails: NotRequired[list[str]]
  'Emails of the user.'
  extension: NotRequired[str]
  'Extension of the user.'
  first_name: NotRequired[str]
  '[single-line only]\n\nFirst name of the user.'
  forwarding_numbers: NotRequired[list[str]]
  'The list of forwarding numbers set for the user.'
  id: int
  'Unique id of the user.'
  image_url: NotRequired[str]
  "Link to the user's profile image."
  is_admin: NotRequired[bool]
  'Boolean to tell if the user is admin.'
  is_available: NotRequired[bool]
  'Boolean to tell if the user is available.'
  is_on_duty: NotRequired[bool]
  'Boolean to tell if the user is on duty.'
  is_online: NotRequired[bool]
  'Boolean to tell if the user is online.'
  is_super_admin: NotRequired[bool]
  'Boolean to tell if the user is super admin.'
  job_title: NotRequired[str]
  '[single-line only]\n\nJob title of the user.'
  language: NotRequired[str]
  'Language of the user.'
  last_name: NotRequired[str]
  '[single-line only]\n\nLast name of the User.'
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
  'License of the user.'
  location: NotRequired[str]
  '[single-line only]\n\nThe self-reported location of the user.'
  muted: NotRequired[bool]
  'Boolean to tell if the user is muted.'
  office_id: NotRequired[int]
  "Id of the user's office."
  phone_numbers: NotRequired[list[str]]
  'The list of phone numbers assigned to the user.'
  role: Literal['coach', 'trainee']
  'The role of the user within the coaching team.'
  state: NotRequired[Literal['active', 'cancelled', 'deleted', 'pending', 'suspended']]
  'The enablement state of the user.'
  status_message: NotRequired[str]
  '[single-line only]\n\nStatus message set by the user.'
  timezone: NotRequired[str]
  'Timezone of the user.'


class CoachingTeamMemberCollection(TypedDict):
  """Collection of coaching team members."""

  cursor: NotRequired[str]
  'A token used to return the next page of results.'
  items: NotRequired[list[CoachingTeamMemberProto]]
  'A list of team members.'


class CoachingTeamMemberMessage(TypedDict):
  """Coaching team membership."""

  member_id: str
  'The id of the user added to the coaching team.'
  role: Literal['coach', 'trainee']
  'The role of the user added.'
