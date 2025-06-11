from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.signature import SignatureProto


class CreateWebsocket(TypedDict):
  """TypedDict representation of the CreateWebsocket schema."""

  secret: NotRequired[str]
  "[single-line only]\n\nWebsocket's signature secret that's used to confirm the validity of the request."


class UpdateWebsocket(TypedDict):
  """TypedDict representation of the UpdateWebsocket schema."""

  secret: NotRequired[str]
  "[single-line only]\n\nWebsocket's signature secret that's used to confirm the validity of the request."


class WebsocketProto(TypedDict):
  """Websocket."""

  id: NotRequired[int]
  "The webhook's ID, which is generated after creating a webhook successfully."
  signature: NotRequired[SignatureProto]
  "Webhook's signature containing the secret."
  websocket_url: NotRequired[str]
  "The websocket's URL. Users need to connect to this url to get event payloads via websocket."


class WebsocketCollection(TypedDict):
  """Collection of webhooks."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[WebsocketProto]]
  'A list of websocket objects.'
