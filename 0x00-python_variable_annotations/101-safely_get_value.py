#!/usr/bin/env python3

"""Function that retrieves a value from a dictionary."""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value associated with key in dct or default."""
    if key in dct:
        return dct[key]
    else:
        return defaulit
