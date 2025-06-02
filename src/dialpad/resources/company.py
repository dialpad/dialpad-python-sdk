from .resource import DialpadResource

class CompanyResource(DialpadResource):
  """CompanyResource implements python bindings for the Dialpad API's company endpoints.
  
  See https://developers.dialpad.com/reference#company for additional documentation.
  """
  _resource_path = ['company']

  def get(self):
    """Gets the company resource.

    See Also:
      https://developers.dialpad.com/reference#companyapi_getcompany
    """
    return self.request(method='GET')
