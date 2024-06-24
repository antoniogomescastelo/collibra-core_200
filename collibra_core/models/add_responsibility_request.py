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

class AddResponsibilityRequest(object):
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
        'owner_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'role_id': 'roleId',
        'owner_id': 'ownerId',
        'resource_id': 'resourceId',
        'resource_type': 'resourceType'
    }

    def __init__(self, role_id=None, owner_id=None, resource_id=None, resource_type=None):  # noqa: E501
        """AddResponsibilityRequest - a model defined in Swagger"""  # noqa: E501
        self._role_id = None
        self._owner_id = None
        self._resource_id = None
        self._resource_type = None
        self.discriminator = None
        self.role_id = role_id
        self.owner_id = owner_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def role_id(self):
        """Gets the role_id of this AddResponsibilityRequest.  # noqa: E501

        The ID of the role that should be assigned to user.  # noqa: E501

        :return: The role_id of this AddResponsibilityRequest.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this AddResponsibilityRequest.

        The ID of the role that should be assigned to user.  # noqa: E501

        :param role_id: The role_id of this AddResponsibilityRequest.  # noqa: E501
        :type: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def owner_id(self):
        """Gets the owner_id of this AddResponsibilityRequest.  # noqa: E501

        The ID of the user who the responsibility is created for.  # noqa: E501

        :return: The owner_id of this AddResponsibilityRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this AddResponsibilityRequest.

        The ID of the user who the responsibility is created for.  # noqa: E501

        :param owner_id: The owner_id of this AddResponsibilityRequest.  # noqa: E501
        :type: str
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def resource_id(self):
        """Gets the resource_id of this AddResponsibilityRequest.  # noqa: E501

        The ID of the resource which the responsibility is created for. NOTE: if null, a global responsibility is created.  # noqa: E501

        :return: The resource_id of this AddResponsibilityRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AddResponsibilityRequest.

        The ID of the resource which the responsibility is created for. NOTE: if null, a global responsibility is created.  # noqa: E501

        :param resource_id: The resource_id of this AddResponsibilityRequest.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this AddResponsibilityRequest.  # noqa: E501

        The type of the resource which the responsibility is created for, i.e. [Community, Asset, Domain].  # noqa: E501

        :return: The resource_type of this AddResponsibilityRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AddResponsibilityRequest.

        The type of the resource which the responsibility is created for, i.e. [Community, Asset, Domain].  # noqa: E501

        :param resource_type: The resource_type of this AddResponsibilityRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["View", "Asset", "Community", "Domain", "AssetType", "DomainType", "Status", "User", "ClassificationMatch", "UserGroup", "Attribute", "StringAttribute", "ScriptAttribute", "BooleanAttribute", "DateAttribute", "NumericAttribute", "SingleValueListAttribute", "MultiValueListAttribute", "Comment", "Attachment", "Responsibility", "Workflow", "Job", "Relation", "RelationType", "ComplexRelation", "ComplexRelationType", "ArticulationRule", "Assignment", "Scope", "RelationTrace", "ValidationRule", "DataQualityRule", "DataQualityMetric", "Address", "InstantMessagingAccount", "Email", "PhoneNumber", "Website", "Activity", "FormProperty", "WorkflowTask", "ActivityChange", "WorkflowInstance", "Role", "AttributeType", "BooleanAttributeType", "DateAttributeType", "DateTimeAttributeType", "MultiValueListAttributeType", "NumericAttributeType", "ScriptAttributeType", "SingleValueListAttributeType", "StringAttributeType", "ViewSharingRule", "ViewAssignmentRule", "JdbcDriverFile", "JdbcDriver", "JdbcIngestionProperties", "CsvIngestionProperties", "ExcelIngestionProperties", "ConnectionStringParameter", "AssignedCharacteristicType", "Notification", "Tag", "ComplexRelationLegType", "ComplexRelationAttributeType", "ComplexRelationLeg", "BaseDataType", "AdvancedDataType", "DiagramPicture", "DiagramPictureSharingRule", "DiagramPictureAssignmentRule", "Rating", "Classification", "PhysicalDataConnector", "Context"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

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
        if issubclass(AddResponsibilityRequest, dict):
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
        if not isinstance(other, AddResponsibilityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
