from dialpad.resources.base import DialpadResource
from dialpad.schemas.stats import ProcessingProto, ProcessStatsMessage, StatsProto


class StatsResource(DialpadResource):
  """StatsResource resource class

  Handles API operations for:
  - /api/v2/stats
  - /api/v2/stats/{id}"""

  def get_result(self, id: str) -> StatsProto:
    """Stats -- Get Result

    Gets the progress and result of a statistics request.

    Added on May 3, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: Request ID returned by a POST /stats request.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/stats/{id}')

  def initiate_processing(self, request_body: ProcessStatsMessage) -> ProcessingProto:
    """Stats -- Initiate Processing

    Begins processing statistics asynchronously, returning a request id to get the status and retrieve the results by calling GET /stats/{request_id}.

    Stats for the whole company will be processed by default. An office_id can be provided to limit stats to a single office. A target_id and target_type can be provided to limit stats to a single target.

    Added on May 3, 2018 for API v2.

    Rate limit: 200 per hour.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/stats', body=request_body)
