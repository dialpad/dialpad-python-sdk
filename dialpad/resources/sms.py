from .resource import DialpadResource

class SMSResource(DialpadResource):
  _resource_path = ['sms']

  def post(self, user_id, to_numbers, text, sender_group_id=None, sender_group_type=None):
    return self.request(method='POST', data={
      'text': text,
      'user_id': user_id,
      'to_numbers': to_numbers,
      'sender_group_id': sender_group_id,
      'sender_group_type': sender_group_type,
    })

  def list(self, state='active', limit=25):
    return self.request(data={'limit': limit, 'state': state})
