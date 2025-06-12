from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.blocked_number import (
  AddBlockedNumbersProto,
  BlockedNumber,
  RemoveBlockedNumbersProto,
)


class BlockedNumbersResource(DialpadResource):
  """BlockedNumbersResource resource class

  Handles API operations for:
  - /api/v2/blockednumbers
  - /api/v2/blockednumbers/add
  - /api/v2/blockednumbers/remove
  - /api/v2/blockednumbers/{number}"""

  def add(self, request_body: AddBlockedNumbersProto) -> None:
    """Blocked Number -- Add

    Blocks the specified numbers company-wide.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/blockednumbers/add', body=request_body)

  def get(self, number: str) -> BlockedNumber:
    """Blocked Number -- Get

    Gets the specified blocked number.

    Rate limit: 1200 per minute.

    Args:
        number: A phone number (e164 format).

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/blockednumbers/{number}')

  def list(self, cursor: Optional[str] = None) -> Iterator[BlockedNumber]:
    """Blocked Numbers -- List

    Lists all numbers that have been blocked via the API.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/blockednumbers', params={'cursor': cursor}
    )

  def remove(self, request_body: RemoveBlockedNumbersProto) -> None:
    """Blocked Number -- Remove

    Unblocks the specified numbers company-wide.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/blockednumbers/remove', body=request_body)
