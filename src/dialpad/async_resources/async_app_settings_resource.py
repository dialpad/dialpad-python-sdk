from typing import Literal, Optional

from dialpad.async_resources.base import AsyncDialpadResource
from dialpad.schemas.app.setting import AppSettingProto


class AsyncAppSettingsResource(AsyncDialpadResource):
  """AsyncAppSettingsResource resource class

  Handles API operations for:
  - /api/v2/app/settings"""

  async def get(
    self,
    target_id: Optional[int] = None,
    target_type: Optional[
      Literal[
        'callcenter',
        'callrouter',
        'channel',
        'coachinggroup',
        'coachingteam',
        'department',
        'office',
        'room',
        'staffgroup',
        'unknown',
        'user',
      ]
    ] = None,
  ) -> AppSettingProto:
    """App Settings -- GET

    Gets the app settings of the OAuth app that is associated with the API key for the target, if target_type and target_id are provided. Otherwise, will return the app settings for the company.

    Rate limit: 1200 per minute.

    Args:
        target_id: The target's id.
        target_type: The target's type.

    Returns:
        A successful response"""
    return await self._request(
      method='GET',
      sub_path='/api/v2/app/settings',
      params={'target_id': target_id, 'target_type': target_type},
    )
