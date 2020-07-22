from .resource import DialpadResource

class UserDeviceResource(DialpadResource):
  """UserDeviceResource implements python bindings for the Dialpad API's userdevice endpoints.
  See https://developers.dialpad.com/reference#userdevices for additional documentation.
  """
  _resource_path = ['userdevices']

  def get(self, device_id):
    """Gets a user device by ID.

    Args:
      device_id (str, required): The ID of the device.

    See Also:
      https://developers.dialpad.com/reference#userdeviceapi_getdevice
    """
    return self.request([device_id])

  def list(self, user_id, limit=25, **kwargs):
    """Lists the devices for a specific user.

    Args:
      user_id (int, required): The ID of the user.
      limit (int, optional): the number of devices to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#userdeviceapi_listuserdevices
    """
    return self.request(data=dict(user_id=user_id, limit=limit, **kwargs))
