from .resource import DialpadResource

class BlockedNumberResource(DialpadResource):
  """BlockedNumberResource implements python bindings for the Dialpad API's blocked-number
  endpoints.
  
  See https://developers.dialpad.com/reference#blockednumbers for additional documentation.
  """
  _resource_path = ['blockednumbers']

  def list(self, limit=25, **kwargs):
    """List all numbers that have been flagged as "blocked" via the API.

    Args:
      limit (int, optional): The number of numbers to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#blockednumberapi_listnumbers
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def block_numbers(self, numbers):
    """Blocks inbound calls from the specified numbers.

    Args:
      numbers (list<str>, required): A list of e164-formatted numbers to block.

    See Also:
      https://developers.dialpad.com/reference#blockednumberapi_addnumbers
    """
    return self.request(['add'], method='POST', data={'numbers': numbers})

  def unblock_numbers(self, numbers):
    """Unblocks inbound calls from the specified numbers.

    Args:
      numbers (list<str>, required): A list of e164-formatted numbers to unblock.

    See Also:
      https://developers.dialpad.com/reference#blockednumberapi_removenumbers
    """
    return self.request(['remove'], method='POST', data={'numbers': numbers})

  def get(self, number):
    """Gets a number object, provided it has been blocked by the API.
    
    Note:
      This API call will 404 if the number is not blocked, and return {"number": <number>} if the
      number is blocked.

    Args:
      number (str, required): An e164-formatted number.

    See Also:
      https://developers.dialpad.com/reference#blockednumberapi_getnumber
    """
    return self.request([number], method='GET')
