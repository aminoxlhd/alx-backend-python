#!/usr/bin/env python3
"""test utils"""
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception function"""
        with self.assertRaises(KeyError) as ab:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ab.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Testing get_json function"""
    @parameterized.expand([
        ("http://holberton.io", {"payload": False}),
        ("http://example.com", {"payload": True})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test_get_json function"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    class TestClass:
        """TestClass class"""

        def _init_(self):
            """init function"""
            self.calls = 0

        def a_method(self):
            """a_method function"""
            self.calls += 1
            return 42

        @memoize
        def a_property(self):
            """a_property function"""
            return self.a_method()

    def test_memoize(self):
        """test_memoize function"""
        test_instance = self.TestClass()

        with patch.object(self.TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            res1 = test_instance.a_property
            res2 = test_instance.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
