from .resource import DialpadResource

class CallRouterResource(DialpadResource):
  """CallRouterResource implements python bindings for the Dialpad API's call router endpoints.
  
  See https://developers.dialpad.com/reference#callrouters for additional documentation.
  """
  _resource_path = ['callrouters']

  def get(self, call_router_id):
    """Gets a specific call router.

    Args:
      call_router_id (int, required): The ID of the call router.

    See Also:
      TODO(Jake): Fill in after the endpoint goes live
    """
    return self.request([call_router_id])

  def list(self, limit=25, **kwargs):
    """Lists call routers

    Args:
      limit (int, optional): The number of call routers to fetch per request.
      office_id (int, optional): If provided, results will be filtered to include only those call
                                 routers that belong to the given office.

    See Also:
      TODO(Jake): Fill in after the endpoint goes live
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def post(self, **kwargs):
    """Creates a new call router.

    Args:
      name (str, required): A human-readable name to identify the call router.
      routing_url (str, required): A valid URL that will be hit at call-routing time for inbound
                                   calls to decide which Target the call should be routed to.
      office_id (int, required): The ID of the office that this router should belong to.
      default_target_id (int, required): The ID of the target that should receive calls for which
                                         the routing URL fails, times out, or responds incorrectly.
      default_target_type (str, required): The type of the default target.
      enabled (bool, optional): If set to False, the router will act as a pass-through to the
                                default target, without hitting the routing URL.
      secret (str, optional): If provided, this secret will be used to sign the payloads that are
                              sent to the routing URL. Payloads will be sent in the form of a JWT
                              if a secret is specified, or as a raw JSON payload if no secret is
                              specified.

    See Also:
      TODO(Jake): Fill in after the endpoint goes live
    """
    return self.request(method='POST', data=kwargs)

  def patch(self, call_router_id, **kwargs):
    """Updates an existing call router.

    Args:
      call_router_id (int, required): The ID of the call router that should be modified.
      name (str, optional): A human-readable name to identify the call router.
      routing_url (str, optional): A valid URL that will be hit at call-routing time for inbound
                                   calls to decide which Target the call should be routed to.
      office_id (int, optional): The ID of the office that this router should belong to.
      default_target_id (int, optional): The ID of the target that should receive calls for which
                                         the routing URL fails, times out, or responds incorrectly.
      default_target_type (str, optional): The type of the default target.
      enabled (bool, optional): If set to False, the router will act as a pass-through to the
                                default target, without hitting the routing URL.
      secret (str, optional): If provided, this secret will be used to sign the payloads that are
                              sent to the routing URL. Payloads will be sent in the form of a JWT
                              if a secret is specified, or as a raw JSON payload if no secret is
                              specified.

    See Also:
      TODO(Jake): Fill in after the endpoint goes live
    """
    return self.request([call_router_id], method='PATCH', data=kwargs)

  def delete(self, call_router_id):
    """Deletes an existing call router.

    Args:
      call_router_id (int, required): The ID of the call router that should be deleted.

    See Also:
      TODO(Jake): Fill in after the endpoint goes live
    """
    return self.request([call_router_id], method='DELETE')

  def assign_number(self, call_router_id, **kwargs):
    """Provisions a phone number for the call router.

    To route a call, call routers must first *receive* a call. In order to receive a call, a call
    router must be given a phone number. Once a call router has a phone number, calls can either be
    forwarded to that number via the usual call routing mechanisms exposed via the Dialpad settings
    page, or called directly by dialing that number.

    Args:
      call_router_id (int, required): The ID of the call router that should receive calls to the
                                      provisioned number.
      number (str, optional): An e164 number that has already been allocated to the company's
                              reserved number pool that should be re-assigned to this call router.
      area_code (str, optional): The area code to use to filter the set of available numbers to be
                                 assigned to this call router. If no area code is explicitly
                                 provided, the area code of the call router's office will be used
                                 instead.

    See Also:
      TODO(Jake): Fill in after the endpoint goes live
    """
    return self.request([call_router_id, 'assign_number'], method='POST', data=kwargs)
