#!/usr/bin/env python3
"""
a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """ retuns the sum of iput list as float"""
    return float(sum(input_list))
