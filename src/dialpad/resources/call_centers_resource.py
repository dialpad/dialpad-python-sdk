from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.group import (
  AddCallCenterOperatorMessage,
  CallCenterProto,
  CallCenterStatusProto,
  CreateCallCenterMessage,
  OperatorCollection,
  OperatorSkillLevelProto,
  RemoveCallCenterOperatorMessage,
  UpdateCallCenterMessage,
  UpdateOperatorSkillLevelMessage,
  UserOrRoomProto,
)


class CallCentersResource(DialpadResource):
  """CallCentersResource resource class

  Handles API operations for:
  - /api/v2/callcenters
  - /api/v2/callcenters/{call_center_id}/operators/{user_id}/skill
  - /api/v2/callcenters/{id}
  - /api/v2/callcenters/{id}/operators
  - /api/v2/callcenters/{id}/status"""

  def add_operator(self, id: int, request_body: AddCallCenterOperatorMessage) -> UserOrRoomProto:
    """Operator -- Add

    Adds an operator to a call center.

    >  Warning
    >
    > This API may result in the usage of call center licenses if required and available. If the licenses are required and not available the operation will fail. Licenses are required when adding an operator that does not have a call center license.

    Added on October 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/callcenters/{id}/operators', body=request_body
    )

  def create(self, request_body: CreateCallCenterMessage) -> CallCenterProto:
    """Call Centers -- Create

    Creates a new call center.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/callcenters', body=request_body)

  def delete(self, id: int) -> CallCenterProto:
    """Call Centers -- Delete

    Deletes a call center by id.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/callcenters/{id}')

  def get(self, id: int) -> CallCenterProto:
    """Call Centers -- Get

    Gets a call center by id. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/callcenters/{id}')

  def get_operator_skill_level(self, call_center_id: int, user_id: int) -> OperatorSkillLevelProto:
    """Operator -- Get Skill Level

    Gets the skill level of an operator within a call center.

    Rate limit: 1200 per minute.

    Args:
        call_center_id: The call center's ID
        user_id: The operator's ID

    Returns:
        A successful response"""
    return self._request(
      method='GET', sub_path=f'/api/v2/callcenters/{call_center_id}/operators/{user_id}/skill'
    )

  def get_status(self, id: int) -> CallCenterStatusProto:
    """Call Centers -- Status

    Gets live status information on the corresponding Call Center.

    Added on August 7, 2023 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/callcenters/{id}/status')

  def list(
    self,
    cursor: Optional[str] = None,
    name_search: Optional[str] = None,
    office_id: Optional[int] = None,
  ) -> Iterator[CallCenterProto]:
    """Call Centers -- List

    Gets all the call centers for the company. Added on Feb 3, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        name_search: search call centers by name or search by the substring of the name. If input example is 'Cool', output example can be a list of call centers whose name contains the string
    'Cool' - ['Cool call center 1', 'Cool call center 2049']
        office_id: search call center by office.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/callcenters',
      params={'cursor': cursor, 'office_id': office_id, 'name_search': name_search},
    )

  def list_operators(self, id: int) -> OperatorCollection:
    """Operators -- List

    Gets operators for a call center. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/callcenters/{id}/operators')

  def partial_update(self, id: int, request_body: UpdateCallCenterMessage) -> CallCenterProto:
    """Call Centers -- Update

    Updates a call center by id.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/callcenters/{id}', body=request_body)

  def remove_operator(
    self, id: int, request_body: RemoveCallCenterOperatorMessage
  ) -> UserOrRoomProto:
    """Operator -- Remove

    Removes an operator from a call center.

    Note: This API will not change or release any licenses.

    Added on October 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='DELETE', sub_path=f'/api/v2/callcenters/{id}/operators', body=request_body
    )

  def update_operator_skill_level(
    self, call_center_id: int, user_id: int, request_body: UpdateOperatorSkillLevelMessage
  ) -> OperatorSkillLevelProto:
    """Operator -- Update Skill Level

    Updates the skill level of an operator within a call center.

    Rate limit: 1200 per minute.

    Args:
        call_center_id: The call center's ID
        user_id: The operator's ID
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH',
      sub_path=f'/api/v2/callcenters/{call_center_id}/operators/{user_id}/skill',
      body=request_body,
    )
