from .resource import DialpadResource

class OfficeResource(DialpadResource):
  """OfficeResource implements python bindings for the Dialpad API's office endpoints.
  See https://developers.dialpad.com/reference#offices for additional documentation.
  """

  _resource_path = ['offices']

  def list(self, limit=25, **kwargs):
    """Lists the company's offices.

    Args:
      limit (int, optional): the number of offices to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#officeapi_listoffices
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def get(self, office_id):
    """Gets an office by ID.

    Args:
      office_id (int, required): The ID of the office to retrieve.

    See Also:
      https://developers.dialpad.com/reference#officeapi_getoffice
    """
    return self.request([office_id], method='GET')

  def assign_number(self, office_id, **kwargs):
    """Assigns a phone number to the specified office

    Args:
      office_id (int, required): The ID of the office to which the number should be assigned.
      number (str, optional): An e164 number that has already been allocated to the company's
                              reserved number pool that should be re-assigned to this office.
      area_code (str, optional): The area code to use to filter the set of available numbers to be
                                 assigned to this office.

    See Also:
      https://developers.dialpad.com/reference#numberapi_assignnumbertooffice
    """
    return self.request([office_id, 'assign_number'], method='POST', data=kwargs)

  def get_operators(self, office_id):
    """Gets the list of users who are operators for the specified office.

    Args:
      office_id (int, required): The ID of the office.

    See Also:
      https://developers.dialpad.com/reference#officeapi_listoperators
    """
    return self.request([office_id, 'operators'], method='GET')

  def unassign_number(self, office_id, number):
    """Unassigns the specified number from the specified office.

    Args:
      office_id (int, required): The ID of the office.
      number (str, required): The e164-formatted number that should be unassigned from the office.

    See Also:
      https://developers.dialpad.com/reference#numberapi_unassignnumberfromoffice
    """
    return self.request([office_id, 'unassign_number'], method='POST', data={'number': number})

  def get_call_centers(self, office_id, limit=25, **kwargs):
    """Lists the call centers under the specified office.

    Args:
      office_id (int, required): The ID of the office.
      limit (int, optional): the number of call centers to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#callcenterapi_listcallcenters
    """
    return self.request([office_id, 'callcenters'], method='GET', data=dict(limit=limit, **kwargs))

  def get_departments(self, office_id, limit=25, **kwargs):
    """Lists the departments under the specified office.

    Args:
      office_id (int, required): The ID of the office.
      limit (int, optional): the number of departments to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#departmentapi_listdepartments
    """
    return self.request([office_id, 'departments'], method='GET', data=dict(limit=limit, **kwargs))

  def get_plan(self, office_id):
    """Gets the plan associated with the office.

    (i.e. a breakdown of the licenses that have been purchased for the specified office)

    Args:
      office_id (int, required): The ID of the office.

    See Also:
      https://developers.dialpad.com/reference#planapi_getplan
    """
    return self.request([office_id, 'plan'], method='GET')

  def update_licenses(self, office_id, fax_line_delta):
    """Updates the number of licenses in the specified office's plan.

    Note:
      Currently only supports modifying the number of fax line licenses.

    Args:
      office_id (int, required): The ID of the office.
      fax_line_delta (int, required): Number of fax lines to add. If a negative number is specified,
                                      then fax lines will be removed rather than added.

    See Also:
      https://developers.dialpad.com/reference#planapi_updatelicenses
    """
    return self.request([office_id, 'plan', 'updateLicenses'], method='POST', data={
        'fax_line_delta': fax_line_delta
    })
