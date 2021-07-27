from .resource import DialpadResource

class NumberResource(DialpadResource):
  """NumberResource implements python bindings for the Dialpad API's number endpoints.
  
  See https://developers.dialpad.com/reference#numbers for additional documentation.
  """
  _resource_path = ['numbers']

  def list(self, limit=25, **kwargs):
    """List all phone numbers in the company.

    Args:
      limit (int, optional): The number of numbers to fetch per request
      status (str, optional): If provided, the results will only contain numbers with the specified
                              status. Must be one of: "available", "pending", "office",
                              "department", "call_center", "user", "room", "porting", "call_router",
                              or "dynamic_caller"

    See Also:
      https://developers.dialpad.com/reference#numberapi_listnumbers
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def get(self, number):
    """Gets a specific number object.

    Args:
      number (str, required): An e164-formatted number.

    See Also:
      https://developers.dialpad.com/reference#numberapi_getnumber
    """
    return self.request([number], method='GET')

  def unassign(self, number, release=False):
    """Unassigns the specified number.

    Args:
      number (str, required): An e164-formatted number.
      release (bool, optional): If the "release" flag is omitted or set to False, the number will
                                be returned to the company pool (i.e. your company will still own
                                the number, but it will no longer be assigned to any targets).
                                If the "release" flag is set, then the number will be beamed back
                                to the Dialpad mothership.

    See Also:
      https://developers.dialpad.com/reference#numberapi_unassignnumber
    """
    return self.request([number], method='DELETE', data={'release': release})

  def assign(self, number, target_id, target_type, primary=True):
    """Assigns the specified number to the specified target.

    Args:
      number (str, required): The e164-formatted number that should be assigned.
      target_id (int, required): The ID of the target to which the number should be assigned.
      target_type (str, required): The type corresponding to the provided target ID.
      primary (bool, optional): (Defaults to True) If the "primary" flag is set, then the assigned
                                number will become the primary number of the specified target.

    See Also:
      https://developers.dialpad.com/reference#numberapi_assignnumber
    """
    return self.request(['assign'], method='POST', data={
        'number': number,
        'target_id': target_id,
        'target_type': target_type,
        'primary': primary
    })

  def format(self, number, country_code=None):
    """Converts local number to E.164 or E.164 to local format.

    Args:
      number (str, required): The phone number in local or E.164 format.
      country_code (str, optional): Country code in ISO 3166-1 alpha-2 format such as "US".
                                    Required when sending a local formatted phone number.

    See Also:
      https://developers.dialpad.com/reference#formatapi_formatnumber
    """
    return self.request(['format'], method='POST', data={
        'number': number,
        'country_code': country_code
    })
