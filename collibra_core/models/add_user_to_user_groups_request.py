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

class AddUserToUserGroupsRequest(object):
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
        'user_id': 'str',
        'user_group_ids': 'list[str]'
    }

    attribute_map = {
        'user_id': 'userId',
        'user_group_ids': 'userGroupIds'
    }

    def __init__(self, user_id=None, user_group_ids=None):  # noqa: E501
        """AddUserToUserGroupsRequest - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._user_group_ids = None
        self.discriminator = None
        self.user_id = user_id
        self.user_group_ids = user_group_ids

    @property
    def user_id(self):
        """Gets the user_id of this AddUserToUserGroupsRequest.  # noqa: E501

        The ID of the user who should be assigned to user groups.  Silently ignored if the ID is provided as path parameter of the request  # noqa: E501

        :return: The user_id of this AddUserToUserGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AddUserToUserGroupsRequest.

        The ID of the user who should be assigned to user groups.  Silently ignored if the ID is provided as path parameter of the request  # noqa: E501

        :param user_id: The user_id of this AddUserToUserGroupsRequest.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this AddUserToUserGroupsRequest.  # noqa: E501

        The list of IDs of the user groups which the user should be assigned to  # noqa: E501

        :return: The user_group_ids of this AddUserToUserGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this AddUserToUserGroupsRequest.

        The list of IDs of the user groups which the user should be assigned to  # noqa: E501

        :param user_group_ids: The user_group_ids of this AddUserToUserGroupsRequest.  # noqa: E501
        :type: list[str]
        """
        if user_group_ids is None:
            raise ValueError("Invalid value for `user_group_ids`, must not be `None`")  # noqa: E501

        self._user_group_ids = user_group_ids

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
        if issubclass(AddUserToUserGroupsRequest, dict):
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
        if not isinstance(other, AddUserToUserGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
