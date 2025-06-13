from typing import AsyncIterator, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.access_control_policies import (
  AssignmentPolicyMessage,
  CreatePolicyMessage,
  PolicyAssignmentProto,
  PolicyProto,
  UnassignmentPolicyMessage,
  UpdatePolicyMessage,
)


class AsyncAccessControlPoliciesResource(AsyncDialpadResource):
  """AsyncAccessControlPoliciesResource resource class

  Handles API operations for:
  - /api/v2/accesscontrolpolicies
  - /api/v2/accesscontrolpolicies/{id}
  - /api/v2/accesscontrolpolicies/{id}/assign
  - /api/v2/accesscontrolpolicies/{id}/assignments
  - /api/v2/accesscontrolpolicies/{id}/unassign"""

  async def assign(self, id: int, request_body: AssignmentPolicyMessage) -> PolicyAssignmentProto:
    """Access Control Policies -- Assign

    Assigns a user to an access control policy.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The access control policy's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path=f'/api/v2/accesscontrolpolicies/{id}/assign', body=request_body
    )

  async def create(self, request_body: CreatePolicyMessage) -> PolicyProto:
    """Access Control Policies -- Create

    Creates a new custom access control policy.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path='/api/v2/accesscontrolpolicies', body=request_body
    )

  async def delete(self, id: int) -> PolicyProto:
    """Access Control Policies -- Delete

    Deletes a policy by marking the state as deleted, and removing all associated users.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The access control policy's id.

    Returns:
        A successful response"""
    return await self._request(method='DELETE', sub_path=f'/api/v2/accesscontrolpolicies/{id}')

  async def get(self, id: int) -> PolicyProto:
    """Access Control Policies -- Get

    Get a specific access control policy's details.

    Rate limit: 1200 per minute.

    Args:
        id: The access control policy's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/accesscontrolpolicies/{id}')

  async def list(self, cursor: Optional[str] = None) -> AsyncIterator[PolicyProto]:
    """Access Control Policies -- List Policies

    Gets all access control policies belonging to the company.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path='/api/v2/accesscontrolpolicies', params={'cursor': cursor}
    ):
      yield item

  async def list_assignments(
    self, id: int, cursor: Optional[str] = None
  ) -> AsyncIterator[PolicyAssignmentProto]:
    """Access Control Policies -- List Assignments

    Lists all users assigned to this access control policy.

    Rate limit: 1200 per minute.

    Args:
        id: The access control policy's id.
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET',
      sub_path=f'/api/v2/accesscontrolpolicies/{id}/assignments',
      params={'cursor': cursor},
    ):
      yield item

  async def partial_update(self, id: int, request_body: UpdatePolicyMessage) -> PolicyProto:
    """Access Control Policies -- Update

    Updates the provided fields for an existing access control policy.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The access control policy's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='PATCH', sub_path=f'/api/v2/accesscontrolpolicies/{id}', body=request_body
    )

  async def unassign(
    self, id: int, request_body: UnassignmentPolicyMessage
  ) -> PolicyAssignmentProto:
    """Access Control Policies -- Unassign

    Unassigns one or all target groups associated with the user for an access control policy.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The access control policy's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path=f'/api/v2/accesscontrolpolicies/{id}/unassign', body=request_body
    )
