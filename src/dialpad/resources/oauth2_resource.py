from typing import Literal, Optional, Union

from dialpad.resources.base import DialpadResource
from dialpad.schemas.oauth import (
  AuthorizationCodeGrantBodySchema,
  AuthorizeTokenResponseBodySchema,
  RefreshTokenGrantBodySchema,
)


class OAuth2Resource(DialpadResource):
  """OAuth2Resource resource class

  Handles API operations for:
  - /oauth2/authorize
  - /oauth2/deauthorize
  - /oauth2/token"""

  def authorize_token(
    self,
    client_id: str,
    redirect_uri: str,
    code_challenge: Optional[str] = None,
    code_challenge_method: Optional[Literal['S256', 'plain']] = None,
    response_type: Optional[Literal['code']] = None,
    scope: Optional[str] = None,
    state: Optional[str] = None,
  ) -> None:
    """Token -- Authorize

    Initiate the OAuth flow to grant an application access to Dialpad resources on behalf of a user.

    Args:
        client_id: The client_id of the OAuth app.
        code_challenge: PKCE challenge value (hash commitment).
        code_challenge_method: PKCE challenge method (hashing algorithm).
        redirect_uri: The URI the user should be redirected back to after granting consent to the app.
        response_type: The OAuth flow to perform. Must be 'code' (authorization code flow).
        scope: Space-separated list of additional scopes that should be granted to the vended token.
        state: Unpredictable token to prevent CSRF."""
    return self._request(
      method='GET',
      sub_path='/oauth2/authorize',
      params={
        'code_challenge_method': code_challenge_method,
        'code_challenge': code_challenge,
        'scope': scope,
        'response_type': response_type,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'state': state,
      },
    )

  def deauthorize_token(self) -> None:
    """Token -- Deauthorize

    Revokes oauth2 tokens for a given oauth app."""
    return self._request(method='POST', sub_path='/oauth2/deauthorize')

  def redeem_token(
    self, request_body: Union[AuthorizationCodeGrantBodySchema, RefreshTokenGrantBodySchema]
  ) -> AuthorizeTokenResponseBodySchema:
    """Token -- Redeem

    Exchanges a temporary oauth code for an authorized access token.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/oauth2/token', body=request_body)
