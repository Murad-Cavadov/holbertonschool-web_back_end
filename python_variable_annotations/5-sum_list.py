#!/usr/bin/env python3
"""
This module provides a type-annotated function 'sum_list' that takes
a list of floats as an argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of float numbers and returns their sum.
    """
    return sum(input_list)
