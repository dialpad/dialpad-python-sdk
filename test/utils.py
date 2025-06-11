import inspect
import logging
from typing import TypedDict, List, Any, Callable
from faker import Faker

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


def _generate_fake_data(type_hint: Any) -> Any:
  """
  Recursively generates fake data based on the provided type hint.

  Args:
      type_hint: The type annotation for which to generate data.

  Returns:
      Generated fake data corresponding to the type hint.
  """
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

  # Handle typing.List[some_type]
  origin = getattr(type_hint, '__origin__', None)
  args = getattr(type_hint, '__args__', None)

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
  logger.warning(f"WarUnhandled type '{type_hint}'. Returning None.")
  return None
