from typing import AsyncIterator, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.uberconference.meeting import MeetingSummaryProto


class AsyncMeetingsResource(AsyncDialpadResource):
  """AsyncMeetingsResource resource class

  Handles API operations for:
  - /api/v2/conference/meetings"""

  async def list(
    self, cursor: Optional[str] = None, room_id: Optional[str] = None
  ) -> AsyncIterator[MeetingSummaryProto]:
    """Meeting Summary -- List

    Lists summaries of meetings that have occured in the specified meeting room.

    Requires scope: ``conference:read``

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        room_id: The meeting room's ID.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET',
      sub_path='/api/v2/conference/meetings',
      params={'cursor': cursor, 'room_id': room_id},
    ):
      yield item
