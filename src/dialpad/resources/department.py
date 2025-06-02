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

  def add_operator(self, department_id, operator_id, operator_type, role='operator'):
    """Adds the specified user as an operator of the specified department.

    Args:
      department_id (int, required): The ID of the department.
      operator_id (int, required): The ID of the operator to add.
      operator_type (str, required): Type of the operator to add ('user' or 'room').
      role (str, optional): The role of the new operator ('operator' or 'admin').
                            Default 'operator'

    See Also:
      https://developers.dialpad.com/reference#departmentapi_addoperator
    """
    return self.request([department_id, 'operators'], method='POST', data={
      'operator_id': operator_id,
      'operator_type': operator_type,
      'role': role,
    })

  def remove_operator(self, department_id, operator_id, operator_type):
    """Removes the specified user from the specified department.

    Args:
      department_id (int, required): The ID of the department.
      operator_id (int, required): The ID of the operator to remove.
      operator_type (str, required): Type of the operator to remove ('user' or 'room').

    See Also:
      https://developers.dialpad.com/reference#departmentapi_removeoperator
    """
    return self.request([department_id, 'operators'], method='DELETE', data={
      'operator_id': operator_id,
      'operator_type': operator_type,
    })
