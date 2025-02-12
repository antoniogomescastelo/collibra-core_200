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
from collibra_core.api.jdbc_driver_api import JDBCDriverApi  # noqa: E501
from collibra_core.rest import ApiException


class TestJDBCDriverApi(unittest.TestCase):
    """JDBCDriverApi unit test stubs"""

    def setUp(self):
        self.api = JDBCDriverApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_jdbc_drivers(self):
        """Test case for find_jdbc_drivers

        Find JDBC Drivers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
