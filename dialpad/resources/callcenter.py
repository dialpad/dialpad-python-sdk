from .resource import DialpadResource

class CallCenterResource(DialpadResource):
  """CallCenterResource implements python bindings for the Dialpad API's call center endpoints.
  See https://developers.dialpad.com/reference#callcenters for additional documentation.
  """

  _resource_path = ['callcenters']

  def get(self, call_center_id):
    """Gets a call center by ID.

    Args:
      call_center_id (int, required): The ID of the call center to retrieve.

    See Also:
      https://developers.dialpad.com/reference#callcenterapi_getcallcenter
    """
    return self.request([call_center_id], method='GET')

  def get_operators(self, call_center_id):
    """Gets the list of users who are operators for the specified call center.

    Args:
      call_center_id (int, required): The ID of the call center.

    See Also:
      https://developers.dialpad.com/reference#callcenterapi_listoperators
    """
    return self.request([call_center_id, 'operators'], method='GET')
