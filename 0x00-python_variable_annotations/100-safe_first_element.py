#!/usr/bin/env python3

"""Function that retrieves the first element of a sequence."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst or None."""
    if lst:
        return lst[0]
    else:
        return None
