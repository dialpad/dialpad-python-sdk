from dialpad.resources.base import DialpadResource
from dialpad.schemas.sms import SendSMSMessage, SMSProto


class SmsResource(DialpadResource):
  """SmsResource resource class

  Handles API operations for:
  - /api/v2/sms"""

  def send(self, request_body: SendSMSMessage) -> SMSProto:
    """SMS -- Send

    Sends an SMS message to a phone number or to a Dialpad channel on behalf of a user.

    Added on Dec 18, 2019 for API v2.

    Tier 0 Rate limit: 100 per minute.

    Tier 1 Rate limit: 800 per minute.



    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/sms', body=request_body)
