from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.webhook import CreateWebhook, UpdateWebhook, WebhookProto


class WebhooksResource(DialpadResource):
  """WebhooksResource resource class

  Handles API operations for:
  - /api/v2/webhooks
  - /api/v2/webhooks/{id}"""

  def create(self, request_body: CreateWebhook) -> WebhookProto:
    """Webhook -- Create

    Creates a new webhook for your company.

    An unique webhook ID will be generated when successfully creating a webhook. A webhook ID is to be required when creating event subscriptions. One webhook ID can be shared between multiple event subscriptions. When triggered, events will be sent to the provided hook_url under webhook. If a secret is provided, the webhook events will be encoded and signed in the JWT format using the shared secret with the HS256 algorithm. The JWT payload should be decoded and the signature verified to ensure that the event came from Dialpad. If no secret is provided, unencoded events will be sent in the JSON format. It is recommended to provide a secret so that you can verify the authenticity of the event.

    Added on April 2nd, 2021 for API v2.

    Rate limit: 100 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/webhooks', body=request_body)

  def delete(self, id: int) -> WebhookProto:
    """Webhook -- Delete

    Deletes a webhook by id.

    Added on April 2nd, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The webhook's ID, which is generated after creating a webhook successfully.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/webhooks/{id}')

  def get(self, id: int) -> WebhookProto:
    """Webhook -- Get

    Gets a webhook by id.

    Added on April 2nd, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The webhook's ID, which is generated after creating a webhook successfully.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/webhooks/{id}')

  def list(self, cursor: Optional[str] = None) -> Iterator[WebhookProto]:
    """Webhook -- List

    Gets a list of all the webhooks that are associated with the company.

    Added on April 2nd, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(method='GET', sub_path='/api/v2/webhooks', params={'cursor': cursor})

  def partial_update(self, id: str, request_body: UpdateWebhook) -> WebhookProto:
    """Webhook -- Update

    Updates a webhook by id.

    Added on April 2nd, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The webhook's ID, which is generated after creating a webhook successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/webhooks/{id}', body=request_body)
