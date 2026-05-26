
#!/usr/bin/env python3
"""
This module provides a type-annotated function 'sum_mixed_list' that
takes a list of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a mixed list of integers and floats and returns their sum.
    """
    return float(sum(mxd_lst))
