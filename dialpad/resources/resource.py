class DialpadResource(object):
  _resource_path = None

  def __init__(self, client, basepath=None):
    self._client = client

  def request(self, path=None, *args, **kwargs):
    if self._resource_path is None:
      raise NotImplementedError('DialpadResource subclasses must have a _resource_path property')
    path = path or []
    return self._client.request(self._resource_path + path, *args, **kwargs)
