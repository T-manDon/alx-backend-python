#!/usr/bin/env python3
"""A client from github
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A Client from github
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Init methd for the GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Func to memoize the org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """URL for the Public repo"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """The func Memoize for the repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """The public repo"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Static: has_license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
