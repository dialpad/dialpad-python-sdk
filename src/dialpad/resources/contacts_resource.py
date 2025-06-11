from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.contact import (
  ContactProto,
  CreateContactMessage,
  CreateContactMessageWithUid,
  UpdateContactMessage,
)


class ContactsResource(DialpadResource):
  """ContactsResource resource class

  Handles API operations for:
  - /api/v2/contacts
  - /api/v2/contacts/{id}"""

  def create(self, request_body: CreateContactMessage) -> ContactProto:
    """Contact -- Create

    Creates a new contact. Added on Mar 2, 2020 for API v2.

    Rate limit: 100 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/contacts', body=request_body)

  def create_or_update(self, request_body: CreateContactMessageWithUid) -> ContactProto:
    """Contact -- Create or Update

    Creates a new shared contact with uid. Added on Jun 11, 2020 for API v2.

    Rate limit: 100 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PUT', sub_path='/api/v2/contacts', body=request_body)

  def delete(self, id: str) -> ContactProto:
    """Contact -- Delete

    Deletes a contact by id. Added on Mar 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The contact's id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/contacts/{id}')

  def get(self, id: str) -> ContactProto:
    """Contact -- Get

    Gets a contact by id. Currently, only contacts of type shared and local can be retrieved by this API.

    Added on Mar 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The contact's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/contacts/{id}')

  def list(
    self,
    cursor: Optional[str] = None,
    include_local: Optional[bool] = None,
    owner_id: Optional[str] = None,
  ) -> Iterator[ContactProto]:
    """Contact -- List

    Gets company shared contacts, or user's local contacts if owner_id is provided.

    Added on Mar 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        include_local: If set to True company local contacts will be included. default False.
        owner_id: The id of the user who owns the contact.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/contacts',
      params={'cursor': cursor, 'include_local': include_local, 'owner_id': owner_id},
    )

  def partial_update(self, id: str, request_body: UpdateContactMessage) -> ContactProto:
    """Contact -- Update

    Updates the provided fields for an existing contact. Added on Mar 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The contact's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/contacts/{id}', body=request_body)
