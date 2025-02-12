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
from collibra_core.api.attribute_types_api import AttributeTypesApi  # noqa: E501
from collibra_core.rest import ApiException


class TestAttributeTypesApi(unittest.TestCase):
    """AttributeTypesApi unit test stubs"""

    def setUp(self):
        self.api = AttributeTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_attribute_type(self):
        """Test case for add_attribute_type

        Adds a new Attribute Type.  # noqa: E501
        """
        pass

    def test_add_attribute_types(self):
        """Test case for add_attribute_types

        Adds multiple Attribute Types.  # noqa: E501
        """
        pass

    def test_change_attribute_type(self):
        """Test case for change_attribute_type

        Changes the attribute types.  # noqa: E501
        """
        pass

    def test_change_attribute_types(self):
        """Test case for change_attribute_types

        Changes multiple attribute types.  # noqa: E501
        """
        pass

    def test_find_attribute_types(self):
        """Test case for find_attribute_types

        Returns attribute types matching the given search criteria.  # noqa: E501
        """
        pass

    def test_get_attribute_type(self):
        """Test case for get_attribute_type

        Returns the attribute type identified by given UUID.  # noqa: E501
        """
        pass

    def test_get_attribute_type_by_name(self):
        """Test case for get_attribute_type_by_name

        Returns the attribute type identified by given name.  # noqa: E501
        """
        pass

    def test_remove_attribute_type(self):
        """Test case for remove_attribute_type

        Removes attribute type identified by given UUID.  # noqa: E501
        """
        pass

    def test_remove_attribute_types(self):
        """Test case for remove_attribute_types

        Removes multiple attribute types.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
