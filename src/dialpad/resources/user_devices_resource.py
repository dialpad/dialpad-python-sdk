from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.userdevice import UserDeviceProto


class UserDevicesResource(DialpadResource):
  """UserDevicesResource resource class

  Handles API operations for:
  - /api/v2/userdevices
  - /api/v2/userdevices/{id}"""

  def get(self, id: str) -> UserDeviceProto:
    """User Device -- Get

    Gets a device by ID.

    Added on Feb 4, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The device's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/userdevices/{id}')

  def list(
    self, cursor: Optional[str] = None, user_id: Optional[str] = None
  ) -> Iterator[UserDeviceProto]:
    """User Device -- List

    Lists the devices for a specific user.

    Added on Feb 4, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        user_id: The user's id. ('me' can be used if you are using a user level API key)

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET', sub_path='/api/v2/userdevices', params={'cursor': cursor, 'user_id': user_id}
    )
