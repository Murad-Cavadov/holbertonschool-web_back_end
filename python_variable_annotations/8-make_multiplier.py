#!/usr/bin/env python3
"""
This module provides a type-annotated function 'make_multiplier' that
returns a function to multiply a float by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies
    a given float by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a given float by the enclosed multiplier.
        """
        return x * multiplier

    return multiplier_function
