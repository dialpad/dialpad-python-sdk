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

  def add_operator(self, call_center_id, user_id, **kwargs):
    """Adds the specified user as an operator of the specified call center.

    Args:
      call_center_id (int, required): The ID of the call center.
      user_id (int, required): The ID of the user to add as an operator.
      skill_level (int, optional): Skill level of the operator. Integer value in range 1 - 100.
                                   Default 100
      role (str, optional): The role of the new operator ('operator', 'supervisor', or 'admin').
                            Default 'operator'
      license_type (str, optional): The type of license to assign to the new operator if a license
                                    is required ('agents', or 'lite_support_agents').
                                    Default 'agents'
      keep_paid_numbers (bool, optional): If the operator is currently on a license that provides
                                          paid numbers and `license_type` is set to
                                          `lite_support_agents`, this option will determine if the
                                          operator keeps those numbers. Set to False for the
                                          numbers to be removed.
                                          Default True

    See Also:
      https://developers.dialpad.com/reference#callcenterapi_addoperator
    """
    kwargs['user_id'] = user_id
    return self.request([call_center_id, 'operators'], method='POST', data=kwargs)

  def remove_operator(self, call_center_id, user_id):
    """Removes the specified user from the specified call center.

    Args:
      call_center_id (int, required): The ID of the call center.
      user_id (int, required): The ID of the user to remove.

    See Also:
      https://developers.dialpad.com/reference#callcenterapi_removeoperator
    """
    return self.request([call_center_id, 'operators'], method='DELETE', data={'user_id': user_id})
