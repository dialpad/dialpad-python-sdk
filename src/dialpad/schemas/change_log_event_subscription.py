from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.webhook import WebhookProto
from dialpad.schemas.websocket import WebsocketProto


class ChangeLogEventSubscriptionProto(TypedDict):
  """Change log event subscription."""

  enabled: NotRequired[bool]
  'Whether or not the change log event subscription is enabled.'
  id: NotRequired[int]
  "The event subscription's ID, which is generated after creating an event subscription successfully."
  webhook: NotRequired[WebhookProto]
  "The webhook's ID, which is generated after creating a webhook successfully."
  websocket: NotRequired[WebsocketProto]
  "The websocket's ID, which is generated after creating a webhook successfully."


class ChangeLogEventSubscriptionCollection(TypedDict):
  """Collection of change log event subscriptions."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[ChangeLogEventSubscriptionProto]]
  'A list of change log event subscriptions.'


class CreateChangeLogEventSubscription(TypedDict):
  """TypedDict representation of the CreateChangeLogEventSubscription schema."""

  enabled: NotRequired[bool]
  'Whether or not the this change log event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully."


class UpdateChangeLogEventSubscription(TypedDict):
  """TypedDict representation of the UpdateChangeLogEventSubscription schema."""

  enabled: NotRequired[bool]
  'Whether or not the change log event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,\nplease provide a valid webhook ID here."
