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

class SetAssetTagsRequest(object):
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
        'tag_names': 'list[str]'
    }

    attribute_map = {
        'tag_names': 'tagNames'
    }

    def __init__(self, tag_names=None):  # noqa: E501
        """SetAssetTagsRequest - a model defined in Swagger"""  # noqa: E501
        self._tag_names = None
        self.discriminator = None
        self.tag_names = tag_names

    @property
    def tag_names(self):
        """Gets the tag_names of this SetAssetTagsRequest.  # noqa: E501

        The names of the tags to be applied on given asset.  # noqa: E501

        :return: The tag_names of this SetAssetTagsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this SetAssetTagsRequest.

        The names of the tags to be applied on given asset.  # noqa: E501

        :param tag_names: The tag_names of this SetAssetTagsRequest.  # noqa: E501
        :type: list[str]
        """
        if tag_names is None:
            raise ValueError("Invalid value for `tag_names`, must not be `None`")  # noqa: E501

        self._tag_names = tag_names

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
        if issubclass(SetAssetTagsRequest, dict):
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
        if not isinstance(other, SetAssetTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
