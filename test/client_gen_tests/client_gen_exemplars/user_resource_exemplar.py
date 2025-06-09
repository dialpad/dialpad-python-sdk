from typing import Optional, List, Dict, Union, Literal, Iterator
from dialpad.resources.base import DialpadResource
from dialpad.schemas.user import CreateUserMessage, UserCollection, UserProto


class ApiV2UsersResource(DialpadResource):
  """Resource for the path /api/v2/users"""

  def get(
    self,
    company_admin: Optional[bool] = None,
    cursor: Optional[str] = None,
    email: Optional[str] = None,
    number: Optional[str] = None,
    state: Optional[
      Literal['active', 'all', 'cancelled', 'deleted', 'pending', 'suspended']
    ] = None,
  ) -> Iterator[UserProto]:
    """User -- List

    Gets company users, optionally filtering by email.

    NOTE: The `limit` parameter has been soft-deprecated. Please omit the `limit` parameter, or reduce it to `100` or less.

    - Limit values of greater than `100` will only produce a page size of `100`, and a
      `400 Bad Request` response will be produced 20% of the time in an effort to raise visibility of side-effects that might otherwise go un-noticed by solutions that had assumed a larger page size.

    - The `cursor` value is provided in the API response, and can be passed as a parameter to retrieve subsequent pages of results.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        company_admin: If provided, filter results by the specified value to return only company admins or only non-company admins.
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        email: The user's email.
        number: The user's phone number.
        state: Filter results by the specified user state (e.g. active, suspended, deleted)

    Returns:
        An iterator of items from A successful response"""
    return self.iter_request(
      method='GET',
      params={
        'cursor': cursor,
        'state': state,
        'company_admin': company_admin,
        'email': email,
        'number': number,
      },
    )

  def post(self, request_body: CreateUserMessage) -> UserProto:
    """User -- Create

    Creates a new user.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self.request(method='POST', body=request_body)
