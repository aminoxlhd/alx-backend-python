#!/usr/bin/env python3
"""takes a string k and an int OR float v as arguments and returns a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv function"""
    return (k, v**2)
