from .resource import DialpadResource

class DeviceResource(DialpadResource):
  _resource_path = ['devices']

  def get(self, device_id):
    return self.request([device_id])

  def list(self, user_id, limit=25):
    return self.request(data={'user_id': user_id, 'limit': limit})
