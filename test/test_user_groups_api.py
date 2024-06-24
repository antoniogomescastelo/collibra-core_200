# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import collibra_core
from collibra_core.api.user_groups_api import UserGroupsApi  # noqa: E501
from collibra_core.rest import ApiException


class TestUserGroupsApi(unittest.TestCase):
    """UserGroupsApi unit test stubs"""

    def setUp(self):
        self.api = UserGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_group(self):
        """Test case for add_user_group

        Add new user group  # noqa: E501
        """
        pass

    def test_add_users_to_user_group(self):
        """Test case for add_users_to_user_group

        Add users to user group  # noqa: E501
        """
        pass

    def test_change_user_group(self):
        """Test case for change_user_group

        Change user group  # noqa: E501
        """
        pass

    def test_find_user_groups(self):
        """Test case for find_user_groups

        Find user groups  # noqa: E501
        """
        pass

    def test_get_user_group(self):
        """Test case for get_user_group

        Get user group  # noqa: E501
        """
        pass

    def test_remove_user_group(self):
        """Test case for remove_user_group

        Remove user group  # noqa: E501
        """
        pass

    def test_remove_users_from_user_group(self):
        """Test case for remove_users_from_user_group

        Remove users from user group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
