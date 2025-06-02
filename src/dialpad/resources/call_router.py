from .resource import DialpadResource

class CallRouterResource(DialpadResource):
  """CallRouterResource implements python bindings for the Dialpad API's call router endpoints.
  
  See https://developers.dialpad.com/reference#callrouters for additional documentation.
  """
  _resource_path = ['callrouters']

  def list(self, office_id, **kwargs):
    """Initiates an oubound call to the specified phone number on behalf of the specified user.

    Args:
      office_id (int, required): The ID of the office to which the routers belong.
      limit (int, optional): The number of routers to fetch per request.

    See Also:
      https://developers.dialpad.com/reference#callrouterapi_listcallrouters
    """
    return self.request(method='GET', data=dict(office_id=office_id, **kwargs))

  def create(self, name, default_target_id, default_target_type, office_id, routing_url, **kwargs):
    """Creates a new API-based call router.

    Args:
      name (str, required):  human-readable display name for the router.
      default_target_id (int, required): The ID of the target that should be used as a fallback
                                         destination for calls if the call router is disabled.
      default_target_type (str, required): The entity type of the default target.
      office_id (int, required): The ID of the office to which the router should belong.
      routing_url (str, required): The URL that should be used to drive call routing decisions.
      secret (str, optional): The call router's signature secret. This is a plain text string that
                              you should generate with a minimum length of 32 characters.
      enabled (bool, optional): If set to False, the call router will skip the routing url and
                                instead forward calls straight to the default target.

    See Also:
      https://developers.dialpad.com/reference#callrouterapi_createcallrouter
    """
    return self.request(method='POST', data=dict(
      name=name,
      default_target_id=default_target_id,
      default_target_type=default_target_type,
      office_id=office_id,
      routing_url=routing_url,
      **kwargs)
   )

  def delete(self, router_id):
    """Deletes the API call router with the given ID.

    Args:
      router_id (str, required): The ID of the router to delete.

    See Also:
      https://developers.dialpad.com/reference#callrouterapi_deletecallrouter
    """
    return self.request([router_id], method='DELETE')

  def get(self, router_id):
    """Fetches the API call router with the given ID.

    Args:
      router_id (str, required): The ID of the router to fetch.

    See Also:
      https://developers.dialpad.com/reference#callrouterapi_getcallrouter
    """
    return self.request([router_id], method='GET')

  def patch(self, router_id, **kwargs):
    """Updates the API call router with the given ID.

    Args:
      router_id (str, required): The ID of the router to update.
      name (str, required): human-readable display name for the router.
      default_target_id (int, required): The ID of the target that should be used as a fallback
                                         destination for calls if the call router is disabled.
      default_target_type (str, required): The entity type of the default target.
      office_id (int, required): The ID of the office to which the router should belong.
      routing_url (str, required): The URL that should be used to drive call routing decisions.
      secret (str, optional): The call router's signature secret. This is a plain text string that
                              you should generate with a minimum length of 32 characters.
      enabled (bool, optional): If set to False, the call router will skip the routing url and
                                instead forward calls straight to the default target
      reset_error_count (bool, optional): Sets the auto-disablement routing error count back to
                                          zero. (See API docs for more details)

    See Also:
      https://developers.dialpad.com/reference#callrouterapi_updatecallrouter
    """
    return self.request([router_id], method='PATCH', data=kwargs)

  def assign_number(self, router_id, **kwargs):
    """Assigns a number to the call router.

    Args:
      router_id (str, required): The ID of the router to assign the number.
      area_code (str, optional): An area code to attempt to use if a reserved pool number is not
                                 provided. If no area code is provided, the office's area code will
                                 be used.
      number (str, optional): A phone number from the reserved pool to attempt to assign.

    See Also:
      https://developers.dialpad.com/reference#numberapi_assignnumbertocallrouter
    """
    return self.request([router_id, 'assign_number'], method='POST', data=kwargs)

