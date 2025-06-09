from typing import Optional, Iterator


class DialpadResource(object):
  _resource_path = None

  def __init__(self, client):
    self._client = client

  def request(self, method: str = 'GET', sub_path: Optional[str] = None, params: Optional[dict] = None, body: Optional[dict] = None, headers: Optional[dict] = None) -> dict:
    if self._resource_path is None:
      raise NotImplementedError('DialpadResource subclasses must define a _resource_path property')

    _path = self._resource_path
    if sub_path:
      _path = f'{_path}/{sub_path}'

    return self._client.request(
      method=method,
      sub_path=_path,
      params=params,
      body=body,
      headers=headers
    )

  def iter_request(self, method: str = 'GET', sub_path: Optional[str] = None, params: Optional[dict] = None, body: Optional[dict] = None, headers: Optional[dict] = None) -> Iterator[dict]:
    if self._resource_path is None:
      raise NotImplementedError('DialpadResource subclasses must define a _resource_path property')

    _path = self._resource_path
    if sub_path:
      _path = f'{_path}/{sub_path}'

    return self._client.iter_request(
      method=method,
      sub_path=_path,
      params=params,
      body=body,
      headers=headers
    )
