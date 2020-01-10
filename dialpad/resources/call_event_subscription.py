from .resource import DialpadResource

class CallEventSubscriptionResource(DialpadResource):
  _resource_path = ['event-subscriptions', 'call']

  def put(self, subscription_id, url, enabled=True, group_calls_only=False, **kwargs):
    """ Update or create an event subscription.

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
    """

    return self.request([subscription_id], method='POST',
                        data=dict(url=url, enabled=enabled, group_calls_only=group_calls_only,
                                  **kwargs))

  def get(self, subscription_id):
    return self.request([subscription_id], method='GET')

  def delete(self, subscription_id):
    return self.request([subscription_id], method='DELETE')

  def list(self, limit=25, **kwargs):
    """ List event subscriptions.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request
      target_id (str, optional): The ID of a specific target to use as a filter
      target_type (str, optional): The type of the target (one of "department", "office",
                                   "callcenter", "user", "room", "staffgroup", "callrouter",
                                   "channel", "coachinggroup", or "unknown")
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))
