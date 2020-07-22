from .resource import DialpadResource

class RoomResource(DialpadResource):
  """RoomResource implements python bindings for the Dialpad API's room endpoints.
  See https://developers.dialpad.com/reference#rooms for additional documentation.
  """

  _resource_path = ['rooms']

  def list(self, limit=25, **kwargs):
    """Lists rooms in the company.

    Args:
      limit (int, optional): The number of rooms to fetch per request.
      office_id (int, optional): If specified, only rooms associated with that office will be
                                 returned.

    See Also:
      https://developers.dialpad.com/reference#roomapi_listrooms
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def create(self, name, office_id):
    """Creates a new room with the specified name within the specified office.

    Args:
      name (str, required): A human-readable name for the room.
      office_id (int, required): The ID of the office.

    See Also:
      https://developers.dialpad.com/reference#roomapi_createroom
    """
    return self.request(method='POST', data={'name': name, 'office_id': office_id})

  def generate_international_pin(self, customer_ref):
    """Creates a PIN to allow an international call to be made from a room phone.

    Args:
      customer_ref (str, required): An identifier to be printed in the usage summary. Typically used
                                    for identifying the person who requested the PIN

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_createinternationalpin
    """
    return self.request(['international_pin'], method='POST', data={'customer_ref': customer_ref})

  def delete(self, room_id):
    """Deletes a room by ID.

    Args:
      room_id (str, required): The ID of the room to be deleted.

    See Also:
      https://developers.dialpad.com/reference#roomapi_deleteroom
    """
    return self.request([room_id], method='DELETE')

  def get(self, room_id):
    """Gets a room by ID.

    Args:
      room_id (str, required): The ID of the room to be fetched.

    See Also:
      https://developers.dialpad.com/reference#roomapi_getroom
    """
    return self.request([room_id], method='GET')

  def update(self, room_id, **kwargs):
    """Updates the specified room.

    Args:
      room_id (str, required): The ID of the room to be updated.
      name (str, optional): A human-readable name for the room.
      phone_numbers (list<str>, optional): The list of e164-formatted phone numbers that should be
                                           associated with this room. New numbers will be assigned,
                                           and omitted numbers will be unassigned.

    See Also:
      https://developers.dialpad.com/reference#roomapi_updateroom
    """
    return self.request([room_id], method='PATCH', data=kwargs)

  def assign_number(self, room_id, **kwargs):
    """Assigns a phone number to the specified room

    Args:
      room_id (int, required): The ID of the room to which the number should be assigned.
      number (str, optional): An e164 number that has already been allocated to the company's
                              reserved number pool that should be re-assigned to this office.
      area_code (str, optional): The area code to use to filter the set of available numbers to be
                                 assigned to this office.

    See Also:
      https://developers.dialpad.com/reference#numberapi_assignnumbertoroom
    """
    return self.request([room_id, 'assign_number'], method='POST', data=kwargs)

  def unassign_number(self, room_id, number):
    """Unassigns the specified number from the specified room.

    Args:
      room_id (int, required): The ID of the room.
      number (str, required): The e164-formatted number that should be unassigned from the room.

    See Also:
      https://developers.dialpad.com/reference#numberapi_unassignnumberfromroom
    """
    return self.request([room_id, 'unassign_number'], method='POST', data={'number': number})

  def get_deskphones(self, room_id):
    """Lists the phones that are assigned to the specified room.

    Args:
      room_id (int, required): The ID of the room.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_listroomdeskphones
    """
    return self.request([room_id, 'deskphones'], method='GET')

  def create_deskphone(self, room_id, mac_address, name, phone_type):
    """Creates a desk phone belonging to the specified room.

    Args:
      room_id (int, required): The ID of the room.
      mac_address (str, required): MAC address of the desk phone.
      name (str, required): A human-readable name for the desk phone.
      phone_type (str, required): Type (vendor) of the desk phone. One of "obi", "polycom", "sip",
                                  "mini", "audiocodes", "yealink". Use "sip" for generic types.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_createroomdeskphone
    """
    return self.request([room_id, 'deskphones'], method='POST', data={
      'mac_address': mac_address,
      'name': name,
      'type': phone_type,
    })

  def delete_deskphone(self, room_id, deskphone_id):
    """Deletes the specified desk phone.

    Args:
      room_id (int, required): The ID of the room.
      deskphone_id (str, required): The ID of the desk phone.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_deleteroomdeskphone
    """
    return self.request([room_id, 'deskphones', deskphone_id], method='DELETE')

  def get_deskphone(self, room_id, deskphone_id):
    """Gets the specified desk phone.

    Args:
      room_id (int, required): The ID of the room.
      deskphone_id (str, required): The ID of the desk phone.

    See Also:
      https://developers.dialpad.com/reference#deskphoneapi_getroomdeskphone
    """
    return self.request([room_id, 'deskphones', deskphone_id], method='GET')
