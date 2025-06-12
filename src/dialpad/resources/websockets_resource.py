from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.websocket import (
  CreateWebsocket,
  UpdateWebsocket,
  WebsocketProto,
)


class WebsocketsResource(DialpadResource):
  """WebsocketsResource resource class

  Handles API operations for:
  - /api/v2/websockets
  - /api/v2/websockets/{id}"""

  def create(self, request_body: CreateWebsocket) -> WebsocketProto:
    """Websocket -- Create

    Creates a new websocket for your company.

    A unique websocket ID will be generated when successfully creating a websocket. A websocket ID is to be required when creating event subscriptions. One websocket ID can be shared between multiple event subscriptions. When triggered, events will be accessed through provided websocket_url under websocket. The url will be expired after 1 hour. Please use the GET websocket API to regenerate url rather than creating new ones. If a secret is provided, the websocket events will be encoded and signed in the JWT format using the shared secret with the HS256 algorithm. The JWT payload should be decoded and the signature verified to ensure that the event came from Dialpad. If no secret is provided, unencoded events will be sent in the JSON format. It is recommended to provide a secret so that you can verify the authenticity of the event.

    Added on April 5th, 2022 for API v2.

    Rate limit: 250 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/websockets', body=request_body)

  def delete(self, id: int) -> WebsocketProto:
    """Websocket -- Delete

    Deletes a websocket by id.

    Added on April 2nd, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The websocket's ID, which is generated after creating a websocket successfully.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/websockets/{id}')

  def get(self, id: int) -> WebsocketProto:
    """Websocket -- Get

    Gets a websocket by id.

    Added on April 5th, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The websocket's ID, which is generated after creating a websocket successfully.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/websockets/{id}')

  def list(self, cursor: Optional[str] = None) -> Iterator[WebsocketProto]:
    """Websocket -- List

    Gets a list of all the websockets that are associated with the company.

    Added on April 5th, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/websockets', params={'cursor': cursor}
    )

  def partial_update(self, id: int, request_body: UpdateWebsocket) -> WebsocketProto:
    """Websocket -- Update

    Updates a websocket by id.

    Added on April 5th, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The websocket's ID, which is generated after creating a websocket successfully.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/websockets/{id}', body=request_body)
