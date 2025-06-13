from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.transcript import TranscriptProto, TranscriptUrlProto


class AsyncTranscriptsResource(AsyncDialpadResource):
  """AsyncTranscriptsResource resource class

  Handles API operations for:
  - /api/v2/transcripts/{call_id}
  - /api/v2/transcripts/{call_id}/url"""

  async def get(self, call_id: int) -> TranscriptProto:
    """Call Transcript -- Get

    Gets the Dialpad AI transcript of a call, including moments.

    Added on Dec 18, 2019 for API v2.

    Rate limit: 1200 per minute.

    Args:
        call_id: The call's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/transcripts/{call_id}')

  async def get_url(self, call_id: int) -> TranscriptUrlProto:
    """Call Transcript -- Get URL

    Gets the transcript url of a call.

    Added on June 9, 2021 for API v2.

    Rate limit: 1200 per minute.

    Args:
        call_id: The call's id.

    Returns:
        A successful response"""
    return await self._request(method='GET', sub_path=f'/api/v2/transcripts/{call_id}/url')
