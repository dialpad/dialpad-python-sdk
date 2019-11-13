from .resource import DialpadResource

class SMSResource(DialpadResource):
  _resource_path = ['sms']

  def post(self, user_id, to_numbers, text, target_id=None, target_type=None):
    return self.request(method='POST', data={
      'text': text,
      'user_id': user_id,
      'to_numbers': to_numbers,
      'target_id': target_id,
      'target_type': target_type,
    })

  def list(self, state='active', limit=25):
    return self.request(data={'limit': limit, 'state': state})
