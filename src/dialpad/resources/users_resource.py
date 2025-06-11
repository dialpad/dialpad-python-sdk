from typing import Iterator, Literal, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.call import (
  ActiveCallProto,
  InitiateCallMessage,
  InitiatedCallProto,
  ToggleViMessage,
  ToggleViProto,
  UpdateActiveCallMessage,
)
from dialpad.schemas.caller_id import CallerIdProto, SetCallerIdMessage
from dialpad.schemas.deskphone import DeskPhone
from dialpad.schemas.number import AssignNumberMessage, NumberProto, UnassignNumberMessage
from dialpad.schemas.office import E911GetProto
from dialpad.schemas.screen_pop import InitiateScreenPopMessage, InitiateScreenPopResponse
from dialpad.schemas.user import (
  CreateUserMessage,
  E911UpdateMessage,
  MoveOfficeMessage,
  PersonaProto,
  SetStatusMessage,
  SetStatusProto,
  ToggleDNDMessage,
  ToggleDNDProto,
  UpdateUserMessage,
  UserProto,
)


class UsersResource(DialpadResource):
  """UsersResource resource class

  Handles API operations for:
  - /api/v2/users
  - /api/v2/users/{id}
  - /api/v2/users/{id}/activecall
  - /api/v2/users/{id}/assign_number
  - /api/v2/users/{id}/caller_id
  - /api/v2/users/{id}/e911
  - /api/v2/users/{id}/initiate_call
  - /api/v2/users/{id}/move_office
  - /api/v2/users/{id}/personas
  - /api/v2/users/{id}/screenpop
  - /api/v2/users/{id}/status
  - /api/v2/users/{id}/togglednd
  - /api/v2/users/{id}/togglevi
  - /api/v2/users/{id}/unassign_number
  - /api/v2/users/{parent_id}/deskphones
  - /api/v2/users/{parent_id}/deskphones/{id}"""

  def assign_number(self, id: int, request_body: AssignNumberMessage) -> NumberProto:
    """Dialpad Number -- Assign

    Assigns a number to a user. The number will automatically be taken from the company's reserved block if there are reserved numbers, otherwise a number will be auto-assigned from the provided area code.

    Added on May 3, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/users/{id}/assign_number', body=request_body
    )

  def create(self, request_body: CreateUserMessage) -> UserProto:
    """User -- Create

    Creates a new user.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/users', body=request_body)

  def delete(self, id: str) -> UserProto:
    """User -- Delete

    Deletes a user by id.

    Added on May 11, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/users/{id}')

  def delete_deskphone(self, id: str, parent_id: int) -> None:
    """Desk Phone -- Delete

    Deletes a user desk phone by id. Added on May 17, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The desk phone's id.
        parent_id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/users/{parent_id}/deskphones/{id}')

  def get(self, id: str) -> UserProto:
    """User -- Get

    Gets a user by id.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/users/{id}')

  def get_caller_id(self, id: str) -> CallerIdProto:
    """Caller ID -- Get

    List all available Caller IDs and the active Called ID for a determined User id

    Added on Aug 3, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/users/{id}/caller_id')

  def get_deskphone(self, id: str, parent_id: int) -> DeskPhone:
    """Desk Phone -- Get

    Gets a user desk phone by id. Added on May 17, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The desk phone's id.
        parent_id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/users/{parent_id}/deskphones/{id}')

  def get_e911_address(self, id: int) -> E911GetProto:
    """E911 Address -- Get

    Gets E911 address of the user by user id.

    Added on May 25, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/users/{id}/e911')

  def initiate_call(self, id: str, request_body: InitiateCallMessage) -> InitiatedCallProto:
    """Call -- Initiate

    Causes a user's native Dialpad application to initiate an outbound call. Added on Nov 18, 2019 for API v2.

    Rate limit: 5 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/users/{id}/initiate_call', body=request_body
    )

  def list(
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
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/users',
      params={
        'cursor': cursor,
        'state': state,
        'company_admin': company_admin,
        'email': email,
        'number': number,
      },
    )

  def list_deskphones(self, parent_id: int) -> Iterator[DeskPhone]:
    """Desk Phone -- List

    Gets all desk phones under a user. Added on May 17, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        parent_id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(method='GET', sub_path=f'/api/v2/users/{parent_id}/deskphones')

  def list_personas(self, id: str) -> Iterator[PersonaProto]:
    """Persona -- List

    Provides a list of personas for a user.

    A persona is a target that a user can make calls from. The receiver of the call will see the details of the persona rather than the user.

    Added on February 12, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(method='GET', sub_path=f'/api/v2/users/{id}/personas')

  def move_office(self, id: str, request_body: MoveOfficeMessage) -> UserProto:
    """User -- Switch Office

    Moves the user to a different office. For international offices only, all of the user's numbers will be unassigned and a new number will be assigned except when the user only has internal numbers starting with 803 -- then the numbers will remain unchanged. Admin can also assign numbers via the user assign number API after. Only supported on paid accounts and there must be enough licenses to transfer the user to the destination office.

    Added on May 31, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/users/{id}/move_office', body=request_body
    )

  def partial_update(self, id: str, request_body: UpdateUserMessage) -> UserProto:
    """User -- Update

    Updates the provided fields for an existing user.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/users/{id}', body=request_body)

  def set_caller_id(self, id: str, request_body: SetCallerIdMessage) -> CallerIdProto:
    """Caller ID -- POST

    Set Caller ID for a determined User id.

    Added on Aug 3, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path=f'/api/v2/users/{id}/caller_id', body=request_body)

  def set_e911_address(self, id: int, request_body: E911UpdateMessage) -> E911GetProto:
    """E911 Address -- Update

    Update E911 address of the given user.

    Added on May 25, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PUT', sub_path=f'/api/v2/users/{id}/e911', body=request_body)

  def toggle_active_call_recording(
    self, id: int, request_body: UpdateActiveCallMessage
  ) -> ActiveCallProto:
    """Call Recording -- Toggle

    Turns call recording on or off for a user's active call.

    Added on Nov 18, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/users/{id}/activecall', body=request_body
    )

  def toggle_active_call_vi(self, id: int, request_body: ToggleViMessage) -> ToggleViProto:
    """Call VI -- Toggle

    Turns call vi on or off for a user's active call. Added on May 4, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/users/{id}/togglevi', body=request_body)

  def toggle_dnd(self, id: str, request_body: ToggleDNDMessage) -> ToggleDNDProto:
    """Do Not Disturb -- Toggle

    Toggle DND status on or off for the given user.

    Added on Oct 14, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/users/{id}/togglednd', body=request_body
    )

  def trigger_screenpop(
    self, id: int, request_body: InitiateScreenPopMessage
  ) -> InitiateScreenPopResponse:
    """Screen-pop -- Trigger

    Initiates screen pop for user device. Requires the "screen_pop" scope.

    Requires scope: ``screen_pop``

    Rate limit: 5 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path=f'/api/v2/users/{id}/screenpop', body=request_body)

  def unassign_number(self, id: int, request_body: UnassignNumberMessage) -> NumberProto:
    """Dialpad Number -- Unassign

    Un-assigns a phone number from a user. The number will be returned to the company's reserved block if there is one. Otherwise the number will be released.

    Added on May 3, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/users/{id}/unassign_number', body=request_body
    )

  def update_user_status(self, id: int, request_body: SetStatusMessage) -> SetStatusProto:
    """User Status -- Update

    Update user's status. Returns the user's status if the user exists.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/users/{id}/status', body=request_body)
