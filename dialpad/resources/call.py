from .resource import DialpadResource

class CallResource(DialpadResource):
  """CallResource implements python bindings for the Dialpad API's call endpoints.
  
  See https://developers.dialpad.com/reference#call for additional documentation.
  """
  _resource_path = ['call']

  def initiate_call(self, phone_number, user_id, **kwargs):
    """Initiates an oubound call to the specified phone number on behalf of the specified user.

    Note:
      This API will initiate the call by ringing the user's devices as well as ringing the specified
      number. When the user answers on their device, they will be connected with the call that is
      ringing the specified number.

      Optionally, group_type and group_id can be specified to cause the call to be routed through
      the specified group. This would be equivelant to the User initiating the call by selecting the
      specified group in the "New Call As" dropdown in the native app, or calling a contact that
      belongs to that group via the native app.

      In particular, the call will show up in that group's section of the app, and the external
      party will receive a call from the primary number of the specified group.

      Additionally, a specific device_id can be specified to cause that specific user-device to
      ring, rather than all of the user's devices.

    Args:
      phone_number (str, required): The e164-formatted number that should be called.
      user_id (int, required): The ID of the user that should be taking the call.
      group_id (int, optional): The ID of the call center, department, or office that should be used
                                to initiate the call.
      group_type (str, optional): One of "office", "department", or "callcenter", corresponding to
                                  the type of ID passed into group_type.
      device_id (str, optional): The ID of the specific user device that should ring.
      custom_data (str, optional): Free-form extra data to associate with the call.

    See Also:
      https://developers.dialpad.com/reference#callapi_call
    """
    return self.request(method='POST', data=dict(phone_number=phone_number, user_id=user_id,
                                                 **kwargs))

  def get_info(self, call_id):
    """Gets call status and other information.

    Args:
      call_id (int, required): The ID of the call.

    See Also:
      https://developers.dialpad.com/reference/callapi_getcallinfo
    """
    return self.request([call_id], method='GET')
