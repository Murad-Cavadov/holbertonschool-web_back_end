#!/usr/bin/env python3
"""
This module provides a type-annotated function 'floor' that
takes a float argument and returns its floor as an integer.
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a given float number.
    """
    return math.floor(n)
