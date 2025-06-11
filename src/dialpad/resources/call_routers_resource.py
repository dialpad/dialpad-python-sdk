from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.call_router import (
  ApiCallRouterProto,
  CreateApiCallRouterMessage,
  UpdateApiCallRouterMessage,
)
from dialpad.schemas.number import AssignNumberMessage, NumberProto


class CallRoutersResource(DialpadResource):
  """CallRoutersResource resource class

  Handles API operations for:
  - /api/v2/callrouters
  - /api/v2/callrouters/{id}
  - /api/v2/callrouters/{id}/assign_number"""

  def assign_number(self, id: int, request_body: AssignNumberMessage) -> NumberProto:
    """Dialpad Number -- Assign

    Assigns a number to a callrouter. The number will automatically be taken from the company's reserved pool if there are reserved numbers, otherwise a number will be auto-assigned from the provided area code.

    Rate limit: 1200 per minute.

    Args:
        id: The API call router's ID
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/callrouters/{id}/assign_number', body=request_body
    )

  def create(self, request_body: CreateApiCallRouterMessage) -> ApiCallRouterProto:
    """Call Router -- Create

    Creates a new API-based call router.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/callrouters', body=request_body)

  def delete(self, id: str) -> None:
    """Call Router -- Delete

    Deletes the API call router with the given ID.

    Rate limit: 1200 per minute.

    Args:
        id: The API call router's ID

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/callrouters/{id}')

  def get(self, id: int) -> ApiCallRouterProto:
    """Call Router -- Get

    Gets the API call router with the given ID.

    Rate limit: 1200 per minute.

    Args:
        id: The API call router's ID

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/callrouters/{id}')

  def list(
    self, cursor: Optional[str] = None, office_id: Optional[int] = None
  ) -> Iterator[ApiCallRouterProto]:
    """Call Router -- List

    Lists all of the API call routers for a given company or office.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        office_id: The office's id.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/callrouters',
      params={'cursor': cursor, 'office_id': office_id},
    )

  def partial_update(self, id: str, request_body: UpdateApiCallRouterMessage) -> ApiCallRouterProto:
    """Call Router -- Update

    Updates the API call router with the given ID.

    Rate limit: 1 per 5 minute.

    Args:
        id: The API call router's ID
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/callrouters/{id}', body=request_body)
