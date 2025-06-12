from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.deskphone import DeskPhone
from dialpad.schemas.number import AssignNumberMessage, NumberProto, UnassignNumberMessage
from dialpad.schemas.room import (
  CreateInternationalPinProto,
  CreateRoomMessage,
  InternationalPinProto,
  RoomProto,
  UpdateRoomMessage,
)


class RoomsResource(DialpadResource):
  """RoomsResource resource class

  Handles API operations for:
  - /api/v2/rooms
  - /api/v2/rooms/international_pin
  - /api/v2/rooms/{id}
  - /api/v2/rooms/{id}/assign_number
  - /api/v2/rooms/{id}/unassign_number
  - /api/v2/rooms/{parent_id}/deskphones
  - /api/v2/rooms/{parent_id}/deskphones/{id}"""

  def assign_number(self, id: int, request_body: AssignNumberMessage) -> NumberProto:
    """Dialpad Number -- Assign

    Assigns a number to a room. The number will automatically be taken from the company's reserved block if there are reserved numbers, otherwise a number will be auto-assigned from the provided area code.

    Added on March 19, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The room's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/rooms/{id}/assign_number', body=request_body
    )

  def assign_phone_pin(self, request_body: CreateInternationalPinProto) -> InternationalPinProto:
    """Room Phone -- Assign PIN

    Assigns a PIN for making international calls from rooms

    When PIN protected international calls are enabled for the company, a PIN is required to make international calls from room phones.

    Added on Aug 16, 2018 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path='/api/v2/rooms/international_pin', body=request_body
    )

  def create(self, request_body: CreateRoomMessage) -> RoomProto:
    """Room -- Create

    Creates a new room.

    Added on Mar 8, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/rooms', body=request_body)

  def delete(self, id: int) -> RoomProto:
    """Room -- Delete

    Deletes a room by id.

    Added on Mar 8, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The room's id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/rooms/{id}')

  def delete_room_phone(self, id: str, parent_id: int) -> None:
    """Room Phone -- Delete

    Deletes a room desk phone by id. Added on May 17, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The desk phone's id.
        parent_id: The room's id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/rooms/{parent_id}/deskphones/{id}')

  def get(self, id: int) -> RoomProto:
    """Room -- Get

    Gets a room by id.

    Added on Aug 13, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The room's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/rooms/{id}')

  def get_room_phone(self, id: str, parent_id: int) -> DeskPhone:
    """Room Phone -- Get

    Gets a room desk phone by id. Added on May 17, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The desk phone's id.
        parent_id: The room's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/rooms/{parent_id}/deskphones/{id}')

  def list(
    self, cursor: Optional[str] = None, office_id: Optional[int] = None
  ) -> Iterator[RoomProto]:
    """Room -- List

    Gets all rooms in your company, optionally filtering by office.

    Added on Aug 13, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        office_id: The office's id.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/rooms', params={'cursor': cursor, 'office_id': office_id}
    )

  def list_room_phones(self, parent_id: int) -> Iterator[DeskPhone]:
    """Room Phone -- List

    Gets all desk phones under a room. Added on May 17, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        parent_id: The room's id.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(method='GET', sub_path=f'/api/v2/rooms/{parent_id}/deskphones')

  def partial_update(self, id: int, request_body: UpdateRoomMessage) -> RoomProto:
    """Room -- Update

    Updates room details by id.

    Added on Mar 8, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The room's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/rooms/{id}', body=request_body)

  def unassign_number(self, id: int, request_body: UnassignNumberMessage) -> NumberProto:
    """Dialpad Number -- Unassign

    Un-assigns a phone number from a room. The number will be returned to the company's reserved pool if there is one. Otherwise the number will be released.

    Added on March 19, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The room's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/rooms/{id}/unassign_number', body=request_body
    )
