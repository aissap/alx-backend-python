#!/usr/bin/env python3
"""
Unit tests for utils.py
"""
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Testing get_json function"""
    @parameterized.expand([
        ("http://holberton.io", {"payload": False}),
        ("http://example.com", {"payload": True})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected result"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Testing memoize decorator"""

    class TestClass:
        """Testing class with memoized method and property"""

        def __init__(self):
            self.calls = 0

        def a_method(self):
            """Method to be memoized"""
            self.calls += 1
            return 42

        @memoize
        def a_property(self):
            """Memoized property"""
            return self.a_method()

    def test_memoize(self):
        """Test memoize decorator"""
        test_instance = self.TestClass()

        with patch.object(self.TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
