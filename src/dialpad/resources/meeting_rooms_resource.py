from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.uberconference.room import RoomProto


class MeetingRoomsResource(DialpadResource):
  """MeetingRoomsResource resource class

  Handles API operations for:
  - /api/v2/conference/rooms"""

  def list(self, cursor: Optional[str] = None) -> Iterator[RoomProto]:
    """Meeting Room -- List

    Lists all conference rooms.

    Requires scope: ``conference:read``

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/conference/rooms', params={'cursor': cursor}
    )
