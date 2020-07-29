#!/usr/bin/env python

"""Tests to automatically detect common issues with resource definitions.

In particular these tests will look through the files in dialpad-python-sdk/dialpad/resources/ and
ensure:

- All subclasses of DialpadResource are exposed directly in resources/__init__.py
- All resources are available as properties of DialpadClient
- Public methods defined on the concrete subclasses only make web requests that agree with
  the Dialpad API's open-api spec
"""

import inspect
import pkgutil
import pytest
import utils

from swagger_stub import swagger_stub

from dialpad.client import DialpadClient
from dialpad import resources
from dialpad.resources.resource import DialpadResource


# The "swagger_files_url" pytest fixture stubs out live requests with a schema validation check
# against the Dialpad API swagger spec.

# NOTE: Responses returned by the stub will not necessarily be a convincing dummy for the responses
#       returned by the live API, so some complex scenarios may not be possible to test using this
#       strategy.
@pytest.fixture(scope='module')
def swagger_files_url():
  return [
    (utils.resource_filepath('swagger_spec.json'), 'https://dialpad.com'),
  ]


class TestResourceSanity:
  """Sanity-tests for (largely) automatically validating new and existing client API methods.

  When new API resource methods are added to the library, examples of each method must be added to
  EX_METHOD_CALLS to allow the unit tests to call those methods and validate that the API requests
  they generate adhere to the swagger spec.

  The example calls should generally include as many keyword arguments as possible so that any
  potential mistakes in the parameter names, url path, and request body can be caught by the
  schema tests.

  Entries in the "EX_METHOD_CALLS" dictionary should be of the form:
  {
    '<ResourceClassName>': {
      'method_name': {
        'arg_name': arg_value,
        'other_arg_name': other_arg_value,
      },
      'other_method_name': etc... 
    }
  }
  """

  EX_METHOD_CALLS = {
    'BlockedNumberResource': {
      'list': {},
      'block_numbers': {
        'numbers': ['+12223334444']
      },
      'unblock_numbers': {
        'numbers': ['+12223334444']
      },
      'get': {
        'number': '+12223334444'
      },
    },
    'CallResource': {
      'initiate_call': {
        'phone_number': '+12223334444',
        'user_id': '123',
        'group_id': '123',
        'group_type': 'department',
        'device_id': '123',
      },
    },
    'CallRouterResource': {
      'get': {
        'call_router_id': '123',
      },
      'post': {
        'name': 'Test Router',
        'routing_url': 'fakeurl.com/url',
        'office_id': '123',
        'default_target_id': '123',
        'default_target_type': 'user',
        'enabled': True,
        'secret': '123',
      },
      'patch': {
        'call_router_id': '123',
        'name': 'Test Router',
        'routing_url': 'fakeurl.com/url',
        'office_id': '123',
        'default_target_id': '123',
        'default_target_type': 'user',
        'enabled': True,
        'secret': '123',
      },
      'delete': {
        'call_router_id': '123',
      },
      'assign_number': {
        'call_router_id': '123',
        'area_code': '519',
      },
    },
    'CallbackResource': {
      'enqueue_callback': {
        'call_center_id': '123',
        'phone_number': '+12223334444',
      },
    },
    'CallCenterResource': {
      'get': {
        'call_center_id': '123',
      },
      'get_operators': {
        'call_center_id': '123',
      },
    },
    'CompanyResource': {
      'get': {},
    },
    'ContactResource': {
      'list': {
        'owner_id': '123',
      },
      'create': {
        'first_name': 'Testiel',
        'last_name': 'McTestersen',
        'company_name': 'ABC',
        'emails': ['tmtesten@test.com'],
        'extension': '123',
        'job_title': 'Eric the half-a-bee',
        'owner_id': '123',
        'phones': ['+12223334444'],
        'trunk_group': '123',
        'urls': ['test.com/about'],
      },
      'create_with_uid': {
        'first_name': 'Testiel',
        'last_name': 'McTestersen',
        'uid': 'UUID-updownupdownleftrightab',
        'company_name': 'ABC',
        'emails': ['tmtesten@test.com'],
        'extension': '123',
        'job_title': 'Eric the half-a-bee',
        'phones': ['+12223334444'],
        'trunk_group': '123',
        'urls': ['test.com/about'],
      },
      'delete': {
        'contact_id': '123',
      },
      'get': {
        'contact_id': '123',
      },
      'patch': {
        'contact_id': '123',
        'first_name': 'Testiel',
        'last_name': 'McTestersen',
        'company_name': 'ABC',
        'emails': ['tmtesten@test.com'],
        'extension': '123',
        'job_title': 'Eric the half-a-bee',
        'phones': ['+12223334444'],
        'trunk_group': '123',
        'urls': ['test.com/about'],
      },
    },
    'DepartmentResource': {
      'get': {
        'department_id': '123',
      },
      'get_operators': {
        'department_id': '123',
      },
    },
    'EventSubscriptionResource': {
      'list_call_event_subscriptions': {
        'target_id': '123',
        'target_type': 'room',
      },
      'get_call_event_subscription': {
        'subscription_id': '123',
      },
      'put_call_event_subscription': {
        'subscription_id': '123',
        'url': 'test.com/subhook',
        'secret': 'badsecret',
        'enabled': True,
        'group_calls_only': False,
        'target_id': '123',
        'target_type': 'office',
        'call_states': ['connected', 'queued'],
      },
      'delete_call_event_subscription': {
        'subscription_id': '123',
      },
      'list_sms_event_subscriptions': {
        'target_id': '123',
        'target_type': 'room',
      },
      'get_sms_event_subscription': {
        'subscription_id': '123',
      },
      'put_sms_event_subscription': {
        'subscription_id': '123',
        'url': 'test.com/subhook',
        'secret': 'badsecret',
        'direction': 'outbound',
        'enabled': True,
        'target_id': '123',
        'target_type': 'office',
      },
      'delete_sms_event_subscription': {
        'subscription_id': '123',
      },
    },
    'NumberResource': {
      'list': {
        'status': 'available',
      },
      'get': {
        'number': '+12223334444',
      },
      'unassign': {
        'number': '+12223334444',
      },
      'assign': {
        'number': '+12223334444',
        'target_id': '123',
        'target_type': 'office',
      },
    },
    'OfficeResource': {
      'list': {},
      'get': {
        'office_id': '123',
      },
      'assign_number': {
        'office_id': '123',
        'number': '+12223334444',
      },
      'get_operators': {
        'office_id': '123',
      },
      'unassign_number': {
        'office_id': '123',
        'number': '+12223334444',
      },
      'get_call_centers': {
        'office_id': '123',
      },
      'get_departments': {
        'office_id': '123',
      },
      'get_plan': {
        'office_id': '123',
      },
      'update_licenses': {
        'office_id': '123',
        'fax_line_delta': '2',
      },
    },
    'RoomResource': {
      'list': {
        'office_id': '123',
      },
      'create': {
        'name': 'Where it happened',
        'office_id': '123',
      },
      'generate_international_pin': {
        'customer_ref': 'Burr, sir',
      },
      'delete': {
        'room_id': '123',
      },
      'get': {
        'room_id': '123',
      },
      'update': {
        'room_id': '123',
        'name': 'For the last tiiiime',
        'phone_numbers': ['+12223334444'],
      },
      'assign_number': {
        'room_id': '123',
        'number': '+12223334444',
      },
      'unassign_number': {
        'room_id': '123',
        'number': '+12223334444',
      },
      'get_deskphones': {
        'room_id': '123',
      },
      'create_deskphone': {
        'room_id': '123',
        'mac_address': 'Tim Cook',
        'name': 'The red one.',
        'phone_type': 'polycom',
      },
      'delete_deskphone': {
        'room_id': '123',
        'deskphone_id': '123',
      },
      'get_deskphone': {
        'room_id': '123',
        'deskphone_id': '123',
      },
    },
    'SMSResource': {
      'send_sms': {
        'user_id': '123',
        'to_numbers': ['+12223334444'],
        'text': 'Itemized list to follow.',
        'infer_country_code': False,
        'sender_group_id': '123',
        'sender_group_type': 'callcenter',
      },
    },
    'StatsExportResource': {
      'post': {
        'coaching_group': False,
        'days_ago_start': '1',
        'days_ago_end': '2',
        'is_today': False,
        'export_type': 'records',
        'stat_type': 'calls',
        'office_id': '123',
        'target_id': '123',
        'target_type': 'callcenter',
        'timezone': 'America/New_York',
      },
      'get': {
        'export_id': '123',
      },
    },
    'TranscriptResource': {
      'get': {
        'call_id': '123',
      },
    },
    'UserResource': {
      'list': {
        'email': 'tmtesten@test.com',
        'state': 'suspended',
      },
      'create': {
        'email': 'tmtesten@test.com',
        'office_id': '123',
        'first_name': 'Testietta',
        'last_name': 'McTestersen',
        'license': 'lite_support_agents',
      },
      'delete': {
        'user_id': '123',
      },
      'get': {
        'user_id': '123',
      },
      'update': {
        'user_id': '123',
        'admin_office_ids': ['123'],
        'emails': ['tmtesten@test.com'],
        'extension': '123',
        'first_name': 'Testietta',
        'last_name': 'McTestersen',
        'forwarding_numbers': ['+12223334444'],
        'is_super_admin': True,
        'job_title': 'Administraterar',
        'license': 'lite_lines',
        'office_id': '123',
        'phone_numbers': ['+12223334444'],
        'state': 'active',
      },
      'toggle_call_recording': {
        'user_id': '123',
        'is_recording': False,
        'play_message': True,
        'recording_type': 'group',
      },
      'assign_number': {
        'user_id': '123',
        'number': '+12223334444',
      },
      'initiate_call': {
        'user_id': '123',
        'phone_number': '+12223334444',
        'custom_data': 'Y u call self?',
        'group_id': '123',
        'group_type': 'department',
        'outbound_caller_id': 'O.0',
      },
      'unassign_number': {
        'user_id': '123',
        'number': '+12223334444',
      },
      'get_deskphones': {
        'user_id': '123',
      },
      'create_deskphone': {
        'user_id': '123',
        'mac_address': 'Tim Cook',
        'name': 'The red one.',
        'phone_type': 'polycom',
      },
      'delete_deskphone': {
        'user_id': '123',
        'deskphone_id': '123',
      },
      'get_deskphone': {
        'user_id': '123',
        'deskphone_id': '123',
      },
    },
    'UserDeviceResource': {
      'get': {
        'device_id': '123',
      },
      'list': {
        'user_id': '123',
      },
    },
  }

  def get_method_example_kwargs(self, resource_instance, resource_method):
    """Returns the appropriate kwargs to use when sanity-checking API resource methods."""
    class_msg = 'DialpadResource subclass "%s" must have an entry in EX_METHOD_CALLS'

    class_name = resource_instance.__class__.__name__
    assert class_name in self.EX_METHOD_CALLS, class_msg % class_name

    method_msg = 'Method "%s.%s" must have an entry in EX_METHOD_CALLS'
    method_name = resource_method.__name__
    assert method_name in self.EX_METHOD_CALLS[class_name], method_msg % (class_name, method_name)

    return self.EX_METHOD_CALLS[class_name][method_name]

  def _get_resource_submodule_names(self):
    """Returns an iterator of python modules that exist in the dialpad/resources directory."""
    for importer, modname, ispkg in pkgutil.iter_modules(resources.__path__):
      if modname == 'resource':
        continue

      if ispkg:
        continue

      yield modname

  def _get_resource_submodules(self):
    """Returns an iterator of python modules that are exposed via from dialpad.resources import *"""
    for modname in self._get_resource_submodule_names():
      if hasattr(resources, modname):
        yield getattr(resources, modname)

  def _get_resource_classes(self):
    """Returns an iterator of DialpadResource subclasses that are exposed under dialpad.resources"""
    for mod in self._get_resource_submodules():
      for k, v in mod.__dict__.iteritems():
        if not inspect.isclass(v):
          continue

        if not issubclass(v, DialpadResource):
          continue

        if v == DialpadResource:
          continue

        yield v

  def test_resources_properly_imported(self):
    """Verifies that all modules definied in the resources directory are properly exposed under
    dialpad.resources.
    """
    exposed_resources = dir(resources)

    msg = '"%s" module is present in the resources directory, but is not imported in ' \
          'resources/__init__.py'

    for modname in self._get_resource_submodule_names():
      assert modname in exposed_resources, msg % modname

  def test_resource_classes_properly_exposed(self):
    """Verifies that all subclasses of DialpadResource that are defined in the resources directory
    are also exposed as direct members of the resources module.
    """
    exposed_resources = dir(resources)

    msg = '"%(name)s" resource class is present in the resources package, but is not exposed ' \
          'directly as resources.%(name)s via resources/__init__.py'

    for c in self._get_resource_classes():
      assert c.__name__ in exposed_resources, msg % {'name': c.__name__}

  def test_request_conformance(self, swagger_stub):
    """Verifies that all API requests produced by this library conform to the swagger spec.

    Although this test cannot guarantee that the requests are semantically correct, it can at least
    determine whether they are schematically correct.

    This test will also fail if there are no test-kwargs defined in EX_METHOD_CALLS for any public
    method implemented by a subclass of DialpadResource.
    """

    # Construct a DialpadClient with a fake API key.
    dp = DialpadClient('123')

    # Iterate through the attributes on the client object to find the API resource accessors.
    for a in dir(dp):
      resource_instance = getattr(dp, a)

      # Skip any attributes that are not DialpadResources
      if not isinstance(resource_instance, DialpadResource):
        continue

      print ''
      print 'Verifying request format of %s methods' % resource_instance.__class__.__name__

      # Iterate through the attributes on the resource instance.
      for method_attr in dir(resource_instance):
        # Skip private attributes.
        if method_attr.startswith('_'):
          continue

        # Skip attributes that are not unique to this particular subclass of DialpadResource.
        if hasattr(DialpadResource, method_attr):
          continue

        # Skip attributes that are not functions.
        resource_method = getattr(resource_instance, method_attr)
        if not callable(resource_method):
          continue

        # Skip attributes that are not instance methods.
        arg_names = inspect.getargspec(resource_method).args
        if not arg_names or arg_names[0] != 'self':
          continue

        # Fetch example kwargs to test the method (and raise if they haven't been provided).
        method_kwargs = self.get_method_example_kwargs(resource_instance, resource_method)

        # Call the method, and allow the swagger mock to raise an exception if it encounters a
        # schema error.
        print 'Testing %s with kwargs: %s' % (method_attr, method_kwargs)
        resource_method(**method_kwargs)
