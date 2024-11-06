# Python Dialpad API Client

A python wrapper around the Dialpad REST API

This document describes the installation, usage, and development practices of this python library.
For information about the API itself, head on over to our
[API Documentation](https://developers.dialpad.com/reference) page!


## Installation

Just use everyone's favourite python package installer: `pip`

```bash
pip install python-dialpad
```

## Usage

### The Short Version

TL;DR, this library provides a `DialpadClient` class, which can be instantiated with an API token
and a dialpad URL.

Once a `DialpadClient` object has been constructed, it can be used to call our API endpoints:

```python
from dialpad import DialpadClient

dp_client = DialpadClient(sandbox=True, token='API_TOKEN_HERE')

print(dp_client.user.get(user_id='1234567'))
```

### Client Constructor Arguments

- `token (required)` The API token that will be used to authenticate API requests.
- `sandbox (optional)` If the `sandbox` argument is set to `True`, then API calls will be
  routed to `https://sandbox.dialpad.com`.
- `base_url (optional)` Routes requests to a specific url.


### API Resources

In general, each resource that we support in our public API will be exposed as properties of the
client object. For example, the `User` resource can be accessed using the `user` property (as
demonstrated above).

Each of these resource properties will expose related HTTP methods as methods of that resource
property.

For example, `GET /api/v2/users/{id}` translates to `dp_client.user.get('the_user_id')`.


### API Responses

In cases where our API responds with a single JSON object, the client method will return a Python
dict (as demonstrated above)

In cases where our API responds with a paginated list of many JSON objects, the client method will
return an iterator which will lazily request the next page as the iterator is iterated upon.

```python
from dialpad import DialpadClient

dp_client = DialpadClient(sandbox=True, token='API_TOKEN_HERE')

for user in dp_client.user.list():
  print(user)
```


## Development

### Testing

That's right, the testing section is first in line! Before you start diving in, let's just make sure your environment is set up properly, and that the tests are running buttery-smooth.

Assuming you've already cloned the repository, all you'll need to do is install `tox`, and run the command against the appropriate environment.

* Install the `tox` package.
  ```shell
  $ pip install tox
  ```

* Run the tests
  ```shell
  $ tox
  ```
  Optionaly, you can specify an environment to run the tests against. For eg:
  ```shell
  $ tox -e py3
  ```
That was easy :)

Neato!

### Adding New Resources

Most of the changes to this library will probably just be adding support for additional resources
and endpoints that we expose in the API, so let's start with how to add a new resource.

Each resource exposed by this library should have its own python file under the `dialpad/resources`
directory, and should define a single `class` that inherits from `DialpadResource`.

The class itself should set the `_resource_path` class property to a list of strings such
that `'/api/v2/' + '/'.join(_resource_path)` corresponds to the API path for that resource.

Once the `_resource_path` is defined, the resource class can define instance methods to expose
functionality related to the resource that it represents, and can use the `self.request` helper
method to make authenticated requests to API paths under the `_resource_path`. For example,
if `_resource_path` is set to `['users']`, then calling `self.request(method='POST')` would make
a `POST` request to `/api/v2/users`. (A more precise description of the `request` method is given
in the following section)

With that in mind, most methods that the developer chooses to add to a resource class will probably
just be a very thin method that passes the appropriate arguments into `self.request`, and returns
the result.


#### The `request` Helper Method

`self.request` is a helper method that handles the details of authentication, response parsing, and
pagination, such that the caller only needs to specify the API path, HTTP method, and request data.
The method arguments are as follows:

- `path (optional)` Any additional path elements that should be added after the `_resource_path`
- `method (optional, default: 'GET')` The HTTP method
- `data (optional)` A python dict defining either the query params or the JSON payload, depending on
  which HTTP method is specified
- `headers (optional)` Any additional headers that should be included in the request (the API key
  is automatically included)

If the request succeeds, then `self.request` will either return a python dict, or an iterator of
python dicts, depending on whether the server responds with a pagenated response. Pagenated
responses will be detected automatically, so the caller does not need to worry about it.

If the request fails, then a `requests.HTTPError` exception will be raised, and it'll be up to the
consumer of this library to deal with it 😎


#### The `resources/__init__.py` File

When a new file is added to the `resources` directory, a new import statement should also be added
to `__init__.py` to expose the newly defined resource class as a direct property of the `resources`
module.


#### `DialpadClient` Resource Properties

In addition to adding the new class to the `__init__.py` file, the new resource class should also
be added as a cached property of the `DialpadClient` class.


#### Recap

To add a new resource to this client library, simply:
- Create a new file under the `resources` directory
- Define a new subclass of `DialpadResource` within said file
- Expose methods related to that resource as methods on your new class
- Add a new import statement in `resources/__init__.py`
- Add a new property to the `DialpadClient` class
