#!/usr/bin/env python3
"""takes a list mxd_lst and returns their sum as a float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list function"""
    return sum(mxd_lst)
