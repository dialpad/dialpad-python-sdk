from dialpad.resources.base import DialpadResource
from dialpad.schemas.faxline import CreateFaxNumberMessage, FaxNumberProto


class FaxLinesResource(DialpadResource):
  """FaxLinesResource resource class

  Handles API operations for:
  - /api/v2/faxline"""

  def assign(self, request_body: CreateFaxNumberMessage) -> FaxNumberProto:
    """Fax Line -- Assign

    Assigns a fax line to a target. Target includes user and department. Depending on the chosen line type, the number will be taken from the company's reserved pool if there are available reserved numbers, otherwise numbers can be auto-assigned using a provided area code.

    Added on January 13, 2025 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/faxline', body=request_body)
