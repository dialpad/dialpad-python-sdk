from typing import Iterator, Literal, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.call_event_subscription import (
  CallEventSubscriptionProto,
  CreateCallEventSubscription,
  UpdateCallEventSubscription,
)


class CallEventSubscriptionsResource(DialpadResource):
  """CallEventSubscriptionsResource resource class

  Handles API operations for:
  - /api/v2/subscriptions/call
  - /api/v2/subscriptions/call/{id}"""

  def create(self, request_body: CreateCallEventSubscription) -> CallEventSubscriptionProto:
    """Call Event -- Create

    Creates a call event subscription. A webhook_id is required so that we know to which url the events shall be sent. Call states can be used to limit the states for which call events are sent. A target_type and target_id may optionally be provided to scope the events only to the calls to/from that target.

    See https://developers.dialpad.com/docs/call-events-logging for details on how call events work,
    including the payload structure, the meaning of different call states, and payload examples.

    Note: **To include the recording url in call events, your API key needs to have the
    "recordings_export" OAuth scope. For Dialpad Meetings call events, your API key needs to have the "conference:all" OAuth scope.**

    Added on April 23rd, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/subscriptions/call', body=request_body)

  def delete(self, id: int) -> CallEventSubscriptionProto:
    """Call Event -- Delete

    Deletes a call event subscription by id.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/subscriptions/call/{id}')

  def get(self, id: int) -> CallEventSubscriptionProto:
    """Call Event -- Get

    Gets a call event subscription by id.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/subscriptions/call/{id}')

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
  ) -> Iterator[CallEventSubscriptionProto]:
    """Call Event -- List

    Gets a list of all the call event subscriptions of a company or of a target.

    Added on April 23rd, 2021 for API v2.

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
      sub_path='/api/v2/subscriptions/call',
      params={'cursor': cursor, 'target_type': target_type, 'target_id': target_id},
    )

  def partial_update(
    self, id: int, request_body: UpdateCallEventSubscription
  ) -> CallEventSubscriptionProto:
    """Call Event -- Update

    Updates a call event subscription by id.

    Added on April 23rd, 2021 for API v2.

    NOTE: See https://developers.dialpad.com/v1.0-archive/reference for APIs that can operate on subscriptions that were created via the deprecated APIs.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/subscriptions/call/{id}', body=request_body
    )
