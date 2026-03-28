from dialpad.resources.base import DialpadResource
from dialpad.schemas.oauth_app import ToggleOAuthAppMessage, ToggleOAuthAppProto


class OAuthAppsResource(DialpadResource):
  """OAuthAppsResource resource class

  Handles API operations for:
  - /api/v2/oauth_apps/{id}/toggle"""

  def toggle(
    self,
    id: str,
    request_body: ToggleOAuthAppMessage,
  ) -> ToggleOAuthAppProto:
    """OAuth app -- Toggle

    Enables or disables an OAuth App for a given target or the API key's target.

    Added on September 13th, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The OAuth App's ID (client_id).
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='PATCH', sub_path=f'/api/v2/oauth_apps/{id}/toggle', body=request_body
    )
