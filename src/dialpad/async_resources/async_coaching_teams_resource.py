from typing import AsyncIterator, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.coaching_team import (
  CoachingTeamMemberMessage,
  CoachingTeamMemberProto,
  CoachingTeamProto,
)


class AsyncCoachingTeamsResource(AsyncDialpadResource):
  """AsyncCoachingTeamsResource resource class

  Handles API operations for:
  - /api/v2/coachingteams
  - /api/v2/coachingteams/{id}
  - /api/v2/coachingteams/{id}/members"""

  async def add_member(
    self, id: int, request_body: CoachingTeamMemberMessage
  ) -> CoachingTeamMemberProto:
    """Coaching Team -- Add Member

    Add a user to the specified coaching team as trainee or coach.

    Added on July 5th, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: Id of the coaching team
        request_body: The request body.

    Returns:
        A successful response"""
    return await self._request(
      method='POST', sub_path=f'/api/v2/coachingteams/{id}/members', body=request_body
    )

  async def get(self, id: int) -> CoachingTeamProto:
    """Coaching Team -- Get

    Get details of a specified coaching team. Added on Jul 30th, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: Id of the coaching team

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/coachingteams/{id}')

  async def list(self, cursor: Optional[str] = None) -> AsyncIterator[CoachingTeamProto]:
    """Coaching Team -- List

    Get a list of all coaching teams in the company. Added on Feb 3rd, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path='/api/v2/coachingteams', params={'cursor': cursor}
    ):
      yield item

  async def list_members(self, id: int) -> AsyncIterator[CoachingTeamMemberProto]:
    """Coaching Team -- List Members

    Get a list of members of a coaching team. Added on Jul 30th, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: Id of the coaching team

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path=f'/api/v2/coachingteams/{id}/members'
    ):
      yield item
