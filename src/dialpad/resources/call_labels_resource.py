from typing import Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.call_label import CompanyCallLabels


class CallLabelsResource(DialpadResource):
  """CallLabelsResource resource class

  Handles API operations for:
  - /api/v2/calllabels"""

  def list(self, limit: Optional[int] = None) -> CompanyCallLabels:
    """Label -- List

    Gets all labels for a determined company.

    Added on Nov 15, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        limit: The maximum number of results to return.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path='/api/v2/calllabels', params={'limit': limit})
