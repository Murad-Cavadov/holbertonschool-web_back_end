#!/usr/bin/env python3
"""
This module provides a type-annotated function 'element_length'
that calculates the length of elements within an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
