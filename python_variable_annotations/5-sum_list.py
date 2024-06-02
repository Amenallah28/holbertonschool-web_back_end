#!/usr/bin/env python3
"""a type-annotated function sum_list which takes a list 
input_list of floats as argument and returns their sum as a float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of the input_list as a float."""
    sum: float = 0.0
    for numb in input_list:
        sum += numb
    return sum
