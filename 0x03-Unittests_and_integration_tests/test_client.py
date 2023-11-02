#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test class for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient."""
        test_client = GithubOrgClient(org_name)

        test_client.org()

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property of GithubOrgClient."""
        test_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
        mock_org.return_value = test_payload

        test_client = GithubOrgClient("test")
        result = test_client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])


    @patch('client.GithubOrgClient._public_repos_url', new_callable=
           unittest.mock.PropertyMock)
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """Test the public_repos method of GithubOrgClient."""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"

        test_client = GithubOrgClient("test")
        result = test_client.public_repos()

        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")
        mock_public_repos_url.assert_called_once()
        self.assertEqual(result, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test the has_license method of GithubOrgClient."""
        test_client = GithubOrgClient("test")
        result = test_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


@parameterized.class_setup(*[(org_payload, repos_payload, expected_repos, apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def mock_get(url):
            if url == 'https://api.github.com/orgs/google':
                return MockResponse(cls.org_payload, 200)
            elif url == 'https://api.github.com/orgs/google/repos':
                return MockResponse(cls.repos_payload, 200)
            else:
                return MockResponse(None, 404)

        cls.mock_get.side_effect = mock_get

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
