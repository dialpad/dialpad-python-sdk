from typing import Literal

from typing_extensions import NotRequired, TypedDict


class AuthorizationCodeGrantBodySchema(TypedDict):
  """Used to redeem an access token via authorization code."""

  client_id: NotRequired[str]
  'The client_id of the oauth app.\n\nNote: must either be provided in the request body, or in a basic authorization header.'
  client_secret: NotRequired[str]
  'The client_secret of the oauth app.\n\nNote: must either be provided in the request body, or in a basic authorization header.'
  code: str
  'The authorization code that resulted from the oauth2 authorization redirect.'
  code_verifier: NotRequired[str]
  'The PKCE code verifier corresponding to the initial PKCE code challenge, if applicable.'
  grant_type: Literal['authorization_code']
  'The type of OAuth grant which is being requested.'


class AuthorizeTokenResponseBodySchema(TypedDict):
  """TypedDict representation of the AuthorizeTokenResponseBodySchema schema."""

  access_token: NotRequired[str]
  'A static access token.'
  expires_in: NotRequired[int]
  'The number of seconds after which the access token will become expired.'
  id_token: NotRequired[str]
  'User ID token (if using OpenID Connect)'
  refresh_token: NotRequired[str]
  'The refresh token that can be used to obtain a new token pair when this one expires.'
  token_type: NotRequired[str]
  'The type of the access_token being issued.'


class RefreshTokenGrantBodySchema(TypedDict):
  """Used to exchange a refresh token for a short-lived access token and another refresh token."""

  client_id: NotRequired[str]
  'The client_id of the oauth app.\n\nNote: must either be provided in the request body, or in a basic authorization header.'
  client_secret: NotRequired[str]
  'The client_secret of the oauth app.\n\nNote: must either be provided in the request body, or in a basic authorization header.'
  grant_type: Literal['refresh_token']
  'The type of OAuth grant which is being requested.'
  refresh_token: str
  'The current refresh token which is being traded in for a new token pair.'
