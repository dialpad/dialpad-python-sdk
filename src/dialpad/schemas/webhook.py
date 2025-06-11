from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.signature import SignatureProto


class CreateWebhook(TypedDict):
  """TypedDict representation of the CreateWebhook schema."""

  hook_url: str
  "The webhook's URL. Triggered events will be sent to the url provided here."
  secret: NotRequired[str]
  "[single-line only]\n\nWebhook's signature secret that's used to confirm the validity of the request."


class UpdateWebhook(TypedDict):
  """TypedDict representation of the UpdateWebhook schema."""

  hook_url: NotRequired[str]
  "The webhook's URL. Triggered events will be sent to the url provided here."
  secret: NotRequired[str]
  "[single-line only]\n\nWebhook's signature secret that's used to confirm the validity of the request."


class WebhookProto(TypedDict):
  """Webhook."""

  hook_url: NotRequired[str]
  "The webhook's URL. Triggered events will be sent to the url provided here."
  id: NotRequired[int]
  "The webhook's ID, which is generated after creating a webhook successfully."
  signature: NotRequired[SignatureProto]
  "Webhook's signature containing the secret."


class WebhookCollection(TypedDict):
  """Collection of webhooks."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[WebhookProto]]
  'A list of webhook objects.'
