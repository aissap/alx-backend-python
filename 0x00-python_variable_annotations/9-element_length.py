#!/usr/bin/env python3

"""Function that determines the length of elements in a list."""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples."""
    return [(i, len(i)) for i in lst]
