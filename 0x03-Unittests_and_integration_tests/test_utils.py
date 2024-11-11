#!/usr/bin/env python3
"""
Func to test_nested_map function access
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    This tests  the funct access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Tests access_nested_map model.
        Args:
            nested_map (Dict): A dictionary with nested dictionaries
            path (List, tuple, set): Keys to acquired needed values in the
                                     nested dictionary
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Tests access_nested_map models for an error when it expects to
        Args:
            nested_map (Dict): A dictionary with nested dictionaries
            path (List, tuple, set): Keys to acquire required value from the
                                     nested dictionary
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests get_json func
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Tests get_json module to receive expected output.
        Args:
            url: url to send http request to
            payload: expected json response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Tests for memoization, memoize
    """
    def test_memoize(self):
        """
        Tests utils.memoize to  work as intended
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
