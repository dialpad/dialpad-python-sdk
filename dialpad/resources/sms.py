from .resource import DialpadResource

class SMSResource(DialpadResource):
  """SMSResource implements python bindings for the Dialpad API's sms endpoints.
  See https://developers.dialpad.com/reference#sms for additional documentation.
  """
  _resource_path = ['sms']

  def send_sms(self, user_id, to_numbers, text, **kwargs):
    """Sends an SMS message on behalf of the specified user.

    Args:
      user_id (int, required): The ID of the user that should be sending the SMS.
      to_numbers (list<str>, required): A list of one-or-more e164-formatted phone numbers which
                                        should receive the SMS.
      text (str, required): The content of the SMS message.
      infer_country_code (bool, optional): If set, the e164-contraint will be relaxed on to_numbers,
                                           and potentially ambiguous numbers will be assumed to be
                                           numbers in the specified user's country.
      sender_group_id (int, optional): The ID of an office, department, or call center that the user
                                       should send the SMS on behalf of.
      sender_group_type (str, optional): The ID type (i.e. office, department, or callcenter).

    See Also:
      https://developers.dialpad.com/reference#roomapi_listrooms
    """
    return self.request(method='POST', data=dict(text=text, user_id=user_id, to_numbers=to_numbers,
                                                 **kwargs))
