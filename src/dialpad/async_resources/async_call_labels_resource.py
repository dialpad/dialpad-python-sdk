from typing import Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.call_label import CompanyCallLabels


class AsyncCallLabelsResource(AsyncDialpadResource):
  """AsyncCallLabelsResource resource class

  Handles API operations for:
  - /api/v2/calllabels"""

  async def list(self, limit: Optional[int] = None) -> CompanyCallLabels:
    """Label -- List

    Gets all labels for a determined company.

    Added on Nov 15, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        limit: The maximum number of results to return.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path='/api/v2/calllabels', params={'limit': limit})
