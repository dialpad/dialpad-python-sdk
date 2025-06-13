from typing import AsyncIterator, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.coaching_team import CoachingTeamProto
from dialpad.schemas.group import (
  AddOperatorMessage,
  CallCenterProto,
  DepartmentProto,
  OperatorCollection,
  RemoveOperatorMessage,
  UserOrRoomProto,
)
from dialpad.schemas.number import AssignNumberMessage, NumberProto, UnassignNumberMessage
from dialpad.schemas.office import (
  CreateOfficeMessage,
  E911GetProto,
  E911UpdateMessage,
  OffDutyStatusesProto,
  OfficeProto,
  OfficeUpdateResponse,
)
from dialpad.schemas.plan import AvailableLicensesProto, PlanProto


class AsyncOfficesResource(AsyncDialpadResource):
  """AsyncOfficesResource resource class

  Handles API operations for:
  - /api/v2/offices
  - /api/v2/offices/{id}
  - /api/v2/offices/{id}/assign_number
  - /api/v2/offices/{id}/e911
  - /api/v2/offices/{id}/offdutystatuses
  - /api/v2/offices/{id}/operators
  - /api/v2/offices/{id}/unassign_number
  - /api/v2/offices/{office_id}/available_licenses
  - /api/v2/offices/{office_id}/callcenters
  - /api/v2/offices/{office_id}/departments
  - /api/v2/offices/{office_id}/plan
  - /api/v2/offices/{office_id}/teams"""

  async def add_operator(self, id: int, request_body: AddOperatorMessage) -> UserOrRoomProto:
    """Operator -- Add

    Adds an operator into office's mainline.

    Added on Sep 22, 2023 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's ID.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path=f'/api/v2/offices/{id}/operators', body=request_body
    )

  async def assign_number(self, id: int, request_body: AssignNumberMessage) -> NumberProto:
    """Dialpad Number -- Assign

    Assigns a number to a office. The number will automatically be taken from the company's reserved pool if there are reserved numbers, otherwise a number will be auto-assigned from the provided area code.

    Added on March 19, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path=f'/api/v2/offices/{id}/assign_number', body=request_body
    )

  async def create(self, request_body: CreateOfficeMessage) -> OfficeUpdateResponse:
    """Office -- POST Creates a secondary office.



    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(method='POST', sub_path='/api/v2/offices', body=request_body)

  async def get(self, id: int) -> OfficeProto:
    """Office -- Get

    Gets an office by id.

    Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/offices/{id}')

  async def get_billing_plan(self, office_id: int) -> PlanProto:
    """Billing Plan -- Get

    Gets the plan for an office.

    Added on Mar 19, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        office_id: The office's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/offices/{office_id}/plan')

  async def get_e911_address(self, id: int) -> E911GetProto:
    """E911 Address -- Get

    Gets E911 address of the office by office id.

    Added on May 25, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/offices/{id}/e911')

  async def list(
    self, active_only: Optional[bool] = None, cursor: Optional[str] = None
  ) -> AsyncIterator[OfficeProto]:
    """Office -- List

    Gets all the offices that are accessible using your api key.

    Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        active_only: Whether we only return active offices.
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET',
      sub_path='/api/v2/offices',
      params={'cursor': cursor, 'active_only': active_only},
    ):
      yield item

  async def list_available_licenses(self, office_id: int) -> AvailableLicensesProto:
    """Licenses -- List Available

    Gets the available licenses for an office.

    Added on July 2, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        office_id: The office's id.

    Returns:
        A successful response"""
    return await self._request(
      method='GET', sub_path=f'/api/v2/offices/{office_id}/available_licenses'
    )

  async def list_call_centers(
    self, office_id: int, cursor: Optional[str] = None
  ) -> AsyncIterator[CallCenterProto]:
    """Call Centers -- List

    Gets all the call centers for an office. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        office_id: The office's id.
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path=f'/api/v2/offices/{office_id}/callcenters', params={'cursor': cursor}
    ):
      yield item

  async def list_coaching_teams(
    self, office_id: int, cursor: Optional[str] = None
  ) -> AsyncIterator[CoachingTeamProto]:
    """Coaching Team -- List

    Get a list of coaching teams of a office. Added on Jul 30th, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        office_id: The office's id.
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path=f'/api/v2/offices/{office_id}/teams', params={'cursor': cursor}
    ):
      yield item

  async def list_departments(
    self, office_id: int, cursor: Optional[str] = None
  ) -> AsyncIterator[DepartmentProto]:
    """Department -- List

    Gets all the departments for an office. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        office_id: The office's id.
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path=f'/api/v2/offices/{office_id}/departments', params={'cursor': cursor}
    ):
      yield item

  async def list_offduty_statuses(self, id: int) -> OffDutyStatusesProto:
    """Off-Duty Status -- List

    Lists Off-Duty status values.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/offices/{id}/offdutystatuses')

  async def list_operators(self, id: int) -> OperatorCollection:
    """Operator -- List

    Gets mainline operators for an office. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/offices/{id}/operators')

  async def remove_operator(self, id: int, request_body: RemoveOperatorMessage) -> UserOrRoomProto:
    """Operator -- Remove

    Removes an operator from office's mainline.

    Added on Sep 22, 2023 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's ID.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='DELETE', sub_path=f'/api/v2/offices/{id}/operators', body=request_body
    )

  async def unassign_number(self, id: int, request_body: UnassignNumberMessage) -> NumberProto:
    """Dialpad Number -- Unassign

    Un-assigns a phone number from a office mainline. The number will be returned to the company's reserved pool if there is one. Otherwise the number will be released.

    Added on March 19, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path=f'/api/v2/offices/{id}/unassign_number', body=request_body
    )

  async def update_e911_address(self, id: int, request_body: E911UpdateMessage) -> E911GetProto:
    """E911 Address -- Update

    Update E911 address of the given office.

    Added on May 25, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The office's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='PUT', sub_path=f'/api/v2/offices/{id}/e911', body=request_body
    )
