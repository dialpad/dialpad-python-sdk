from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.channel import ChannelProto, CreateChannelMessage
from dialpad.schemas.member_channel import (
  AddChannelMemberMessage,
  MembersProto,
  RemoveChannelMemberMessage,
)


class ChannelsResource(DialpadResource):
  """ChannelsResource resource class

  Handles API operations for:
  - /api/v2/channels
  - /api/v2/channels/{id}
  - /api/v2/channels/{id}/members"""

  def add_member(self, id: int, request_body: AddChannelMemberMessage) -> MembersProto:
    """Member -- Add

    Adds an user to a channel.

    Added on May 12, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The channel's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/channels/{id}/members', body=request_body
    )

  def create(self, request_body: CreateChannelMessage) -> ChannelProto:
    """Channel -- Create

    Creates a new channel.

    Added on May 11, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/channels', body=request_body)

  def delete(self, id: int) -> None:
    """Channel -- Delete

    Deletes a channel by id.

    Added on May 11, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The channel id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/channels/{id}')

  def get(self, id: int) -> ChannelProto:
    """Channel -- Get

    Get channel by id

    Added on May 11, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The channel id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/channels/{id}')

  def list(
    self, cursor: Optional[str] = None, state: Optional[str] = None
  ) -> Iterator[ChannelProto]:
    """Channel -- List

    Lists all channels in the company.

    Added on May 11, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        state: The state of the channel.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/channels', params={'cursor': cursor, 'state': state}
    )

  def list_members(self, id: int, cursor: Optional[str] = None) -> Iterator[MembersProto]:
    """Members -- List

    List all the members from a channel

    Added on May 11, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The channel id
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path=f'/api/v2/channels/{id}/members', params={'cursor': cursor}
    )

  def remove_member(self, id: int, request_body: RemoveChannelMemberMessage) -> None:
    """Member -- Remove

    Removes a member from a channel.

    Added on May 12, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The channel's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='DELETE', sub_path=f'/api/v2/channels/{id}/members', body=request_body
    )
