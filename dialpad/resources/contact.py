from .resource import DialpadResource

class ContactResource(DialpadResource):
  """ContactResource implements python bindings for the Dialpad API's contact endpoints.
  
  See https://developers.dialpad.com/reference#contacts for additional documentation.
  """
  _resource_path = ['contacts']

  def list(self, limit=25, **kwargs):
    """Lists contacts in the company.

    Args:
      limit (int, optional): The number of contacts to fetch per request.
      owner_id (int, optional): A specific user who's contacts should be listed.

    See Also:
      https://developers.dialpad.com/reference#contactapi_listcontacts
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def create(self, first_name, last_name, **kwargs):
    """Creates a new contact.

    Args:
      first_name (str, required): The contact's first name.
      last_name (str, required): The contact's family name.
      company_name (str, optional): The name of the contact's company.
      emails (list<str>, optional): A list of email addresses associated with the contact.
      extension (str, optional): The contact's extension number.
      job_title (str, optional): The contact's job title.
      owner_id (str, optional): The ID of the user who should own this contact. If no owner_id is
                                specified, then a company-level shared contact will be created.
      phones (list<str>, optional): A list of e164 numbers that belong to this contact.
      trunk_group (str, optional): The contact's trunk group.
      urls (list<str>, optional): A list of urls that pertain to this contact.

    See Also:
      https://developers.dialpad.com/reference#contactapi_createcontact
    """
    return self.request(method='POST', data=dict(first_name=first_name, last_name=last_name,
                                                 **kwargs))

  def create_with_uid(self, first_name, last_name, uid, **kwargs):
    """Creates a new contact with a prescribed unique identifier.

    Args:
      first_name (str, required): The contact's first name.
      last_name (str, required): The contact's family name.
      uid (str, required): A unique identifier that should be included in the contact's ID.
      company_name (str, optional): The name of the contact's company.
      emails (list<str>, optional): A list of email addresses associated with the contact.
      extension (str, optional): The contact's extension number.
      job_title (str, optional): The contact's job title.
      phones (list<str>, optional): A list of e164 numbers that belong to this contact.
      trunk_group (str, optional): The contact's trunk group.
      urls (list<str>, optional): A list of urls that pertain to this contact.

    See Also:
      https://developers.dialpad.com/reference#contactapi_createcontactwithuid
    """
    return self.request(method='PUT', data=dict(first_name=first_name, last_name=last_name, uid=uid,
                                                **kwargs))

  def delete(self, contact_id):
    """Deletes the specified contact.

    Args:
      contact_id (str, required): The ID of the contact to delete.

    See Also:
      https://developers.dialpad.com/reference#contactapi_deletecontact
    """
    return self.request([contact_id], method='DELETE')

  def get(self, contact_id):
    """Gets a contact by ID.

    Args:
      contact_id (str, required): The ID of the contact.

    See Also:
      https://developers.dialpad.com/reference#contactapi_getcontact
    """
    return self.request([contact_id], method='GET')

  def patch(self, contact_id, **kwargs):
    """Updates an existing contact.

    Args:
      contact_id (str, required): The ID of the contact.
      first_name (str, optional): The contact's first name.
      last_name (str, optional): The contact's family name.
      company_name (str, optional): The name of the contact's company.
      emails (list<str>, optional): A list of email addresses associated with the contact.
      extension (str, optional): The contact's extension number.
      job_title (str, optional): The contact's job title.
      phones (list<str>, optional): A list of e164 numbers that belong to this contact.
      trunk_group (str, optional): The contact's trunk group.
      urls (list<str>, optional): A list of urls that pertain to this contact.

    See Also:
      https://developers.dialpad.com/reference#contactapi_updatecontact
    """
    return self.request([contact_id], method='PATCH', data=kwargs)
