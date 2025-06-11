from typing import Literal

from typing_extensions import NotRequired, TypedDict


class OptOutScopeInfo(TypedDict):
  """Note, this info should be present for a particular entry in the result set if and only if the given external endpoint is actually opted out (i.e. see OptOutState.opted_out documentation); in other words, this does not apply for results in the 'opted_back_in' state."""

  opt_out_scope_level: Literal['a2p_campaign', 'company']
  'Scope level that the external endpoint is opted out of.'
  scope_id: int
  'Unique ID of the scope entity (Company or A2P Campaign).\n\nNote, this refers to the ID assigned to this entity by Dialpad, as opposed to the TCR-assigned id.'


class SmsOptOutEntryProto(TypedDict):
  """Individual sms-opt-out list entry."""

  date: NotRequired[int]
  'An optional timestamp in (milliseconds-since-epoch UTC format) representing the time at which the given external endpoint transitioned to the opt_out_state.'
  external_endpoint: str
  "An E.164-formatted DID representing the 'external endpoint' used to contact the 'external user'\n."
  opt_out_scope_info: NotRequired[OptOutScopeInfo]
  "Description of the scope of communications that this external endpoint is opted out from.\n\nAs explained in the OptOutScopeInfo documentation, this must be provided if this list entry describes an endpoint that is opted out of some scope (indicated by the value of 'opt_out_state'). If the 'opt_out_state' for this entry is not 'opted_out', then this parameter will be excluded entirely or set to a null value.\n\nFor SMS opt-out-import requests: in the A2P-campaign-scope case, opt_out_scope_info.id must refer to the id of a valid, registered A2P campaign entity owned by this company. In the company-scope case, opt_out_scope_info.id must be set to the company id."
  opt_out_state: Literal['opted_back_in', 'opted_out']
  'Opt-out state for this entry in the list.'


class SmsOptOutListProto(TypedDict):
  """A list of sms-opt-out entries to be returned in the API response."""

  cursor: NotRequired[str]
  'A token that can be used to return the next page of results, if there are any remaining; to fetch the next page, the requester must pass this value as an argument in a new request.'
  items: NotRequired[list[SmsOptOutEntryProto]]
  'List of sms opt-out entries.'
