from .resource import DialpadResource

class TranscriptResource(DialpadResource):
  """TranscriptResource implements python bindings for the Dialpad API's transcript endpoints.
  See https://developers.dialpad.com/reference#transcripts for additional documentation.
  """
  _resource_path = ['transcripts']

  def get(self, call_id):
    """Get the transcript of a call.

    Args:
      call_id (int, required): The ID of the call.

    See Also:
      https://developers.dialpad.com/reference#transcriptapi_gettranscript
    """
    return self.request([call_id])
