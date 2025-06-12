from typing import Literal

from typing_extensions import NotRequired, TypedDict

from dialpad.schemas.webhook import WebhookProto
from dialpad.schemas.websocket import WebsocketProto


class AgentStatusEventSubscriptionProto(TypedDict):
  """Agent-status event subscription."""

  agent_type: Literal['callcenter']
  'The agent type this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the this agent status event subscription is enabled.'
  id: NotRequired[int]
  "The event subscription's ID, which is generated after creating an event subscription successfully."
  webhook: NotRequired[WebhookProto]
  "The webhook's ID, which is generated after creating a webhook successfully."
  websocket: NotRequired[WebsocketProto]
  "The websocket's ID, which is generated after creating a webhook successfully."


class AgentStatusEventSubscriptionCollection(TypedDict):
  """Collection of agent status event subscriptions."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request. Use the cursor provided in the previous response.'
  items: NotRequired[list[AgentStatusEventSubscriptionProto]]
  'A list of SMS event subscriptions.'


class CreateAgentStatusEventSubscription(TypedDict):
  """TypedDict representation of the CreateAgentStatusEventSubscription schema."""

  agent_type: Literal['callcenter']
  'The agent type this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the this agent status event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully."


class UpdateAgentStatusEventSubscription(TypedDict):
  """TypedDict representation of the UpdateAgentStatusEventSubscription schema."""

  agent_type: NotRequired[Literal['callcenter']]
  'The agent type this event subscription subscribes to.'
  enabled: NotRequired[bool]
  'Whether or not the this agent status event subscription is enabled.'
  endpoint_id: NotRequired[int]
  "The logging endpoint's ID, which is generated after creating a webhook or websocket successfully. If you plan to pair this event subscription with another logging endpoint,\nplease provide a valid webhook ID here."
