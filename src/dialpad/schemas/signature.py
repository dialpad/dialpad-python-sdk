from typing_extensions import NotRequired, TypedDict


class SignatureProto(TypedDict):
  """Signature settings."""

  algo: NotRequired[str]
  'The hash algorithm used to compute the signature.'
  secret: NotRequired[str]
  '[single-line only]\n\nThe secret string that will be used to sign the payload.'
  type: NotRequired[str]
  'The signature token type.\n\n(i.e. `jwt`)'
