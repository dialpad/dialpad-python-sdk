from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.schedule_reports import (
  ProcessScheduleReportsMessage,
  ScheduleReportsStatusEventSubscriptionProto,
)


class ScheduleReportsResource(DialpadResource):
  """ScheduleReportsResource resource class

  Handles API operations for:
  - /api/v2/schedulereports
  - /api/v2/schedulereports/{id}"""

  def create(
    self, request_body: ProcessScheduleReportsMessage
  ) -> ScheduleReportsStatusEventSubscriptionProto:
    """schedule reports -- Create

    Creates a schedule reports subscription for your company. An endpoint_id is required in order to receive the event payload and can be obtained via websockets or webhooks. A schedule reports is a mechanism to schedule daily, weekly or monthly record and statistics reports.

    Added on Jun 17, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/schedulereports', body=request_body)

  def delete(self, id: int) -> ScheduleReportsStatusEventSubscriptionProto:
    """Schedule reports -- Delete

    Deletes a schedule report subscription by id. A schedule report is a mechanism to schedule daily, weekly or monthly record and statistics reports.

    Added on Jul 6, 2022 for API v2

    Rate limit: 1200 per minute.

    Args:
        id: The schedule reports subscription's ID.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/schedulereports/{id}')

  def get(self, id: int) -> ScheduleReportsStatusEventSubscriptionProto:
    """Schedule reports -- Get

    Gets a schedule report subscription by id. A schedule report is a mechanism to schedule daily, weekly or monthly record and statistics reports.

    Added on Jul 6, 2022 for API v2

    Rate limit: 1200 per minute.

    Args:
        id: The schedule reports subscription's ID.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/schedulereports/{id}')

  def list(
    self, cursor: Optional[str] = None
  ) -> Iterator[ScheduleReportsStatusEventSubscriptionProto]:
    """Schedule reports -- List

    Lists all schedule reports subscription for a company. A schedule report is a mechanism to schedule daily, weekly or monthly record and statistics reports.

    Added on Jul 6, 2022 for API v2

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/schedulereports', params={'cursor': cursor}
    )

  def partial_update(
    self, id: int, request_body: ProcessScheduleReportsMessage
  ) -> ScheduleReportsStatusEventSubscriptionProto:
    """Schedule reports -- Update

    Updates a schedule report subscription by id. A schedule report is a mechanism to schedule daily, weekly or monthly record and statistics reports.

    Added on Jul 6, 2022 for API v2

    Rate limit: 1200 per minute.

    Args:
        id: The schedule reports subscription's ID.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/schedulereports/{id}', body=request_body
    )
