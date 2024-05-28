#!/usr/bin/env python3
"""test utils"""
import unittest
import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """ test_access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception function"""
        with self.assertRaises(KeyError) as ab:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ab.exception), repr(path[-1]))
