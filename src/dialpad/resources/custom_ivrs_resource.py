from typing import Iterator, Literal, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.custom_ivr import (
  CreateCustomIvrMessage,
  CustomIvrDetailsProto,
  CustomIvrProto,
  UpdateCustomIvrDetailsMessage,
  UpdateCustomIvrMessage,
)


class CustomIVRsResource(DialpadResource):
  """CustomIVRsResource resource class

  Handles API operations for:
  - /api/v2/customivrs
  - /api/v2/customivrs/{ivr_id}
  - /api/v2/customivrs/{target_type}/{target_id}/{ivr_type}"""

  def assign(
    self,
    ivr_type: Literal[
      'ASK_FIRST_OPERATOR_NOT_AVAILABLE',
      'AUTO_RECORDING',
      'CALLAI_AUTO_RECORDING',
      'CG_AUTO_RECORDING',
      'CLOSED',
      'CLOSED_DEPARTMENT_INTRO',
      'CLOSED_MENU',
      'CLOSED_MENU_OPTION',
      'CSAT_INTRO',
      'CSAT_OUTRO',
      'CSAT_PREAMBLE',
      'CSAT_QUESTION',
      'DEPARTMENT_INTRO',
      'GREETING',
      'HOLD_AGENT_READY',
      'HOLD_APPREC',
      'HOLD_CALLBACK_ACCEPT',
      'HOLD_CALLBACK_ACCEPTED',
      'HOLD_CALLBACK_CONFIRM',
      'HOLD_CALLBACK_CONFIRM_NUMBER',
      'HOLD_CALLBACK_DIFFERENT_NUMBER',
      'HOLD_CALLBACK_DIRECT',
      'HOLD_CALLBACK_FULFILLED',
      'HOLD_CALLBACK_INVALID_NUMBER',
      'HOLD_CALLBACK_KEYPAD',
      'HOLD_CALLBACK_REJECT',
      'HOLD_CALLBACK_REJECTED',
      'HOLD_CALLBACK_REQUEST',
      'HOLD_CALLBACK_REQUESTED',
      'HOLD_CALLBACK_SAME_NUMBER',
      'HOLD_CALLBACK_TRY_AGAIN',
      'HOLD_CALLBACK_UNDIALABLE',
      'HOLD_ESCAPE_VM_EIGHT',
      'HOLD_ESCAPE_VM_FIVE',
      'HOLD_ESCAPE_VM_FOUR',
      'HOLD_ESCAPE_VM_NINE',
      'HOLD_ESCAPE_VM_ONE',
      'HOLD_ESCAPE_VM_POUND',
      'HOLD_ESCAPE_VM_SEVEN',
      'HOLD_ESCAPE_VM_SIX',
      'HOLD_ESCAPE_VM_STAR',
      'HOLD_ESCAPE_VM_TEN',
      'HOLD_ESCAPE_VM_THREE',
      'HOLD_ESCAPE_VM_TWO',
      'HOLD_ESCAPE_VM_ZERO',
      'HOLD_INTERRUPT',
      'HOLD_INTRO',
      'HOLD_MUSIC',
      'HOLD_POSITION_EIGHT',
      'HOLD_POSITION_FIVE',
      'HOLD_POSITION_FOUR',
      'HOLD_POSITION_MORE',
      'HOLD_POSITION_NINE',
      'HOLD_POSITION_ONE',
      'HOLD_POSITION_SEVEN',
      'HOLD_POSITION_SIX',
      'HOLD_POSITION_TEN',
      'HOLD_POSITION_THREE',
      'HOLD_POSITION_TWO',
      'HOLD_POSITION_ZERO',
      'HOLD_WAIT',
      'MENU',
      'MENU_OPTION',
      'NEXT_TARGET',
      'VM_DROP_MESSAGE',
      'VM_UNAVAILABLE',
      'VM_UNAVAILABLE_CLOSED',
    ],
    target_id: int,
    target_type: Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ],
    request_body: UpdateCustomIvrMessage,
  ) -> CustomIvrProto:
    """Custom IVR -- Assign

    Sets an existing Ivr for a target.

    Added on July 27, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        ivr_type: Type of ivr you want to update
        target_id: The target's id.
        target_type: Target's type.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH',
      sub_path=f'/api/v2/customivrs/{target_type}/{target_id}/{ivr_type}',
      body=request_body,
    )

  def create(self, request_body: CreateCustomIvrMessage) -> CustomIvrDetailsProto:
    """Custom IVR -- Create

    Creates a new custom IVR for a target.

    Added on June 15, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/customivrs', body=request_body)

  def list(
    self,
    target_id: int,
    target_type: Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ],
    cursor: Optional[str] = None,
  ) -> Iterator[CustomIvrProto]:
    """Custom IVR -- Get

    Gets all the custom IVRs for a target.

    Added on July 14, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        target_id: The target's id.
        target_type: Target's type.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/customivrs',
      params={'cursor': cursor, 'target_type': target_type, 'target_id': target_id},
    )

  def partial_update(
    self, ivr_id: str, request_body: UpdateCustomIvrDetailsMessage
  ) -> CustomIvrDetailsProto:
    """Custom IVR -- Update

    Update the name or description of an existing custom ivr.

    Rate limit: 1200 per minute.

    Args:
        ivr_id: The ID of the custom ivr to be updated.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/customivrs/{ivr_id}', body=request_body)

  def unassign(
    self,
    ivr_type: Literal[
      'ASK_FIRST_OPERATOR_NOT_AVAILABLE',
      'AUTO_RECORDING',
      'CALLAI_AUTO_RECORDING',
      'CG_AUTO_RECORDING',
      'CLOSED',
      'CLOSED_DEPARTMENT_INTRO',
      'CLOSED_MENU',
      'CLOSED_MENU_OPTION',
      'CSAT_INTRO',
      'CSAT_OUTRO',
      'CSAT_PREAMBLE',
      'CSAT_QUESTION',
      'DEPARTMENT_INTRO',
      'GREETING',
      'HOLD_AGENT_READY',
      'HOLD_APPREC',
      'HOLD_CALLBACK_ACCEPT',
      'HOLD_CALLBACK_ACCEPTED',
      'HOLD_CALLBACK_CONFIRM',
      'HOLD_CALLBACK_CONFIRM_NUMBER',
      'HOLD_CALLBACK_DIFFERENT_NUMBER',
      'HOLD_CALLBACK_DIRECT',
      'HOLD_CALLBACK_FULFILLED',
      'HOLD_CALLBACK_INVALID_NUMBER',
      'HOLD_CALLBACK_KEYPAD',
      'HOLD_CALLBACK_REJECT',
      'HOLD_CALLBACK_REJECTED',
      'HOLD_CALLBACK_REQUEST',
      'HOLD_CALLBACK_REQUESTED',
      'HOLD_CALLBACK_SAME_NUMBER',
      'HOLD_CALLBACK_TRY_AGAIN',
      'HOLD_CALLBACK_UNDIALABLE',
      'HOLD_ESCAPE_VM_EIGHT',
      'HOLD_ESCAPE_VM_FIVE',
      'HOLD_ESCAPE_VM_FOUR',
      'HOLD_ESCAPE_VM_NINE',
      'HOLD_ESCAPE_VM_ONE',
      'HOLD_ESCAPE_VM_POUND',
      'HOLD_ESCAPE_VM_SEVEN',
      'HOLD_ESCAPE_VM_SIX',
      'HOLD_ESCAPE_VM_STAR',
      'HOLD_ESCAPE_VM_TEN',
      'HOLD_ESCAPE_VM_THREE',
      'HOLD_ESCAPE_VM_TWO',
      'HOLD_ESCAPE_VM_ZERO',
      'HOLD_INTERRUPT',
      'HOLD_INTRO',
      'HOLD_MUSIC',
      'HOLD_POSITION_EIGHT',
      'HOLD_POSITION_FIVE',
      'HOLD_POSITION_FOUR',
      'HOLD_POSITION_MORE',
      'HOLD_POSITION_NINE',
      'HOLD_POSITION_ONE',
      'HOLD_POSITION_SEVEN',
      'HOLD_POSITION_SIX',
      'HOLD_POSITION_TEN',
      'HOLD_POSITION_THREE',
      'HOLD_POSITION_TWO',
      'HOLD_POSITION_ZERO',
      'HOLD_WAIT',
      'MENU',
      'MENU_OPTION',
      'NEXT_TARGET',
      'VM_DROP_MESSAGE',
      'VM_UNAVAILABLE',
      'VM_UNAVAILABLE_CLOSED',
    ],
    target_id: int,
    target_type: Literal[
      'callcenter',
      'callrouter',
      'channel',
      'coachinggroup',
      'coachingteam',
      'department',
      'office',
      'room',
      'staffgroup',
      'unknown',
      'user',
    ],
    request_body: UpdateCustomIvrMessage,
  ) -> CustomIvrDetailsProto:
    """Custom IVR -- Delete

    Delete and un-assign an Ivr from a target.

    Rate limit: 1200 per minute.

    Args:
        ivr_type: Type of ivr you want to update.
        target_id: The id of the target.
        target_type: Target's type. of the custom ivr to be updated.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='DELETE',
      sub_path=f'/api/v2/customivrs/{target_type}/{target_id}/{ivr_type}',
      body=request_body,
    )
