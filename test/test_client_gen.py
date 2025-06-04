#!/usr/bin/env python

"""Tests to verify that the API client generation components are working correctly.
"""

import os

from openapi_core import OpenAPI

from cli.client_gen.annotation import spec_piece_to_annotation


REPO_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPEC_FILE = os.path.join(REPO_ROOT, 'dialpad_api_spec.json')

class TestGenerationUtilities:
  """Tests for the client generation utilities."""

  def test_spec_piece_to_annotation(self):
    """Test the spec_piece_to_annotation function."""
    # Load the OpenAPI specification from the file
    open_api = OpenAPI.from_file_path(SPEC_FILE)

    # Now we'll gather all the possible elements that we expect spec_piece_to_annotation to
    # successfully operate on. This is more of a completeness test than a correctness test,
    # but it should still be useful to ensure that the function can handle all the expected cases.
    elements_to_test = []

    for _path_key, path_schema in (open_api.spec / 'paths').items():
      for _method_key, method_schema in path_schema.items():
        if 'requestBody' in method_schema:
          elements_to_test.append(method_schema / 'requestBody')
          if 'content' in (method_schema / 'requestBody'):
            schema_element = method_schema / 'requestBody' / 'content' / 'application/json' / 'schema'
            if 'properties' in schema_element:
              for _property_key, property_schema in (schema_element / 'properties').items():
                elements_to_test.append(property_schema)

        if 'responses' in method_schema:
          elements_to_test.append(method_schema / 'responses')

        if 'parameters' in method_schema:
          for parameter_schema in (method_schema / 'parameters'):
            elements_to_test.append(parameter_schema)

    # And now we'll go hunting for any bits that break.
    for example_case in elements_to_test:
      try:
        annotation = spec_piece_to_annotation(example_case)
      except Exception as e:
        print(f"Error processing {example_case}: {e}")
        raise
