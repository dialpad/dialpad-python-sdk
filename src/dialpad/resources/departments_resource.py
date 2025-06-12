from typing import Iterator, Optional

from dialpad.resources.base import DialpadResource
from dialpad.schemas.group import (
  AddOperatorMessage,
  CreateDepartmentMessage,
  DepartmentProto,
  OperatorCollection,
  RemoveOperatorMessage,
  UpdateDepartmentMessage,
  UserOrRoomProto,
)


class DepartmentsResource(DialpadResource):
  """DepartmentsResource resource class

  Handles API operations for:
  - /api/v2/departments
  - /api/v2/departments/{id}
  - /api/v2/departments/{id}/operators"""

  def add_operator(self, id: int, request_body: AddOperatorMessage) -> UserOrRoomProto:
    """Operator -- Add

    Adds an operator to a department.

    Added on October 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The department's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='POST', sub_path=f'/api/v2/departments/{id}/operators', body=request_body
    )

  def create(self, request_body: CreateDepartmentMessage) -> DepartmentProto:
    """Departments-- Create

    Creates a new department.

    Added on March 25th, 2022 for API v2.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='POST', sub_path='/api/v2/departments', body=request_body)

  def delete(self, id: int) -> DepartmentProto:
    """Departments-- Delete

    Deletes a department by id.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The department's id.

    Returns:
        A successful response"""
    return self._request(method='DELETE', sub_path=f'/api/v2/departments/{id}')

  def get(self, id: int) -> DepartmentProto:
    """Department -- Get

    Gets a department by id. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The department's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/departments/{id}')

  def list(
    self,
    cursor: Optional[str] = None,
    name_search: Optional[str] = None,
    office_id: Optional[int] = None,
  ) -> Iterator[DepartmentProto]:
    """Department -- List

    Gets all the departments in the company. Added on Feb 3rd, 2022 for API v2.

    Rate limit: 1200 per minute.

    Args:
        cursor: A token used to return the next page of a previous request. Use the cursor provided in the previous response.
        name_search: search departments by name or search by the substring of the name. If input example is 'Happy', output example can be a list of departments whose name contains the string Happy - ['Happy department 1', 'Happy department 2']
        office_id: filter departments by office.

    Returns:
        An iterator of items from A successful response"""
    return self._iter_request(
      method='GET',
      sub_path='/api/v2/departments',
      params={'cursor': cursor, 'office_id': office_id, 'name_search': name_search},
    )

  def list_operators(self, id: int) -> OperatorCollection:
    """Operator -- List

    Gets operators for a department. Added on May 1, 2018 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The department's id.

    Returns:
        A successful response"""
    return self._request(method='GET', sub_path=f'/api/v2/departments/{id}/operators')

  def partial_update(self, id: int, request_body: UpdateDepartmentMessage) -> DepartmentProto:
    """Departments-- Update

    Updates a new department.

    Requires a company admin API key.

    Rate limit: 1200 per minute.

    Args:
        id: The call center's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(method='PATCH', sub_path=f'/api/v2/departments/{id}', body=request_body)

  def remove_operator(self, id: int, request_body: RemoveOperatorMessage) -> UserOrRoomProto:
    """Operator -- Remove

    Removes an operator from a department.

    Added on October 2, 2020 for API v2.

    Rate limit: 1200 per minute.

    Args:
        id: The department's id.
        request_body: The request body.

    Returns:
        A successful response"""
    return self._request(
      method='DELETE', sub_path=f'/api/v2/departments/{id}/operators', body=request_body
    )
