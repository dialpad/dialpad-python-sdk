from .resource import DialpadResource

class EventSubscriptionResource(DialpadResource):
  """EventSubscriptionResource implements python bindings for the Dialpad API's event subscription
  endpoints.
  
  See https://developers.dialpad.com/reference#event for additional documentation.
  """
  _resource_path = ['event-subscriptions']

  def list_call_event_subscriptions(self, limit=25, **kwargs):
    """Lists call event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#calleventsubscriptionapi_listcalleventsubscriptions
    """
    return self.request(['call'], method='GET', data=dict(limit=limit, **kwargs))

  def get_call_event_subscription(self, subscription_id):
    """Gets a specific call event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#calleventsubscriptionapi_getcalleventsubscription
    """
    return self.request(['call', subscription_id], method='GET')

  def put_call_event_subscription(self, subscription_id, url, enabled=True, group_calls_only=False,
                                  **kwargs):
    """Update or create a call event subscription.

    The subscription_id is required. If the ID exists, then this call will update the subscription
    resource. If the ID does not exist, then it will create a new subscription with that ID.

    Args:
      subscription_id (str, required): The ID of the subscription
      url (str, required): The URL which should be called when the subscription fires
      secret (str, optional): A secret to use to encrypt subscription event payloads
      enabled (bool, optional): Whether or not the subscription should actually fire
      group_calls_only (bool, optional): Whether to limit the subscription to only fire if the call
                                         is a group call
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")
      call_states (list<str>, optional): The specific types of call events that should trigger the
                                         subscription (any of "preanswer", "calling", "ringing",
                                         "connected", "merged", "hold", "queued", "voicemail",
                                         "eavesdrop", "monitor", "barge", "hangup", "blocked",
                                         "admin", "parked", "takeover", "all", "postcall",
                                         "transcription", or "recording")

    See Also:
      https://developers.dialpad.com/reference#calleventsubscriptionapi_createorupdatecalleventsubscription
    """

    return self.request(['call', subscription_id], method='PUT',
                        data=dict(url=url, enabled=enabled, group_calls_only=group_calls_only,
                                  **kwargs))

  def delete_call_event_subscription(self, subscription_id):
    """Deletes a specific call event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#calleventsubscriptionapi_deletecalleventsubscription
    """
    return self.request(['call', subscription_id], method='DELETE')


  def list_sms_event_subscriptions(self, limit=25, **kwargs):
    """Lists sms event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#smseventsubscriptionapi_listsmseventsubscriptions
    """
    return self.request(['sms'], method='GET', data=dict(limit=limit, **kwargs))

  def get_sms_event_subscription(self, subscription_id):
    """Gets a specific sms event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#smseventsubscriptionapi_getsmseventsubscription
    """
    return self.request(['sms', subscription_id], method='GET')

  def put_sms_event_subscription(self, subscription_id, url, direction, enabled=True,
                                  **kwargs):
    """Update or create an sms event subscription.

    The subscription_id is required. If the ID exists, then this call will update the subscription
    resource. If the ID does not exist, then it will create a new subscription with that ID.

    Args:
      subscription_id (str, required): The ID of the subscription
      url (str, required): The URL which should be called when the subscription fires
      direction (str, required): The SMS direction that should fire the subscripion ("inbound",
                                 "outbound", or "all")
      enabled (bool, optional): Whether or not the subscription should actually fire
      secret (str, optional): A secret to use to encrypt subscription event payloads
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#smseventsubscriptionapi_createorupdatesmseventsubscription
    """

    return self.request(['sms', subscription_id], method='PUT',
                        data=dict(url=url, enabled=enabled, direction=direction,
                                  **kwargs))

  def delete_sms_event_subscription(self, subscription_id):
    """Deletes a specific sms event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#smseventsubscriptionapi_deletesmseventsubscription
    """
    return self.request(['sms', subscription_id], method='DELETE')

