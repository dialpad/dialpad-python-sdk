from .resource import DialpadResource

class DepartmentResource(DialpadResource):
  """DepartmentResource implements python bindings for the Dialpad API's department endpoints.
  See https://developers.dialpad.com/reference#departments for additional documentation.
  """

  _resource_path = ['departments']

  def get(self, department_id):
    """Gets a department by ID.

    Args:
      department_id (int, required): The ID of the department to retrieve.

    See Also:
      https://developers.dialpad.com/reference#departmentapi_getdepartment
    """
    return self.request([department_id], method='GET')

  def get_operators(self, department_id):
    """Gets the list of users who are operators for the specified department.

    Args:
      department_id (int, required): The ID of the department.

    See Also:
      https://developers.dialpad.com/reference#departmentapi_listoperators
    """
    return self.request([department_id, 'operators'], method='GET')
