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

class SetAssetResponsibilitiesRequest(object):
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
        'role_id': 'str',
        'owner_ids': 'list[str]'
    }

    attribute_map = {
        'role_id': 'roleId',
        'owner_ids': 'ownerIds'
    }

    def __init__(self, role_id=None, owner_ids=None):  # noqa: E501
        """SetAssetResponsibilitiesRequest - a model defined in Swagger"""  # noqa: E501
        self._role_id = None
        self._owner_ids = None
        self.discriminator = None
        self.role_id = role_id
        self.owner_ids = owner_ids

    @property
    def role_id(self):
        """Gets the role_id of this SetAssetResponsibilitiesRequest.  # noqa: E501

        The ID of the role for the responsibilities to be set.  # noqa: E501

        :return: The role_id of this SetAssetResponsibilitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this SetAssetResponsibilitiesRequest.

        The ID of the role for the responsibilities to be set.  # noqa: E501

        :param role_id: The role_id of this SetAssetResponsibilitiesRequest.  # noqa: E501
        :type: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def owner_ids(self):
        """Gets the owner_ids of this SetAssetResponsibilitiesRequest.  # noqa: E501

        The IDs of the owners. An owner is either user or group.  # noqa: E501

        :return: The owner_ids of this SetAssetResponsibilitiesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this SetAssetResponsibilitiesRequest.

        The IDs of the owners. An owner is either user or group.  # noqa: E501

        :param owner_ids: The owner_ids of this SetAssetResponsibilitiesRequest.  # noqa: E501
        :type: list[str]
        """
        if owner_ids is None:
            raise ValueError("Invalid value for `owner_ids`, must not be `None`")  # noqa: E501

        self._owner_ids = owner_ids

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
        if issubclass(SetAssetResponsibilitiesRequest, dict):
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
        if not isinstance(other, SetAssetResponsibilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
