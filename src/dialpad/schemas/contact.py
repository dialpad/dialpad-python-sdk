from typing import Literal

from typing_extensions import NotRequired, TypedDict


class ContactProto(TypedDict):
  """Contact."""

  company_name: NotRequired[str]
  '[single-line only]\n\nThe name of the company that this contact is employed by.'
  display_name: NotRequired[str]
  '[single-line only]\n\nThe formatted name that will be displayed for this contact.'
  emails: NotRequired[list[str]]
  'The email addresses associated with this contact.'
  extension: NotRequired[str]
  "The contact's extension number."
  first_name: NotRequired[str]
  '[single-line only]\n\nThe given name of the contact.'
  id: NotRequired[str]
  'The ID of the contact.'
  job_title: NotRequired[str]
  '[single-line only]\n\nThe job title of this contact.'
  last_name: NotRequired[str]
  '[single-line only]\n\nThe family name of the contact.'
  owner_id: NotRequired[str]
  'The ID of the entity that owns this contact.'
  phones: NotRequired[list[str]]
  'The phone numbers associated with this contact.'
  primary_email: NotRequired[str]
  'The email address to display in a context where only one email can be shown.'
  primary_phone: NotRequired[str]
  'The primary phone number to be used when calling this contact.'
  trunk_group: NotRequired[str]
  '[Deprecated]'
  type: NotRequired[Literal['local', 'shared']]
  'Either shared or local.'
  urls: NotRequired[list[str]]
  'A list of websites associated with or belonging to this contact.'


class ContactCollection(TypedDict):
  """Collection of contacts."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[ContactProto]]
  'A list of contact objects.'


class CreateContactMessage(TypedDict):
  """TypedDict representation of the CreateContactMessage schema."""

  company_name: NotRequired[str]
  "[single-line only]\n\nThe contact's company name."
  emails: NotRequired[list[str]]
  "The contact's emails.\n\nThe first email in the list is the contact's primary email."
  extension: NotRequired[str]
  "The contact's extension number."
  first_name: str
  "[single-line only]\n\nThe contact's first name."
  job_title: NotRequired[str]
  "[single-line only]\n\nThe contact's job title."
  last_name: str
  "[single-line only]\n\nThe contact's last name."
  owner_id: NotRequired[str]
  'The id of the user who will own this contact.\n\nIf provided, a local contact will be created for this user. Otherwise, the contact will be created as a shared contact in your company.'
  phones: NotRequired[list[str]]
  "The contact's phone numbers.\n\nThe phone number must be in e164 format. The first number in the list is the contact's primary phone."
  trunk_group: NotRequired[str]
  '[Deprecated]'
  urls: NotRequired[list[str]]
  'A list of websites associated with or belonging to this contact.'


class CreateContactMessageWithUid(TypedDict):
  """TypedDict representation of the CreateContactMessageWithUid schema."""

  company_name: NotRequired[str]
  "[single-line only]\n\nThe contact's company name."
  emails: NotRequired[list[str]]
  "The contact's emails.\n\nThe first email in the list is the contact's primary email."
  extension: NotRequired[str]
  "The contact's extension number."
  first_name: str
  "[single-line only]\n\nThe contact's first name."
  job_title: NotRequired[str]
  "[single-line only]\n\nThe contact's job title."
  last_name: str
  "[single-line only]\n\nThe contact's last name."
  phones: NotRequired[list[str]]
  "The contact's phone numbers.\n\nThe phone number must be in e164 format. The first number in the list is the contact's primary phone."
  trunk_group: NotRequired[str]
  '[Deprecated]'
  uid: str
  "The unique id to be included as part of the contact's generated id."
  urls: NotRequired[list[str]]
  'A list of websites associated with or belonging to this contact.'


class UpdateContactMessage(TypedDict):
  """TypedDict representation of the UpdateContactMessage schema."""

  company_name: NotRequired[str]
  "[single-line only]\n\nThe contact's company name."
  emails: NotRequired[list[str]]
  "The contact's emails.\n\nThe first email in the list is the contact's primary email."
  extension: NotRequired[str]
  "The contact's extension number."
  first_name: NotRequired[str]
  "[single-line only]\n\nThe contact's first name."
  job_title: NotRequired[str]
  "[single-line only]\n\nThe contact's job title."
  last_name: NotRequired[str]
  "[single-line only]\n\nThe contact's last name."
  phones: NotRequired[list[str]]
  "The contact's phone numbers.\n\nThe phone number must be in e164 format. The first number in the list is the contact's primary phone."
  trunk_group: NotRequired[str]
  '[Deprecated]'
  urls: NotRequired[list[str]]
  'A list of websites associated with or belonging to this contact.'
