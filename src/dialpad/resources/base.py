from typing import Iterator, Optional


class DialpadResource(object):
  def __init__(self, client):
    self._client = client

  def _request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> dict:
    return self._client.request(
      method=method, sub_path=sub_path, params=params, body=body, headers=headers
    )

  def _iter_request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> Iterator[dict]:
    return self._client.iter_request(
      method=method, sub_path=sub_path, params=params, body=body, headers=headers
    )
