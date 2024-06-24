# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from collibra_core.models.assigned_characteristic_type import AssignedCharacteristicType  # noqa: F401,E501

class AssignedAttributeType(AssignedCharacteristicType):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'attribute_type': 'AttributeType'
    }
    if hasattr(AssignedCharacteristicType, "swagger_types"):
        swagger_types.update(AssignedCharacteristicType.swagger_types)

    attribute_map = {
        'attribute_type': 'attributeType'
    }
    if hasattr(AssignedCharacteristicType, "attribute_map"):
        attribute_map.update(AssignedCharacteristicType.attribute_map)

    def __init__(self, attribute_type=None, *args, **kwargs):  # noqa: E501
        """AssignedAttributeType - a model defined in Swagger"""  # noqa: E501
        self._attribute_type = None
        self.discriminator = None
        if attribute_type is not None:
            self.attribute_type = attribute_type
        AssignedCharacteristicType.__init__(self, *args, **kwargs)

    @property
    def attribute_type(self):
        """Gets the attribute_type of this AssignedAttributeType.  # noqa: E501


        :return: The attribute_type of this AssignedAttributeType.  # noqa: E501
        :rtype: AttributeType
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this AssignedAttributeType.


        :param attribute_type: The attribute_type of this AssignedAttributeType.  # noqa: E501
        :type: AttributeType
        """

        self._attribute_type = attribute_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AssignedAttributeType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssignedAttributeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
