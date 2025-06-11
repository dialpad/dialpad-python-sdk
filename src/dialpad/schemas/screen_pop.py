from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.userdevice import UserDeviceProto


class InitiateScreenPopMessage(TypedDict):
  """TypedDict representation of the InitiateScreenPopMessage schema."""

  screen_pop_uri: str
  'The screen pop\'s url.\n\nMost Url should start with scheme name such as http or https. Be aware that url with userinfo subcomponent, such as\n"https://username:password@www.example.com" is not supported for security reasons. Launching native apps is also supported through a format such as "customuri://domain.com"'


class InitiateScreenPopResponse(TypedDict):
  """Screen pop initiation."""

  device: NotRequired[UserDeviceProto]
  'A device owned by the user.'
