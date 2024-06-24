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
from collibra_core.models.attribute_type import AttributeType  # noqa: F401,E501

class StringAttributeType(AttributeType):
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
        'string_type': 'str'
    }
    if hasattr(AttributeType, "swagger_types"):
        swagger_types.update(AttributeType.swagger_types)

    attribute_map = {
        'string_type': 'stringType'
    }
    if hasattr(AttributeType, "attribute_map"):
        attribute_map.update(AttributeType.attribute_map)

    def __init__(self, string_type=None, *args, **kwargs):  # noqa: E501
        """StringAttributeType - a model defined in Swagger"""  # noqa: E501
        self._string_type = None
        self.discriminator = None
        if string_type is not None:
            self.string_type = string_type
        AttributeType.__init__(self, *args, **kwargs)

    @property
    def string_type(self):
        """Gets the string_type of this StringAttributeType.  # noqa: E501

        The type of content of the String.  # noqa: E501

        :return: The string_type of this StringAttributeType.  # noqa: E501
        :rtype: str
        """
        return self._string_type

    @string_type.setter
    def string_type(self, string_type):
        """Sets the string_type of this StringAttributeType.

        The type of content of the String.  # noqa: E501

        :param string_type: The string_type of this StringAttributeType.  # noqa: E501
        :type: str
        """
        allowed_values = ["RICH_TEXT", "PLAIN_TEXT"]  # noqa: E501
        if string_type not in allowed_values:
            raise ValueError(
                "Invalid value for `string_type` ({0}), must be one of {1}"  # noqa: E501
                .format(string_type, allowed_values)
            )

        self._string_type = string_type

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
        if issubclass(StringAttributeType, dict):
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
        if not isinstance(other, StringAttributeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
