from typing import Optional, List, Dict, Union, Literal
from dialpad.resources import DialpadResource
from dialpad.schemas.user import UpdateUserMessage, UserProto


class ApiV2UsersIdResource(DialpadResource):
  """Resource for the path /api/v2/users/{id}"""

  def delete(self, id: str) -> UserProto:
    """User -- Delete

    Deletes a user by id.

    Added on May 11, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)"""
    pass

  def get(self, id: str) -> UserProto:
    """User -- Get

    Gets a user by id.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)"""
    pass

  def patch(self, id: str, request_body: UpdateUserMessage) -> UserProto:
    """User -- Update

    Updates the provided fields for an existing user.

    Added on March 22, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The user's id. ('me' can be used if you are using a user level API key)
        request_body: The request body."""
    pass
