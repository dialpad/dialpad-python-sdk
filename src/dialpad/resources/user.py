from .resource import DialpadResource

class UserResource(DialpadResource):
  """UserResource implements python bindings for the Dialpad API's user endpoints.
  See https://developers.dialpad.com/reference#users for additional documentation.
  """
  _resource_path = ['users']

  def list(self, limit=25, **kwargs):
    """Lists users in the company.

    Args:
      email (str, optional): Limits results to users with a matching email address.
      state (str, optional): Limits results to users in the specified state (one of "active",
                             "canceled", "suspended", "pending", "deleted", "all)
      limit (int, optional): The number of users to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#userapi_listusers
    """
    return self.request(data=dict(limit=limit, **kwargs))

  def create(self, email, office_id, **kwargs):
    """Creates a new user.

    Args:
      email (str, required): The user's email address.
      office_id (int, required): The ID of the office that the user should belong to.
      first_name (str, optional): The first name of the user.
      last_name (str, optional): The last name of the user.
      license (str, optional): The license that the user should be created with. (One of "talk",
                               "agents", "lite_support_agents", "lite_lines")

    See Also:
      https://developers.dialpad.com/reference#userapi_createuser
    """
    return self.request(method='POST', data=dict(email=email, office_id=office_id, **kwargs))

  def delete(self, user_id):
    """Deletes a user.

    Args:
      user_id (int, required): The ID of the user to delete.

    See Also:
      https://developers.dialpad.com/reference#userapi_deleteuser
    """
    return self.request([user_id], method='DELETE')

  def get(self, user_id):
    """Gets a user by ID.

    Args:
      user_id (int, required): The ID of the user.

    See Also:
      https://developers.dialpad.com/reference#userapi_getuser
    """
    return self.request([user_id])

  def update(self, user_id, **kwargs):
    """Updates a user by ID.

    Note:
      The "phone_numbers" argument can be used to re-order or unassign numbers, but it cannot be
      used to assign new numbers. To assign new numbers to a user, please use the number assignment
      API instead.

    Args:
      user_id (int, required): The ID of the user.
      admin_office_ids (list<str>, optional): The office IDs that this user should be an admin of.
      emails (list<str>, optional): The email addresses that should be assoiciated with this user.
      extension (str, optional): The extension that this user can be reached at.
      first_name (str, optional): The first name of the user.
      last_name (str, optional): The last name of the user.
      forwarding_numbers (list<str>, optional): The e164-formatted numbers that should also ring
                                                when the user receives a Dialpad call.
      is_super_admin (bool, optional): Whether this user should be a company-level admin.
      job_title (str, optional): The user's job title.
      license (str, optional): The user's license type. Changing this affects billing for the user.
      office_id (int, optional): The ID of office to which this user should belong.
      phone_numbers (list<str>, optional): The e164-formatted numbers that should be assigned to
                                           this user.
      state (str, optional): The state of the user (One of "suspended", "active")

    See Also:
      https://developers.dialpad.com/reference#userapi_updateuser
    """
    return self.request([user_id], method='PATCH', data=kwargs)

  def toggle_call_recording(self, user_id, **kwargs):
    """Turn call recording on or off for a user's active call.

    Args:
      user_id (int, required): The ID of the user.
      is_recording (bool, optional): Whether recording should be turned on.
      play_message (bool, optional): Whether a message should be played to the user to notify them
                                     that they are now being (or no longer being) recorded.
      recording_type (str, optional): One of "user", "group", or "all". If set to "user", then only
                                      the user's individual calls will be recorded. If set to
                                      "group", then only calls in which the user is acting as an
                                      operator will be recorded. If set to "all", then all of the
                                      user's calls will be recorded.

    See Also:
      https://developers.dialpad.com/reference#callapi_updateactivecall
    """
    return self.request([user_id, 'activecall'], method='PATCH', data=kwargs)

  def assign_number(self, user_id, **kwargs):
    """Assigns a new number to the user.

    Args:
      user_id (int, required): The ID of the user to which the number should be assigned.
      number (str, optional): An e164 number that has already been allocated to the company's
                              reserved number pool that should be re-assigned to this user.
      area_code (str, optional): The area code to use to filter the set of available numbers to be
                                 assigned to this user.

    See Also:
      https://developers.dialpad.com/reference#numberapi_assignnumbertouser
    """
    return self.request([user_id, 'assign_number'], method='POST', data=kwargs)

  def initiate_call(self, user_id, phone_number, **kwargs):
    """Causes a user's native Dialpad application to initiate an outbound call.

    Args:
      user_id (int, required): The ID of the user.
      phone_number (str, required): The e164-formatted number to call.
      custom_data (str, optional): free-form extra data to associate with the call.
      group_id (str, optional): The ID of a group that will be used to initiate the call.
      group_type (str, optional): The type of a group that will be used to initiate the call.
      outbound_caller_id (str, optional): The e164-formatted number shown to the call recipient
                                  (or "blocked"). If set to "blocked", the recipient will receive a
                                  call from "unknown caller".

    See Also:
      https://developers.dialpad.com/reference#callapi_initiatecall
    """
    data = {
      'phone_number': phone_number
    }
    for k in ['group_id', 'group_type', 'outbound_caller_id', 'custom_data']:
      if k in kwargs:
        data[k] = kwargs.pop(k)
    assert not kwargs
    return self.request([user_id, 'initiate_call'], method='POST', data=data)

  def unassign_number(self, user_id, number):
    """Unassigns the specified number from the specified user.

    Args:
      user_id (int, required): The ID of the user.
      number (str, required): The e164-formatted number that should be unassigned from the user.

    See Also:
      https://developers.dialpad.com/reference#numberapi_unassignnumberfromuser
    """
    return self.request([user_id, 'unassign_number'], method='POST', data={'number': number})

  def get_deskphones(self, user_id):
    """Lists the desk phones that are associated with a user.

    Args:
      user_id (int, required): The ID of the user.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_listuserdeskphones
    """
    return self.request([user_id, 'deskphones'], method='GET')

  def create_deskphone(self, user_id, mac_address, name, phone_type):
    """Creates a desk phone belonging to the specified user.

    Args:
      user_id (int, required): The ID of the user.
      mac_address (str, required): MAC address of the desk phone.
      name (str, required): A human-readable name for the desk phone.
      phone_type (str, required): Type (vendor) of the desk phone. One of "obi", "polycom", "sip",
                                  "mini", "audiocodes", "yealink". Use "sip" for generic types.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_createuserdeskphone
    """
    return self.request([user_id, 'deskphones'], method='POST', data={
      'mac_address': mac_address,
      'name': name,
      'type': phone_type,
    })

  def delete_deskphone(self, user_id, deskphone_id):
    """Deletes the specified desk phone.

    Args:
      user_id (int, required): The ID of the user.
      deskphone_id (str, required): The ID of the desk phone.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_deleteuserdeskphone
    """
    return self.request([user_id, 'deskphones', deskphone_id], method='DELETE')

  def get_deskphone(self, user_id, deskphone_id):
    """Gets the specified desk phone.

    Args:
      user_id (int, required): The ID of the user.
      deskphone_id (str, required): The ID of the desk phone.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_getuserdeskphone
    """
    return self.request([user_id, 'deskphones', deskphone_id], method='GET')

  def get_personas(self, user_id):
    """Lists the calling personas that are associated with a user.

    Args:
      user_id (int, required): The ID of the user.

    See Also:
      https://developers.dialpad.com/reference#users
    """
    return self.request([user_id, 'personas'], method='GET')

  def toggle_do_not_disturb(self, user_id, do_not_disturb):
    """Toggle DND status on or off for the given user.

    Args:
      user_id (int, required): The ID of the user.
      do_not_disturb (bool, required): A boolean indicating whether to enable or disable the
                                       "do not disturb" setting.

    See Also:
      https://developers.dialpad.com/reference/userapi_togglednd
    """
    return self.request([user_id, 'togglednd'], method='PATCH',
                         data={'do_not_disturb': do_not_disturb})

  def search(self, query, **kwargs):
    """User -- Search

    Searches for users matching a specific criteria. It matches phone numbers, emails, or name.
    Optionally, it accepts filters to reduce the amount of final results.

    - The `cursor` value is provided in the API response, and can be passed as a parameter to
    retrieve subsequent pages of results.

    Args:
      query (str, required): A string that will be matched against user information. For phone
                                numbers in e164 format, it is recommended to URL-encode the model
                                term.
      cursor (str, optional): A token used to return the next page of a previous request. Use the
                              cursor provided in the previous response.
      filter (str, optional): If provided, query will be performed against a smaller set of data.
                              Format for providing filters is in the form of an array of key=value
                              pairs. (i.e. filter=[key=value])

    See Also:
      https://developers.dialpad.com/reference/searchusers
    """
    return self.request(['search'], method='GET', data=dict(query=query, **kwargs))
