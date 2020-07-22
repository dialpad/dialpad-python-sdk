from .resource import DialpadResource

class CallbackResource(DialpadResource):
  """CallbackResource implements python bindings for the Dialpad API's callback endpoints.
  
  See https://developers.dialpad.com/reference#callback for additional documentation.
  """
  _resource_path = ['callback']

  def enqueue_callback(self, call_center_id, phone_number):
    """Requests a call-back for the specified number by adding it to the callback queue for the
    specified call center.

    The call back is added to the queue for the call center like a regular call, and a call is
    initiated when the next operator becomes available. This API respects all existing call center
    settings, e.g. business / holiday hours and queue settings. This API currently does not allow
    international call backs. Duplicate call backs for a given number and call center are not
    allowed.

    Args:
      call_center_id (str, required): The ID of the call center for which the callback should be
                                      enqueued.
      phone_number (str, required): The e164-formatted number that should be added to the callback
                                    queue.

    See Also:
      https://developers.dialpad.com/reference#callapi_callback
    """
    return self.request(method='POST', data=dict(call_center_id=call_center_id,
                                                 phone_number=phone_number))
