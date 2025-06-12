from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.contact_event_subscription import (
  ContactEventSubscriptionProto,
  CreateContactEventSubscription,
  UpdateContactEventSubscription,
)


class ContactEventSubscriptionsResource(DialpadResource):
  """ContactEventSubscriptionsResource resource class

  Handles API operations for:
  - /api/v2/subscriptions/contact
  - /api/v2/subscriptions/contact/{id}"""

  def create(self, request_body: CreateContactEventSubscription) -> ContactEventSubscriptionProto:
    """Contact Event -- Create

    Creates a contact event subscription for your company. A webhook_id is required so that we know to which url the events shall be sent.

    See https://developers.dialpad.com/docs/contact-events for details on how contact events work, including the payload structure and payload examples.

    Added on April 23rd, 2021 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/subscriptions/contact', body=request_body)

  def delete(self, id: int) -> ContactEventSubscriptionProto:
    """Contact Event -- Delete

    Deletes a contact event subscription by id.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/subscriptions/contact/{id}')

  def get(self, id: int) -> ContactEventSubscriptionProto:
    """Contact Event -- Get

    Gets a contact event subscription by id.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/subscriptions/contact/{id}')

  def list(self, cursor: Optional[str] = None) -> Iterator[ContactEventSubscriptionProto]:
    """Contact Event -- List

    Gets a list of all the contact event subscriptions of a company.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/subscriptions/contact', params={'cursor': cursor}
    )

  def partial_update(
    self, id: int, request_body: UpdateContactEventSubscription
  ) -> ContactEventSubscriptionProto:
    """Contact Event -- Update

    Updates a contact event subscription by id.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/subscriptions/contact/{id}', body=request_body
    )
