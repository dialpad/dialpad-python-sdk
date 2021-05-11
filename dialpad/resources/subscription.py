from .resource import DialpadResource

class SubscriptionResource(DialpadResource):
  """SubscriptionResource implements python bindings for the Dialpad API's subscription
  endpoints.
  
  See https://developers.dialpad.com/reference#subscriptions for additional documentation.
  """
  _resource_path = ['subscriptions']

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
