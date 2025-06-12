from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.agent_status_event_subscription import (
  AgentStatusEventSubscriptionProto,
  CreateAgentStatusEventSubscription,
  UpdateAgentStatusEventSubscription,
)


class AgentStatusEventSubscriptionsResource(DialpadResource):
  """AgentStatusEventSubscriptionsResource resource class

  Handles API operations for:
  - /api/v2/subscriptions/agent_status
  - /api/v2/subscriptions/agent_status/{id}"""

  def create(
    self, request_body: CreateAgentStatusEventSubscription
  ) -> AgentStatusEventSubscriptionProto:
    """Agent Status -- Create

    Creates an agent status event subscription for your company. A webhook_id is required so that we know to which url the events shall be sent. Please be aware that only call center agent is supported for agent event subscription now.

    See https://developers.dialpad.com/docs/agent-status-events for details on how agent status events work, including the payload structure and payload examples.

    Added on May 7th, 2021 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path='/api/v2/subscriptions/agent_status', body=request_body
    )

  def delete(self, id: int) -> AgentStatusEventSubscriptionProto:
    """Agent Status -- Delete

    Deletes an agent status event subscription by id.

    Added on May 7th, 2021 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/subscriptions/agent_status/{id}')

  def get(self, id: int) -> AgentStatusEventSubscriptionProto:
    """Agent Status -- Get

    Gets an agent status event subscription by id.

    Added on May 7th, 2021 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/subscriptions/agent_status/{id}')

  def list(self, cursor: Optional[str] = None) -> Iterator[AgentStatusEventSubscriptionProto]:
    """Agent Status -- List

    Gets a list of all the agent status event subscriptions of a company.

    Added on May 7th, 2021 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/subscriptions/agent_status', params={'cursor': cursor}
    )

  def partial_update(
    self, id: str, request_body: UpdateAgentStatusEventSubscription
  ) -> AgentStatusEventSubscriptionProto:
    """Agent Status -- Update

    Updates an agent status event subscription by id.

    Added on May 7th, 2021 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The event subscription's ID, which is generated after creating an event subscription successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/subscriptions/agent_status/{id}', body=request_body
    )
