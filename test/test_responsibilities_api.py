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
from collibra_core.api.responsibilities_api import ResponsibilitiesApi  # noqa: E501
from collibra_core.rest import ApiException


class TestResponsibilitiesApi(unittest.TestCase):
    """ResponsibilitiesApi unit test stubs"""

    def setUp(self):
        self.api = ResponsibilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_responsibilities(self):
        """Test case for add_responsibilities

        Adds multiple responsibilities in one go.  # noqa: E501
        """
        pass

    def test_add_responsibility(self):
        """Test case for add_responsibility

        Adds a new responsibility.  # noqa: E501
        """
        pass

    def test_find_responsibilities(self):
        """Test case for find_responsibilities

        Finds responsibilities.  # noqa: E501
        """
        pass

    def test_get_responsibility(self):
        """Test case for get_responsibility

        Returns the responsibility identified by the given id.  # noqa: E501
        """
        pass

    def test_remove_responsibilities(self):
        """Test case for remove_responsibilities

        Removes multiple responsibilities in one go.  # noqa: E501
        """
        pass

    def test_remove_responsibility(self):
        """Test case for remove_responsibility

        Removes the responsibility identified by the given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
