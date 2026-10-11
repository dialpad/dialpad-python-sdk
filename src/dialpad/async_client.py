from typing import AsyncIterator, Optional

import httpx

from .async_resources import AsyncDialpadResourcesMixin

hosts = dict(live='https://dialpad.com', sandbox='https://sandbox.dialpad.com')

# How long to wait on the API before giving up on a request, in seconds.
DEFAULT_TIMEOUT = 600.0


class AsyncDialpadClient(AsyncDialpadResourcesMixin):
  def __init__(
    self,
    token: str,
    sandbox: bool = False,
    base_url: Optional[str] = None,
    company_id: Optional[str] = None,
    timeout: Optional[float] = DEFAULT_TIMEOUT,
  ):
    self._token = token
    self._session = httpx.AsyncClient(timeout=timeout)
    self._base_url = base_url or hosts.get('sandbox' if sandbox else 'live')
    self._company_id = company_id

  @property
  def company_id(self):
    return self._company_id

  @company_id.setter
  def company_id(self, value):
    self._company_id = value

  @company_id.deleter
  def company_id(self):
    self._company_id = None

  def _url(self, path: str) -> str:
    return f'{self._base_url}/{path.lstrip("/")}'

  async def _raw_request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> httpx.Response:
    url = self._url(sub_path)
    # Work on a copy, so that the caller's dict is not left holding the API token.
    headers = dict(headers or {})
    if self.company_id:
      headers.update({'DP-Company-ID': str(self.company_id)})

    headers.update({'Authorization': f'Bearer {self._token}'})
    if str(method).upper() in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
      return await self._session.request(
        method=str(method).upper(),
        url=url,
        headers=headers,
        params=params,
        json=body,
      )
    raise ValueError(f'Unsupported method "{method}"')

  async def iter_request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> AsyncIterator[dict]:
    # Ensure that we have a mutable copy of params.
    params = dict(params or {})
    response = await self._raw_request(
      method=method, sub_path=sub_path, params=params, body=body, headers=headers
    )
    response.raise_for_status()

    if response.status_code == 204:  # No Content
      return

    response_json = response.json()
    if 'items' in response_json:
      for item in (response_json['items'] or []):
        yield item

    while response_json.get('cursor', None):
      params['cursor'] = response_json['cursor']
      response = await self._raw_request(
        method=method, sub_path=sub_path, params=params, body=body, headers=headers
      )
      response.raise_for_status()
      if response.status_code == 204:  # No Content
        return

      response_json = response.json()
      if 'items' in response_json:
        for item in (response_json['items'] or []):
          yield item

  async def request(
    self,
    method: str = 'GET',
    sub_path: Optional[str] = None,
    params: Optional[dict] = None,
    body: Optional[dict] = None,
    headers: Optional[dict] = None,
  ) -> dict:
    response = await self._raw_request(
      method=method, sub_path=sub_path, params=params, body=body, headers=headers
    )
    response.raise_for_status()

    if response.status_code == 204:  # No Content
      return None

    return response.json()
