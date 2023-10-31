#!/usr/bin/env python3
"""Module for testing the access_nested_map function."""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test the access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test the access_nested_map function for exceptions."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(
            str(context.exception), f"'{path[-1]}'"
        )

class TestGetJson(unittest.TestCase):
    """Test class for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test the get_json function."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
class TestMemoize(unittest.TestCase):
    """Test class for the memoize decorator."""

    class TestClass:
        def __init__(self):
            self.counter = 0

        def a_method(self):
            self.counter += 1
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """Test the memoize decorator."""
        with patch.object(self.TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_instance = self.TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
