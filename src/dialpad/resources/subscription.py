from .resource import DialpadResource

class SubscriptionResource(DialpadResource):
  """SubscriptionResource implements python bindings for the Dialpad API's subscription
  endpoints.
  
  See https://developers.dialpad.com/reference#subscriptions for additional documentation.
  """
  _resource_path = ['subscriptions']

  def list_agent_status_event_subscriptions(self, limit=25, **kwargs):
    """Lists agent status event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request

    See Also:
      https://developers.dialpad.com/reference#webhookagentstatuseventsubscriptionapi_listagentstatuseventsubscriptions
    """
    return self.request(['agent_status'], method='GET', data=dict(limit=limit, **kwargs))

  def get_agent_status_event_subscription(self, subscription_id):
    """Gets a specific agent status event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhookagentstatuseventsubscriptionapi_getagentstatuseventsubscription
    """
    return self.request(['agent_status', subscription_id], method='GET')

  def create_agent_status_event_subscription(self, webhook_id, agent_type, enabled=True, **kwargs):
    """Create a new agent status event subscription.

    Args:
      webhook_id (str, required): The ID of the webhook which should be called when the
                                  subscription fires
      agent_type (str, required): The type of agent to subscribe to updates to
      enabled (bool, optional): Whether or not the subscription should actually fire

    See Also:
      https://developers.dialpad.com/reference#webhookagentstatuseventsubscriptionapi_createagentstatuseventsubscription
    """

    return self.request(['agent_status'], method='POST',
                        data=dict(webhook_id=webhook_id, enabled=enabled, agent_type=agent_type,
                                  **kwargs))

  def update_agent_status_event_subscription(self, subscription_id, **kwargs):
    """Update an existing agent status event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription
      webhook_id (str, optional): The ID of the webhook which should be called when the
                                  subscription fires
      agent_type (str, optional): The type of agent to subscribe to updates to
      enabled (bool, optional): Whether or not the subscription should actually fire

    See Also:
      https://developers.dialpad.com/reference#webhookagentstatuseventsubscriptionapi_updateagentstatuseventsubscription
    """

    return self.request(['agent_status', subscription_id], method='PATCH', data=kwargs)

  def delete_agent_status_event_subscription(self, subscription_id):
    """Deletes a specific agent status event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhookagentstatuseventsubscriptionapi_deleteagentstatuseventsubscription
    """
    return self.request(['agent_status', subscription_id], method='DELETE')


  def list_call_event_subscriptions(self, limit=25, **kwargs):
    """Lists call event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#webhookcalleventsubscriptionapi_listcalleventsubscriptions
    """
    return self.request(['call'], method='GET', data=dict(limit=limit, **kwargs))

  def get_call_event_subscription(self, subscription_id):
    """Gets a specific call event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhookcalleventsubscriptionapi_getcalleventsubscription
    """
    return self.request(['call', subscription_id], method='GET')

  def create_call_event_subscription(self, webhook_id, enabled=True, group_calls_only=False,
                                     **kwargs):
    """Create a new call event subscription.

    Args:
      webhook_id (str, required): The ID of the webhook which should be called when the
                                  subscription fires
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
      https://developers.dialpad.com/reference#webhookcalleventsubscriptionapi_createcalleventsubscription
    """

    return self.request(['call'], method='POST',
                        data=dict(webhook_id=webhook_id, enabled=enabled, group_calls_only=group_calls_only,
                                  **kwargs))

  def update_call_event_subscription(self, subscription_id, **kwargs):
    """Update an existing call event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription
      webhook_id (str, optional): The ID of the webhook which should be called when the
                                  subscription fires
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
      https://developers.dialpad.com/reference#webhookcalleventsubscriptionapi_updatecalleventsubscription
    """
    return self.request(['call', subscription_id], method='PATCH', data=kwargs)

  def delete_call_event_subscription(self, subscription_id):
    """Deletes a specific call event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhookcalleventsubscriptionapi_deletecalleventsubscription
    """
    return self.request(['call', subscription_id], method='DELETE')


  def list_contact_event_subscriptions(self, limit=25, **kwargs):
    """Lists contact event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request

    See Also:
      https://developers.dialpad.com/reference#webhookcontacteventsubscriptionapi_listcontacteventsubscriptions
    """
    return self.request(['contact'], method='GET', data=dict(limit=limit, **kwargs))

  def get_contact_event_subscription(self, subscription_id):
    """Gets a specific contact event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhookcontacteventsubscriptionapi_getcontacteventsubscription
    """
    return self.request(['contact', subscription_id], method='GET')

  def create_contact_event_subscription(self, webhook_id, contact_type, enabled=True, **kwargs):
    """Create a new contact event subscription.

    Args:
      webhook_id (str, required): The ID of the webhook which should be called when the
                                  subscription fires
      contact_type (str, required): The type of contact to subscribe to events for
      enabled (bool, optional): Whether or not the subscription should actually fire

    See Also:
      https://developers.dialpad.com/reference#webhookcontacteventsubscriptionapi_createcontacteventsubscription
    """

    return self.request(['contact'], method='POST',
                        data=dict(webhook_id=webhook_id, enabled=enabled,
                                  contact_type=contact_type, **kwargs))

  def update_contact_event_subscription(self, subscription_id, **kwargs):
    """Update an existing contact event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription
      webhook_id (str, optional): The ID of the webhook which should be called when the
                                  subscription fires
      contact_type (str, optional): The type of contact to subscribe to events for
      enabled (bool, optional): Whether or not the subscription should actually fire

    See Also:
      https://developers.dialpad.com/reference#webhookcontacteventsubscriptionapi_updatecontacteventsubscription
    """
    return self.request(['contact', subscription_id], method='PATCH', data=kwargs)

  def delete_contact_event_subscription(self, subscription_id):
    """Deletes a specific contact event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhookcontacteventsubscriptionapi_deletecontacteventsubscription
    """
    return self.request(['contact', subscription_id], method='DELETE')


  def list_sms_event_subscriptions(self, limit=25, **kwargs):
    """Lists SMS event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#webhooksmseventsubscriptionapi_listsmseventsubscriptions
    """
    return self.request(['sms'], method='GET', data=dict(limit=limit, **kwargs))

  def get_sms_event_subscription(self, subscription_id):
    """Gets a specific sms event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhooksmseventsubscriptionapi_getsmseventsubscription
    """
    return self.request(['sms', subscription_id], method='GET')

  def create_sms_event_subscription(self, webhook_id, direction, enabled=True, **kwargs):
    """Create a new SMS event subscription.

    Args:
      webhook_id (str, required): The ID of the webhook which should be called when the
                                  subscription fires
      direction (str, required): The SMS direction that should fire the subscripion ("inbound",
                                 "outbound", or "all")
      enabled (bool, optional): Whether or not the subscription should actually fire
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#smseventsubscriptionapi_createorupdatesmseventsubscription
    """

    return self.request(['sms'], method='POST',
                        data=dict(webhook_id=webhook_id, enabled=enabled, direction=direction,
                                  **kwargs))

  def update_sms_event_subscription(self, subscription_id, **kwargs):
    """Update an existing SMS event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription
      webhook_id (str, optional): The ID of the webhook which should be called when the
                                  subscription fires
      direction (str, optional): The SMS direction that should fire the subscripion ("inbound",
                                 "outbound", or "all")
      enabled (bool, optional): Whether or not the subscription should actually fire
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")

    See Also:
      https://developers.dialpad.com/reference#smseventsubscriptionapi_createorupdatesmseventsubscription
    """

    return self.request(['sms', subscription_id], method='PATCH', data=kwargs)

  def delete_sms_event_subscription(self, subscription_id):
    """Deletes a specific sms event subscription.

    Args:
      subscription_id (str, required): The ID of the subscription

    See Also:
      https://developers.dialpad.com/reference#webhooksmseventsubscriptionapi_deletesmseventsubscription
    """
    return self.request(['sms', subscription_id], method='DELETE')

