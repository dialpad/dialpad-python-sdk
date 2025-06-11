from typing import Iterator, Literal, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.call import (
  AddCallLabelsMessage,
  AddParticipantMessage,
  CallProto,
  InitiatedIVRCallProto,
  OutboundIVRMessage,
  RingCallMessage,
  RingCallProto,
  TransferCallMessage,
  TransferredCallProto,
  UnparkCallMessage,
)


class CallsResource(DialpadResource):
  """CallsResource resource class

  Handles API operations for:
  - /api/v2/call
  - /api/v2/call/initiate_ivr_call
  - /api/v2/call/{id}
  - /api/v2/call/{id}/actions/hangup
  - /api/v2/call/{id}/labels
  - /api/v2/call/{id}/participants/add
  - /api/v2/call/{id}/transfer
  - /api/v2/call/{id}/unpark"""

  def add_participant(self, id: int, request_body: AddParticipantMessage) -> RingCallProto:
    """Call -- Add Participant

    Adds another participant to a call. Valid methods to add are by phone or by target. Targets require to have a primary phone Added on Nov 11, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/call/{id}/participants/add', body=request_body
    )

  def get(self, id: int) -> CallProto:
    """Call -- Get

    Get Call status and other information. Added on May 25, 2021 for API v2.

    Rate limit: 10 per minute.

    Args:
        id: The call's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/call/{id}')

  def hangup_call(self, id: int) -> None:
    """Call Actions -- Hang up

    Hangs up the call. Added on Oct 25, 2024 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call's id.

    Returns:
        A successful response"""
    return self._request(method='PUT', sub_path=f'/api/v2/call/{id}/actions/hangup')

  def initiate_ivr_call(self, request_body: OutboundIVRMessage) -> InitiatedIVRCallProto:
    """Call -- Initiate IVR Call

    Initiates an outbound call to ring an IVR Workflow.

    Added on Aug 14, 2023 for API v2.

    Rate limit: 10 per minute per IVR.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path='/api/v2/call/initiate_ivr_call', body=request_body
    )

  def initiate_ring_call(self, request_body: RingCallMessage) -> RingCallProto:
    """Call -- Initiate via Ring

    Initiates an outbound call to ring all devices (or a single specified device).

    Added on Feb 20, 2020 for API v2.

    Rate limit: 5 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/call', body=request_body)

  def list(
    self,
    cursor: Optional[str] = None,
    started_after: Optional[int] = None,
    started_before: Optional[int] = None,
    target_id: Optional[int] = None,
    target_type: Optional[
      Literal[
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
      ]
    ] = None,
  ) -> Iterator[CallProto]:
    """Call -- List

    Provides a paginated list of calls matching the specified filter parameters in reverse-chronological order by call start time (i.e. recent calls first)

    Note: This API will only include calls that have already concluded.

    Added on May 27, 2024 for API v2.

    Requires a company admin API key.

    Requires scope: ``calls:list``

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        started_after: Only includes calls that started more recently than the specified timestamp.
    (UTC ms-since-epoch timestamp)
        started_before: Only includes calls that started prior to the specified timestamp.
    (UTC ms-since-epoch timestamp)
        target_id: The ID of a target to filter against.
        target_type: The target type associated with the target ID.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/call',
      params={
        'cursor': cursor,
        'started_after': started_after,
        'started_before': started_before,
        'target_id': target_id,
        'target_type': target_type,
      },
    )

  def set_call_label(self, id: int, request_body: AddCallLabelsMessage) -> CallProto:
    """Label -- Set

    Set Labels for a determined call id.

    Added on Nov 15, 2022 for API v2.

    Rate limit: 250 per minute.

    Args:
        id: The call's id
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PUT', sub_path=f'/api/v2/call/{id}/labels', body=request_body)

  def transfer(self, id: int, request_body: TransferCallMessage) -> TransferredCallProto:
    """Call -- Transfer

    Transfers call to another recipient. Added on Sep 25, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path=f'/api/v2/call/{id}/transfer', body=request_body)

  def unpark(self, id: int, request_body: UnparkCallMessage) -> RingCallProto:
    """Call -- Unpark

    Unparks call from Office mainline. Added on Nov 11, 2024 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path=f'/api/v2/call/{id}/unpark', body=request_body)
