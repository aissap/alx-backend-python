#!/usr/bin/env python3

"""Function that sums a list of mixed integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of mixed integers and floats."""
    return sum(mxd_lst)
