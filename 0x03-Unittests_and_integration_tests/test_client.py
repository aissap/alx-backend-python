#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""
    
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])

    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        mock_get_json.return_value = {"login": org_name}
        github_org_client = GithubOrgClient(org_name)
        org_info = github_org_client.org()
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )
        self.assertEqual(org_info, {"login": org_name})
