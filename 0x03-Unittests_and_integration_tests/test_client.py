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

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url method"""
        known_payload = {
                "repos_url": "https://api.github.com/orgs/example/repos"
                }

        with patch.object(GithubOrgClient, 'org', return_value=known_payload):
            github_org_client = GithubOrgClient('example')
            result = github_org_client._public_repos_url
            
            self.assertEqual(result, known_payload["repos_url"])

     @patch('client.get_json')
    @patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=unittest.mock.PropertyMock
    )
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos method"""
        test_url = "http://example.com"
        test_payload = {"payload": True}

        with patch('client.get_json') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            github_org_client = GithubOrgClient('example')
            result = github_org_client.public_repos()

            mock_get.assert_called_once_with("https://api.github.com/orgs/example/repos")

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
