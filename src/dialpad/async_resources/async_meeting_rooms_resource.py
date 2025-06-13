from typing import AsyncIterator, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.uberconference.room import RoomProto


class AsyncMeetingRoomsResource(AsyncDialpadResource):
  """AsyncMeetingRoomsResource resource class

  Handles API operations for:
  - /api/v2/conference/rooms"""

  async def list(self, cursor: Optional[str] = None) -> AsyncIterator[RoomProto]:
    """Meeting Room -- List

    Lists all conference rooms.

    Requires scope: ``conference:read``

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    async for item in self._iter_request(
      method='GET', sub_path='/api/v2/conference/rooms', params={'cursor': cursor}
    ):
      yield item
