from .resource import DialpadResource

class AppSettingsResource(DialpadResource):
  """AppSettingsResource implements python bindings for the Dialpad API's app-settings
  endpoints.
  
  See https://developers.dialpad.com/reference/appsettingsapi_getappsettings for additional
  documentation.
  """
  _resource_path = ['app', 'settings']

  def get(self, target_id=None, target_type=None):
    """Gets the app settings of the oauth app that is associated with the API key.

    If a target is specified, it will fetch the settings for that target,
    otherwise it will fetch the company-level settings.
  
    Args:
      target_id(int, optional): The target's id.
      target_type(str, optional): The target's type.

    See Also:
      https://developers.dialpad.com/reference/appsettingsapi_getappsettings
    """
    return self.request(method='GET', data=dict(target_id=target_id, target_type=target_type))
