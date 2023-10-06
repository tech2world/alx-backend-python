#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with
the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

expected output:
{'lst': typing.Iterable[typing.Sequence],
'return': typing.List[typing.Tuple[typing.Sequence, int]]}
"""


from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
