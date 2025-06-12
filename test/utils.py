import inspect
import logging
from typing import Annotated, Any, Callable, List, Literal, Union, get_args, get_origin

from faker import Faker
from typing_extensions import NotRequired

fake = Faker()
logger = logging.getLogger(__name__)


def generate_faked_kwargs(func: Callable) -> dict[str, Any]:
  """
  Generates a dictionary of keyword arguments for a given function.

  This function inspects the signature of the input function and uses the Faker
  library to generate mock data for each parameter based on its type annotation.
  It supports standard types, lists, and nested TypedDicts.

  Args:
      func: The function for which to generate kwargs.

  Returns:
      A dictionary of keyword arguments that can be used to call the function.
  """
  kwargs = {}
  signature = inspect.signature(func)
  params = signature.parameters

  for name, param in params.items():
    annotation = param.annotation
    if annotation is not inspect.Parameter.empty:
      kwargs[name] = _generate_fake_data(annotation)
    else:
      # Handle cases where there's no type hint with a default or warning
      print(f"Warning: No type annotation for parameter '{name}'. Skipping.")

  return kwargs


def _is_typed_dict(type_hint: Any) -> bool:
  """Checks if a type hint is a TypedDict."""
  return (
    inspect.isclass(type_hint)
    and issubclass(type_hint, dict)
    and hasattr(type_hint, '__annotations__')
  )


def _unwrap_not_required(type_hint: Any) -> Any:
  """
  Unwraps NotRequired annotations to get the underlying type.

  Args:
      type_hint: The type annotation that might be wrapped in NotRequired.

  Returns:
      The unwrapped type or the original type if not NotRequired.
  """
  origin = get_origin(type_hint)
  if origin is NotRequired:
    args = get_args(type_hint)
    return args[0] if args else type_hint
  return type_hint


def _generate_fake_data(type_hint: Any) -> Any:
  """
  Recursively generates fake data based on the provided type hint.

  Args:
      type_hint: The type annotation for which to generate data.

  Returns:
      Generated fake data corresponding to the type hint.
  """
  # Unwrap NotRequired annotations first
  type_hint = _unwrap_not_required(type_hint)

  # Handle basic types
  if type_hint is int:
    return fake.pyint()
  if type_hint is str:
    return fake.word()
  if type_hint is float:
    return fake.pyfloat()
  if type_hint is bool:
    return fake.boolean()
  if type_hint is list or type_hint is List:
    # Generate a list of 1-5 strings for a generic list
    return [fake.word() for _ in range(fake.pyint(min_value=1, max_value=5))]

  # Handle typing.List[some_type], Literal, Optional, and Union
  origin = get_origin(type_hint) or getattr(type_hint, '__origin__', None)
  args = get_args(type_hint) or getattr(type_hint, '__args__', None)

  if origin is Annotated and args[-1] == 'base64':
    return 'DEADBEEF'  # Placeholder for base64-encoded data

  # Handle Literal types
  if origin is Literal and args:
    return fake.random_element(elements=args)

  # Handle Optional types (which are Union[T, None])
  if origin is Union and args:
    # Filter out NoneType from Union args
    non_none_args = [arg for arg in args if arg is not type(None)]
    if len(non_none_args) == 1:
      # This is Optional[T] - generate data for T with 80% probability
      if fake.boolean(chance_of_getting_true=80):
        return _generate_fake_data(non_none_args[0])
      return None
    # For general Union types, pick a random non-None type
    if non_none_args:
      chosen_type = fake.random_element(elements=non_none_args)
      return _generate_fake_data(chosen_type)

  if origin in (list, List) and args:
    inner_type = args[0]
    # Generate a list of 1-5 elements of the specified inner type
    return [_generate_fake_data(inner_type) for _ in range(fake.pyint(min_value=1, max_value=5))]

  # Handle TypedDict
  if _is_typed_dict(type_hint):
    typed_dict_data = {}
    for field_name, field_type in type_hint.__annotations__.items():
      typed_dict_data[field_name] = _generate_fake_data(field_type)
    return typed_dict_data

  # Fallback for unhandled types
  logger.warning(f"Unhandled type '{type_hint}'. Returning None.")
  return None
