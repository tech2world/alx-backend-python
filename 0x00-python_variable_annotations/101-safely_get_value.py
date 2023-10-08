#!/usr/bin/env python3
"""
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
Here's what the mappings should look like
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]
"""

from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None)-> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
