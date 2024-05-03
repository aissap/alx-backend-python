#!/usr/bin/env python3

"""Function to create a tuple from a string and an int/float."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and the square of v."""
    return (k, v ** 2)
