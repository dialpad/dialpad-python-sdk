from .resource import DialpadResource

class WebhookResource(DialpadResource):
  """WebhookResource implements python bindings for the Dialpad API's webhook endpoints.
  
  See https://developers.dialpad.com/reference#webhooks for additional documentation.
  """
  _resource_path = ['webhooks']

  def list_webhooks(self, limit=25, **kwargs):
    """Lists all webhooks.

    Args:
      limit (int, optional): The number of subscriptions to fetch per request

    See Also:
      https://developers.dialpad.com/reference#webhookapi_listwebhooks
    """
    return self.request(method='GET', data=dict(limit=limit, **kwargs))

  def get_webhook(self, webhook_id):
    """Gets a specific webhook.

    Args:
      webhook_id (str, required): The ID of the webhook

    See Also:
      https://developers.dialpad.com/reference#webhookapi_getwebhook
    """
    return self.request([webhook_id], method='GET')

  def create_webhook(self, hook_url, **kwargs):
    """Creates a new webhook.

    Args:
      hook_url (str, required): The URL which should be called when subscriptions fire
      secret (str, optional): A secret to use to encrypt subscription event payloads

    See Also:
      https://developers.dialpad.com/reference#webhookapi_createwebhook
    """
    return self.request(method='POST', data=dict(hook_url=hook_url, **kwargs))

  def update_webhook(self, webhook_id, **kwargs):
    """Updates a specific webhook

    Args:
      webhook_id (str, required): The ID of the webhook
      hook_url (str, optional): The URL which should be called when subscriptions fire
      secret (str, optional): A secret to use to encrypt subscription event payloads

    See Also:
      https://developers.dialpad.com/reference#webhookapi_updatewebhook
    """
    return self.request([webhook_id], method='PATCH', data=kwargs)

  def delete_webhook(self, webhook_id):
    """Deletes a specific webhook.

    Args:
      webhook_id (str, required): The ID of the webhook

    See Also:
      https://developers.dialpad.com/reference#webhookapi_deletewebhook
    """
    return self.request([webhook_id], method='DELETE')
