from typing import AsyncIterator, Optional


class AsyncDialpadResource(object):
  def __init__(self, client):
    self._client = client

  async def _request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> dict:
    return await self._client.request(
      method=method, sub_path=sub_path, params=params, body=body, headers=headers
    )

  async def _iter_request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> AsyncIterator[dict]:
    async for item in self._client.iter_request(
      method=method, sub_path=sub_path, params=params, body=body, headers=headers
    ):
      yield item
