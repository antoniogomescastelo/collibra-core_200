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

class ChangeRelationTypeRequest(object):
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
        'public_id': 'str',
        'source_type_id': 'str',
        'role': 'str',
        'target_type_id': 'str',
        'co_role': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'public_id': 'publicId',
        'source_type_id': 'sourceTypeId',
        'role': 'role',
        'target_type_id': 'targetTypeId',
        'co_role': 'coRole',
        'description': 'description'
    }

    def __init__(self, id=None, public_id=None, source_type_id=None, role=None, target_type_id=None, co_role=None, description=None):  # noqa: E501
        """ChangeRelationTypeRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._public_id = None
        self._source_type_id = None
        self._role = None
        self._target_type_id = None
        self._co_role = None
        self._description = None
        self.discriminator = None
        self.id = id
        if public_id is not None:
            self.public_id = public_id
        if source_type_id is not None:
            self.source_type_id = source_type_id
        if role is not None:
            self.role = role
        if target_type_id is not None:
            self.target_type_id = target_type_id
        if co_role is not None:
            self.co_role = co_role
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ChangeRelationTypeRequest.  # noqa: E501

        The ID of the Relation Type to be changed. Silently ignored if the ID is provided as path parameter of the request.  # noqa: E501

        :return: The id of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeRelationTypeRequest.

        The ID of the Relation Type to be changed. Silently ignored if the ID is provided as path parameter of the request.  # noqa: E501

        :param id: The id of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def public_id(self):
        """Gets the public_id of this ChangeRelationTypeRequest.  # noqa: E501

        The new public id for the Relation Type. It must be unique within all Relation Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \"_C\". WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable.  # noqa: E501

        :return: The public_id of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this ChangeRelationTypeRequest.

        The new public id for the Relation Type. It must be unique within all Relation Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \"_C\". WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable.  # noqa: E501

        :param public_id: The public_id of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._public_id = public_id

    @property
    def source_type_id(self):
        """Gets the source_type_id of this ChangeRelationTypeRequest.  # noqa: E501

        The ID of the new source type for the Relation Type.  # noqa: E501

        :return: The source_type_id of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_type_id

    @source_type_id.setter
    def source_type_id(self, source_type_id):
        """Sets the source_type_id of this ChangeRelationTypeRequest.

        The ID of the new source type for the Relation Type.  # noqa: E501

        :param source_type_id: The source_type_id of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._source_type_id = source_type_id

    @property
    def role(self):
        """Gets the role of this ChangeRelationTypeRequest.  # noqa: E501

        The new name of the role that the source plays.  # noqa: E501

        :return: The role of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ChangeRelationTypeRequest.

        The new name of the role that the source plays.  # noqa: E501

        :param role: The role of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def target_type_id(self):
        """Gets the target_type_id of this ChangeRelationTypeRequest.  # noqa: E501

        The ID of the new target type for the Relation Type.  # noqa: E501

        :return: The target_type_id of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_type_id

    @target_type_id.setter
    def target_type_id(self, target_type_id):
        """Sets the target_type_id of this ChangeRelationTypeRequest.

        The ID of the new target type for the Relation Type.  # noqa: E501

        :param target_type_id: The target_type_id of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._target_type_id = target_type_id

    @property
    def co_role(self):
        """Gets the co_role of this ChangeRelationTypeRequest.  # noqa: E501

        The new name of the role that the target plays.  # noqa: E501

        :return: The co_role of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._co_role

    @co_role.setter
    def co_role(self, co_role):
        """Sets the co_role of this ChangeRelationTypeRequest.

        The new name of the role that the target plays.  # noqa: E501

        :param co_role: The co_role of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._co_role = co_role

    @property
    def description(self):
        """Gets the description of this ChangeRelationTypeRequest.  # noqa: E501

        The new description of the Relation Type.  # noqa: E501

        :return: The description of this ChangeRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeRelationTypeRequest.

        The new description of the Relation Type.  # noqa: E501

        :param description: The description of this ChangeRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ChangeRelationTypeRequest, dict):
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
        if not isinstance(other, ChangeRelationTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
