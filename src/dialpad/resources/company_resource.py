from typing import Iterator, Literal, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.company import CompanyProto
from dialpad.schemas.sms_opt_out import SmsOptOutEntryProto


class CompanyResource(DialpadResource):
  """CompanyResource resource class

  Handles API operations for:
  - /api/v2/company
  - /api/v2/company/{id}/smsoptout"""

  def get(self) -> CompanyProto:
    """Company -- Get

    Gets company information.

    Added on Feb 21, 2019 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path='/api/v2/company')

  def get_sms_opt_out_list(
    self,
    id: str,
    opt_out_state: Literal['opted_back_in', 'opted_out'],
    a2p_campaign_id: Optional[int] = None,
    cursor: Optional[str] = None,
  ) -> Iterator[SmsOptOutEntryProto]:
    """Company -- Get SMS Opt-out List



    Requires a company admin API key.

    Rate limit: 250 per minute.

    Args:
        id: ID of the requested company. This is required and must be specified in the URL path. The value must match the id from the company linked to the API key.
        a2p_campaign_id: Optional company A2P campaign entity id to filter results by. Note, if set,
    then the parameter 'opt_out_state' must be also set to the value 'opted_out'.
        cursor: Optional token used to return the next page of a previous request. Use the cursor provided in the previous response.
        opt_out_state: Required opt-out state to filter results by. Only results matching this state will be returned.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path=f'/api/v2/company/{id}/smsoptout',
      params={'a2p_campaign_id': a2p_campaign_id, 'cursor': cursor, 'opt_out_state': opt_out_state},
    )
