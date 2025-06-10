from typing import Optional, List, Dict, Union, Literal, Iterator, Any
from dialpad.resources.base import DialpadResource
from dialpad.schemas.wfm.metrics import AgentMetricsResponse


class WFMAgentMetricsResource(DialpadResource):
  """WFMAgentMetricsResource resource class

  Handles API operations for:
  - /api/v2/wfm/metrics/agent"""

  def list(
    self,
    end: str,
    start: str,
    cursor: Optional[str] = None,
    emails: Optional[str] = None,
    ids: Optional[str] = None,
  ) -> Iterator[AgentMetrics]:
    """Agent Metrics

    Returns paginated, detailed agent-level performance metrics.

    Rate limit: 1200 per minute.

    Args:
        cursor: Include the cursor returned in a previous request to get the next page of data
        emails: (optional) Comma-separated email addresses of agents
        end: UTC ISO 8601 timestamp (exclusive, e.g., 2025-02-23T00:00:00Z)
        ids: (optional) Comma-separated Dialpad user IDs of agents
        start: UTC ISO 8601 timestamp (inclusive, e.g., 2025-02-17T00:00:00Z)

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      params={'ids': ids, 'emails': emails, 'cursor': cursor, 'end': end, 'start': start},
    )
