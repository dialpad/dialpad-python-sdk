from typing import Iterator, Literal, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.sms_event_subscription import (
  CreateSmsEventSubscription,
  SmsEventSubscriptionProto,
  UpdateSmsEventSubscription,
)


class SmsEventSubscriptionsResource(DialpadResource):
  """SmsEventSubscriptionsResource resource class

  Handles API operations for:
  - /api/v2/subscriptions/sms
  - /api/v2/subscriptions/sms/{id}"""

  def create(self, request_body: CreateSmsEventSubscription) -> SmsEventSubscriptionProto:
    """SMS Event -- Create

    Creates a SMS event subscription. A webhook_id is required so that we know to which url the events shall be sent. A SMS direction is also required in order to limit the direction for which SMS events are sent. Use 'all' to get SMS events for all directions. A target_type and target_id may optionally be provided to scope the events only to SMS to/from that target.

    See https://developers.dialpad.com/docs/sms-events for details on how SMS events work, including the payload structure and payload examples.

    NOTE: **To include the MESSAGE CONTENT in SMS events, your API key needs to have the
    "message_content_export" OAuth scope for when a target is specified in this API and/or
    "message_content_export:all" OAuth scope for when no target is specified.**

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Added on April 9th, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/subscriptions/sms', body=request_body)

  def delete(self, id: int) -> SmsEventSubscriptionProto:
    """SMS Event -- Delete

    Deletes a SMS event subscription by id.

    Added on April 9th, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/subscriptions/sms/{id}')

  def get(self, id: int) -> SmsEventSubscriptionProto:
    """SMS Event -- Get

    Gets a SMS event subscription by id.

    Added on April 9th, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/subscriptions/sms/{id}')

  def list(
    self,
    cursor: Optional[str] = None,
    target_id: Optional[int] = None,
    target_type: Optional[
      Literal[
        'callcenter',
        'callrouter',
        'channel',
        'coachinggroup',
        'coachingteam',
        'department',
        'office',
        'room',
        'staffgroup',
        'unknown',
        'user',
      ]
    ] = None,
  ) -> Iterator[SmsEventSubscriptionProto]:
    """SMS Event -- List

    Gets a list of all the SMS event subscriptions of a company or of a target.

    Added on April 9th, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        target_id: The target's id.
        target_type: Target's type.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/subscriptions/sms',
      params={'cursor': cursor, 'target_type': target_type, 'target_id': target_id},
    )

  def partial_update(
    self, id: int, request_body: UpdateSmsEventSubscription
  ) -> SmsEventSubscriptionProto:
    """SMS Event -- Update

    Updates a SMS event subscription by id.

    Added on April 9th, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/subscriptions/sms/{id}', body=request_body
    )
