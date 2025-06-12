from dialpad.resources.base import DialpadResource
from dialpad.schemas.recording_share_link import (
  CreateRecordingShareLink,
  RecordingShareLink,
  UpdateRecordingShareLink,
)


class RecordingShareLinksResource(DialpadResource):
  """RecordingShareLinksResource resource class

  Handles API operations for:
  - /api/v2/recordingsharelink
  - /api/v2/recordingsharelink/{id}"""

  def create(self, request_body: CreateRecordingShareLink) -> RecordingShareLink:
    """Recording Sharelink -- Create

    Creates a recording share link.

    Added on Aug 26, 2021 for API v2.

    Rate limit: 100 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/recordingsharelink', body=request_body)

  def delete(self, id: str) -> RecordingShareLink:
    """Recording Sharelink -- Delete

    Deletes a recording share link by id.

    Added on Aug 26, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The recording share link's ID.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/recordingsharelink/{id}')

  def get(self, id: str) -> RecordingShareLink:
    """Recording Sharelink -- Get

    Gets a recording share link by id.

    Added on Aug 26, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The recording share link's ID.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/recordingsharelink/{id}')

  def update(self, id: str, request_body: UpdateRecordingShareLink) -> RecordingShareLink:
    """Recording Sharelink -- Update

    Updates a recording share link by id.

    Added on Aug 26, 2021 for API v2.

    Rate limit: 100 per minute.

    Args:
        id: The recording share link's ID.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PUT', sub_path=f'/api/v2/recordingsharelink/{id}', body=request_body
    )
