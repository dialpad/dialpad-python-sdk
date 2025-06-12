from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.webhook import WebhookProto
from dialpad.schemas.websocket import WebsocketProto


class ContactEventSubscriptionProto(TypedDict):
  """Contact event subscription."""

  contact_type: NotRequired[Literal['local', 'shared']]
  'The contact type this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the contact event subscription is enabled.'
  id: NotRequired[int]
  'The ID of the contact event subscription object.'
  webhook: NotRequired[WebhookProto]
  "The webhook's ID, which is generated after creating a webhook successfully."
  websocket: NotRequired[WebsocketProto]
  "The websocket's ID, which is generated after creating a webhook successfully."


class ContactEventSubscriptionCollection(TypedDict):
  """Collection of contact event subscriptions."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[ContactEventSubscriptionProto]]
  'A list event subscriptions.'


class CreateContactEventSubscription(TypedDict):
  """TypedDict representation of the CreateContactEventSubscription schema."""

  contact_type: Literal['local', 'shared']
  'The contact type this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the contact event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully."


class UpdateContactEventSubscription(TypedDict):
  """TypedDict representation of the UpdateContactEventSubscription schema."""

  contact_type: Literal['local', 'shared']
  'The contact type this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the contact event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,\nplease provide a valid webhook ID here."
