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

class ChangeDomainRequest(object):
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
        'id': 'str',
        'name': 'str',
        'community_id': 'str',
        'type_id': 'str',
        'description': 'str',
        'excluded_from_auto_hyperlinking': 'bool',
        'remove_scope_overlap_on_move': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'community_id': 'communityId',
        'type_id': 'typeId',
        'description': 'description',
        'excluded_from_auto_hyperlinking': 'excludedFromAutoHyperlinking',
        'remove_scope_overlap_on_move': 'removeScopeOverlapOnMove'
    }

    def __init__(self, id=None, name=None, community_id=None, type_id=None, description=None, excluded_from_auto_hyperlinking=None, remove_scope_overlap_on_move=None):  # noqa: E501
        """ChangeDomainRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._community_id = None
        self._type_id = None
        self._description = None
        self._excluded_from_auto_hyperlinking = None
        self._remove_scope_overlap_on_move = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if community_id is not None:
            self.community_id = community_id
        if type_id is not None:
            self.type_id = type_id
        if description is not None:
            self.description = description
        if excluded_from_auto_hyperlinking is not None:
            self.excluded_from_auto_hyperlinking = excluded_from_auto_hyperlinking
        if remove_scope_overlap_on_move is not None:
            self.remove_scope_overlap_on_move = remove_scope_overlap_on_move

    @property
    def id(self):
        """Gets the id of this ChangeDomainRequest.  # noqa: E501

        The ID of the domain to be changed. Silently ignored if the ID is provided as path parameter of the request.  # noqa: E501

        :return: The id of this ChangeDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeDomainRequest.

        The ID of the domain to be changed. Silently ignored if the ID is provided as path parameter of the request.  # noqa: E501

        :param id: The id of this ChangeDomainRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ChangeDomainRequest.  # noqa: E501

        The new name for the domain  # noqa: E501

        :return: The name of this ChangeDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChangeDomainRequest.

        The new name for the domain  # noqa: E501

        :param name: The name of this ChangeDomainRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def community_id(self):
        """Gets the community_id of this ChangeDomainRequest.  # noqa: E501

        The ID of the new community for the domain  # noqa: E501

        :return: The community_id of this ChangeDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._community_id

    @community_id.setter
    def community_id(self, community_id):
        """Sets the community_id of this ChangeDomainRequest.

        The ID of the new community for the domain  # noqa: E501

        :param community_id: The community_id of this ChangeDomainRequest.  # noqa: E501
        :type: str
        """

        self._community_id = community_id

    @property
    def type_id(self):
        """Gets the type_id of this ChangeDomainRequest.  # noqa: E501

        The ID of the new domain type for the domain  # noqa: E501

        :return: The type_id of this ChangeDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ChangeDomainRequest.

        The ID of the new domain type for the domain  # noqa: E501

        :param type_id: The type_id of this ChangeDomainRequest.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

    @property
    def description(self):
        """Gets the description of this ChangeDomainRequest.  # noqa: E501

        The new description for the domain  # noqa: E501

        :return: The description of this ChangeDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeDomainRequest.

        The new description for the domain  # noqa: E501

        :param description: The description of this ChangeDomainRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def excluded_from_auto_hyperlinking(self):
        """Gets the excluded_from_auto_hyperlinking of this ChangeDomainRequest.  # noqa: E501

        Whether the domain should be excluded from hyperlinking or not  # noqa: E501

        :return: The excluded_from_auto_hyperlinking of this ChangeDomainRequest.  # noqa: E501
        :rtype: bool
        """
        return self._excluded_from_auto_hyperlinking

    @excluded_from_auto_hyperlinking.setter
    def excluded_from_auto_hyperlinking(self, excluded_from_auto_hyperlinking):
        """Sets the excluded_from_auto_hyperlinking of this ChangeDomainRequest.

        Whether the domain should be excluded from hyperlinking or not  # noqa: E501

        :param excluded_from_auto_hyperlinking: The excluded_from_auto_hyperlinking of this ChangeDomainRequest.  # noqa: E501
        :type: bool
        """

        self._excluded_from_auto_hyperlinking = excluded_from_auto_hyperlinking

    @property
    def remove_scope_overlap_on_move(self):
        """Gets the remove_scope_overlap_on_move of this ChangeDomainRequest.  # noqa: E501

        Whether scopes assigned to domain should be removed on move if there are any inherited scopes in new community  # noqa: E501

        :return: The remove_scope_overlap_on_move of this ChangeDomainRequest.  # noqa: E501
        :rtype: bool
        """
        return self._remove_scope_overlap_on_move

    @remove_scope_overlap_on_move.setter
    def remove_scope_overlap_on_move(self, remove_scope_overlap_on_move):
        """Sets the remove_scope_overlap_on_move of this ChangeDomainRequest.

        Whether scopes assigned to domain should be removed on move if there are any inherited scopes in new community  # noqa: E501

        :param remove_scope_overlap_on_move: The remove_scope_overlap_on_move of this ChangeDomainRequest.  # noqa: E501
        :type: bool
        """

        self._remove_scope_overlap_on_move = remove_scope_overlap_on_move

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
        if issubclass(ChangeDomainRequest, dict):
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
        if not isinstance(other, ChangeDomainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
