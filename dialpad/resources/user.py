from .resource import DialpadResource

class UserResource(DialpadResource):
  _resource_path = ['users']

  def get(self, user_id):
    return self.request([user_id])

  def initiate_call(self, user_id, phone_number, **kwargs):
    data = {
      'phone_number': phone_number
    }
    for k in ['group_id', 'group_type', 'outbound_caller_id', 'custom_data']:
      if k in kwargs:
        data[k] = kwargs.pop(k)
    assert not kwargs
    return self.request([user_id, 'initiate_call'], method='POST', data=data)

  def list(self, state='active', limit=25):
    return self.request(data={'limit': limit, 'state': state})

  def assign_number(self, user_id, **kwargs):
    return self.request([user_id, 'assign_number'], method='POST', data=kwargs)
