from dialpad.resources.base import DialpadResource
from dialpad.schemas.call import CallbackMessage, CallbackProto, ValidateCallbackProto


class CallbacksResource(DialpadResource):
  """CallbacksResource resource class

  Handles API operations for:
  - /api/v2/callback
  - /api/v2/callback/validate"""

  def enqueue_callback(self, request_body: CallbackMessage) -> CallbackProto:
    """Call Back -- Enqueue

    Requests a call back to a given number by an operator in a given call center. The call back is added to the queue for the call center like a regular call, and a call is initiated when the next operator becomes available. This API respects all existing call center settings,
    e.g. business / holiday hours and queue settings. This API currently does not allow international call backs. Duplicate call backs for a given number and call center are not allowed. Specific error messages will be provided in case of failure.

    Added on Dec 9, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/callback', body=request_body)

  def validate_callback(self, request_body: CallbackMessage) -> ValidateCallbackProto:
    """Call Back -- Validate

    Performs a dry-run of creating a callback request, without adding it to the call center queue.

    This performs the same validation logic as when actually enqueuing a callback request, allowing early identification of problems which would prevent a successful callback request.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/callback/validate', body=request_body)
