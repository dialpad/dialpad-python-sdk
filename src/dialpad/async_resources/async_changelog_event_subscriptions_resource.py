from typing import AsyncIterator, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.change_log_event_subscription import (
  ChangeLogEventSubscriptionProto,
  CreateChangeLogEventSubscription,
  UpdateChangeLogEventSubscription,
)


class AsyncChangelogEventSubscriptionsResource(AsyncDialpadResource):
  """AsyncChangelogEventSubscriptionsResource resource class

  Handles API operations for:
  - /api/v2/subscriptions/changelog
  - /api/v2/subscriptions/changelog/{id}"""

  async def create(
    self, request_body: CreateChangeLogEventSubscription
  ) -> ChangeLogEventSubscriptionProto:
    """Change Log -- Create

    Creates a change log event subscription for your company. An endpoint_id is required so that we know to which url the events shall be sent.

    See https://developers.dialpad.com/docs/change-log-events for details on how change log events work, including the payload structure and payload examples.

    Added on December 9th, 2022 for API v2.

    Requires a company admin API key.

    Requires scope: ``change_log``

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path='/api/v2/subscriptions/changelog', body=request_body
    )

  async def delete(self, id: int) -> ChangeLogEventSubscriptionProto:
    """Change Log -- Delete

    Deletes a change log event subscription by id.

    Added on December 9th, 2022 for API v2.

    Requires a company admin API key.

    Requires scope: ``change_log``

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return await self._request(method='DELETE', sub_path=f'/api/v2/subscriptions/changelog/{id}')

  async def get(self, id: int) -> ChangeLogEventSubscriptionProto:
    """Change Log -- Get

    Gets a change log event subscription by id.

    Added on December 9th, 2022 for API v2.

    Requires a company admin API key.

    Requires scope: ``change_log``

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/subscriptions/changelog/{id}')

  async def list(
    self, cursor: Optional[str] = None
  ) -> AsyncIterator[ChangeLogEventSubscriptionProto]:
    """Change Log -- List

    Gets a list of all the change log event subscriptions of a company.

    Added on December 9th, 2022 for API v2.

    Requires a company admin API key.

    Requires scope: ``change_log``

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path='/api/v2/subscriptions/changelog', params={'cursor': cursor}
    ):
      yield item

  async def partial_update(
    self, id: str, request_body: UpdateChangeLogEventSubscription
  ) -> ChangeLogEventSubscriptionProto:
    """Change Log -- Update

    Updates change log event subscription by id.

    Added on December 9th, 2022 for API v2.

    Requires a company admin API key.

    Requires scope: ``change_log``

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='PATCH', sub_path=f'/api/v2/subscriptions/changelog/{id}', body=request_body
    )
