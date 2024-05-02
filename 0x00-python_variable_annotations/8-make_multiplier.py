#!/usr/bin/env python3
"""takes a float and returns a function that multiplies a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function"""

    def multiplier_function(m: float) -> float:
        """multiplier_function"""
        return multiplier * m

    return multiplier_function
