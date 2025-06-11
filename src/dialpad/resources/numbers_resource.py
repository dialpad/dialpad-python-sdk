from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.e164_format import FormatNumberResponse
from dialpad.schemas.number import (
  AssignNumberTargetGenericMessage,
  AssignNumberTargetMessage,
  NumberProto,
  SwapNumberMessage,
)


class NumbersResource(DialpadResource):
  """NumbersResource resource class

  Handles API operations for:
  - /api/v2/numbers
  - /api/v2/numbers/assign
  - /api/v2/numbers/format
  - /api/v2/numbers/swap
  - /api/v2/numbers/{number}
  - /api/v2/numbers/{number}/assign"""

  def assign(self, number: str, request_body: AssignNumberTargetMessage) -> NumberProto:
    """Dialpad Number -- Assign

    Assigns a number to a target. Target includes user, department, office, room, callcenter,
    callrouter, staffgroup, channel and coachinggroup. The number will automatically be taken from the company's reserved pool if there are reserved numbers, otherwise a number will be auto-assigned from the provided area code.

    Added on May 26, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        number: A specific number to assign
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/numbers/{number}/assign', body=request_body
    )

  def auto_assign(self, request_body: AssignNumberTargetGenericMessage) -> NumberProto:
    """Dialpad Number -- Auto-Assign

    Assigns a number to a target. The number will automatically be taken from the company's reserved pool if there are reserved numbers, otherwise a number will be auto-assigned from the provided area code. Target includes user, department, office, room, callcenter, callrouter,
    staffgroup, channel and coachinggroup.

    Added on November 18, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/numbers/assign', body=request_body)

  def format_number(
    self, country_code: Optional[str] = None, number: Optional[str] = None
  ) -> FormatNumberResponse:
    """Phone String -- Reformat

    Used to convert local number to E.164 or E.164 to local format.

    Added on June 15, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        country_code: Country code in ISO 3166-1 alpha-2 format such as "US". Required when sending local formatted phone number
        number: Phone number in local or E.164 format

    Returns:
        A successful response"""
    return self._request(
      method='POST',
      sub_path='/api/v2/numbers/format',
      params={'country_code': country_code, 'number': number},
    )

  def get(self, number: str) -> NumberProto:
    """Dialpad Number -- Get

    Gets number details by number.

    Added on May 3, 2018 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        number: A phone number (e164 format).

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/numbers/{number}')

  def list(
    self, cursor: Optional[str] = None, status: Optional[str] = None
  ) -> Iterator[NumberProto]:
    """Dialpad Number -- List

    Gets all numbers in your company.

    Added on May 3, 2018 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        status: Status to filter by.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/numbers', params={'cursor': cursor, 'status': status}
    )

  def swap(self, request_body: SwapNumberMessage) -> NumberProto:
    """Dialpad Number -- Swap

    Swaps a target's primary number with a new one.
    - If a specific number is provided (`type: 'provided_number'`), the target’s primary number is swapped with that number. The provided number must be available in the company’s reserved pool,
    and the `reserve_pool` experiment must be enabled for the company.
    - If an area code is provided (`type: 'area_code'`), an available number from that area code is assigned.
    - If neither is provided (`type: 'auto'`), a number is automatically assigned — first from the company’s reserved pool (if available), otherwise from the target’s office area code. If no type is specified, 'auto' is used by default.

    Added on Mar 28, 2025 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/numbers/swap', body=request_body)

  def unassign(self, number: str, release: Optional[bool] = None) -> NumberProto:
    """Dialpad Number -- Unassign

    Un-assigns a phone number from a target. The number will be returned to the company's reserved pool if there is one. Otherwise the number will be released.

    Added on Jan 28, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        number: A phone number (e164 format).
        release: Releases the number (does not return it to the company reserved pool).

    Returns:
        A successful response"""
    return self._request(
      method='DELETE', sub_path=f'/api/v2/numbers/{number}', params={'release': release}
    )
