from .resource import DialpadResource

class TranscriptResource(DialpadResource):
  _resource_path = ['transcripts']

  def get(self, call_id):
    return self.request([call_id])
