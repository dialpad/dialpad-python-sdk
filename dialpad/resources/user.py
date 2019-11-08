from .resource import DialpadResource

class UserResource(DialpadResource):
  _resource_path = ['users']

  def get(self, user_id):
    return self.request([user_id])

  def list(self, state='active', limit=25):
    return self.request(data={'limit': limit, 'state': state})
