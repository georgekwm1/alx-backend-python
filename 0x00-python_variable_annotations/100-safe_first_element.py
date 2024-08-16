#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Optional, Union, Sequence, Any, TypeVar

T = TypeVar('T', bound=Union[Any, None])


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
