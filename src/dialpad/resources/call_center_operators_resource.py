from dialpad.resources.base import DialpadResource
from dialpad.schemas.group import OperatorDutyStatusProto, UpdateOperatorDutyStatusMessage


class CallCenterOperatorsResource(DialpadResource):
  """CallCenterOperatorsResource resource class

  Handles API operations for:
  - /api/v2/callcenters/operators/{id}/dutystatus"""

  def get_duty_status(self, id: int) -> OperatorDutyStatusProto:
    """Operator -- Get Duty Status

    Gets the operator's on duty status and reason.

    Rate limit: 1200 per minute.

    Args:
        id: The operator's user id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/callcenters/operators/{id}/dutystatus')

  def update_duty_status(
    self, id: int, request_body: UpdateOperatorDutyStatusMessage
  ) -> OperatorDutyStatusProto:
    """Operator -- Update Duty Status

    Updates the operator's duty status for all call centers which user belongs to.

    Rate limit: 1200 per minute.

    Args:
        id: The operator's user id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/callcenters/operators/{id}/dutystatus', body=request_body
    )
