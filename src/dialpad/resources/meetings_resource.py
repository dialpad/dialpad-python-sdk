from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.uberconference.meeting import MeetingSummaryProto


class MeetingsResource(DialpadResource):
  """MeetingsResource resource class

  Handles API operations for:
  - /api/v2/conference/meetings"""

  def list(
    self, cursor: Optional[str] = None, room_id: Optional[str] = None
  ) -> Iterator[MeetingSummaryProto]:
    """Meeting Summary -- List

    Lists summaries of meetings that have occured in the specified meeting room.

    Requires scope: ``conference:read``

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        room_id: The meeting room's ID.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/conference/meetings',
      params={'cursor': cursor, 'room_id': room_id},
    )
