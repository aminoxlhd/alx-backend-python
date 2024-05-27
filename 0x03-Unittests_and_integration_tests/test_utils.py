#!/usr/bin/env python3
"""test utils"""
import unittest
import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand
    [{"a": 1}, path = ("a",)
    {"a": {"b": 2}}, path = ("a",)
    {"a": {"b": 2}}, path = ("a", "b")]
