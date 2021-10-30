import json
import os
import requests


RESOURCE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '.resources')


def resource_filepath(filename):
  """Returns a path to the given file name in the test resources directory."""
  return os.path.join(RESOURCE_PATH, filename)


def prepare_test_resources():
  """Prepares any resources that are expected to be available at test-time."""

  if not os.path.exists(RESOURCE_PATH):
    os.mkdir(RESOURCE_PATH)

  # Generate the Dialpad API swagger spec, and write it to a file for easy access.
  with open(resource_filepath('swagger_spec.json'), 'w') as f:
    json.dump(_generate_swagger_spec(), f)


def _generate_swagger_spec():
  """Downloads current Dialpad API swagger spec and returns it as a dict."""

  # Unfortunately, a little bit of massaging is needed to appease the swagger parser.
  def _hotpatch_spec_piece(piece):
    if 'type' in piece:
      if piece['type'] == 'string' and piece.get('format') == 'int64' and 'default' in piece:
        piece['default'] = str(piece['default'])

      if 'operationId' in piece and 'parameters' in piece:
        for sub_p in piece['parameters']:
          sub_p['required'] = sub_p.get('required', False)

    if 'basePath' in piece:
      del piece['basePath']

  def _hotpatch_spec(spec):
    if isinstance(spec, dict):
      _hotpatch_spec_piece(spec)
      for k, v in spec.items():
        _hotpatch_spec(v)

    elif isinstance(spec, list):
      for v in spec:
        _hotpatch_spec(v)

    return spec

  # Download the spec from dialpad.com.
  spec_json = requests.get('https://dialpad.com/static/openapi/apiv2openapi-en.json').json()

  # Return a patched version that will satisfy the swagger lib.
  return _hotpatch_spec(spec_json)
