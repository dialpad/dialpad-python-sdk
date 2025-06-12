from dialpad.resources.base import DialpadResource
from dialpad.schemas.call_review_share_link import (
  CallReviewShareLink,
  CreateCallReviewShareLink,
  UpdateCallReviewShareLink,
)


class CallReviewShareLinksResource(DialpadResource):
  """CallReviewShareLinksResource resource class

  Handles API operations for:
  - /api/v2/callreviewsharelink
  - /api/v2/callreviewsharelink/{id}"""

  def create(self, request_body: CreateCallReviewShareLink) -> CallReviewShareLink:
    """Call Review Sharelink -- Create

    Create a call review share link by call id.

    Added on Sep 21, 2022 for API v2.

    Rate limit: 250 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/callreviewsharelink', body=request_body)

  def delete(self, id: str) -> CallReviewShareLink:
    """Call Review Sharelink -- Delete

    Delete a call review share link by  id.

    Added on Sep 21, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The share link's id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/callreviewsharelink/{id}')

  def get(self, id: str) -> CallReviewShareLink:
    """Call Review Sharelink -- Get

    Gets a call review share link by call id.

    Added on Sep 21, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The share link's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/callreviewsharelink/{id}')

  def update(self, id: str, request_body: UpdateCallReviewShareLink) -> CallReviewShareLink:
    """Call Review Sharelink -- Update

    Update a call review share link by id.

    Added on Sep 21, 2022 for API v2.

    Rate limit: 250 per minute.

    Args:
        id: The share link's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PUT', sub_path=f'/api/v2/callreviewsharelink/{id}', body=request_body
    )
