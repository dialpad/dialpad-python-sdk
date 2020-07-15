from .resource import DialpadResource

class CallRouterResource(DialpadResource):
  _resource_path = ['callrouters']

  def get(self, call_router_id):
    return self.request([call_router_id])

  def post(self, **kwargs):
    return self.request(method='POST', data=kwargs)

  def patch(self, call_router_id, **kwargs):
    return self.request([call_router_id], method='PATCH', data=kwargs)

  def delete(self, call_router_id):
    return self.request([call_router_id], method='DELETE')
