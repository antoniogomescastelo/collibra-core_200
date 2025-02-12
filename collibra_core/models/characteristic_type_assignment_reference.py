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

class CharacteristicTypeAssignmentReference(object):
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
        'min': 'int',
        'max': 'int',
        'type': 'str',
        'relation_type_direction': 'str',
        'relation_type_restriction': 'str'
    }

    attribute_map = {
        'id': 'id',
        'min': 'min',
        'max': 'max',
        'type': 'type',
        'relation_type_direction': 'relationTypeDirection',
        'relation_type_restriction': 'relationTypeRestriction'
    }

    def __init__(self, id=None, min=None, max=None, type=None, relation_type_direction=None, relation_type_restriction=None):  # noqa: E501
        """CharacteristicTypeAssignmentReference - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._min = None
        self._max = None
        self._type = None
        self._relation_type_direction = None
        self._relation_type_restriction = None
        self.discriminator = None
        self.id = id
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        self.type = type
        if relation_type_direction is not None:
            self.relation_type_direction = relation_type_direction
        if relation_type_restriction is not None:
            self.relation_type_restriction = relation_type_restriction

    @property
    def id(self):
        """Gets the id of this CharacteristicTypeAssignmentReference.  # noqa: E501

        The ID of the reference.  # noqa: E501

        :return: The id of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CharacteristicTypeAssignmentReference.

        The ID of the reference.  # noqa: E501

        :param id: The id of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def min(self):
        """Gets the min of this CharacteristicTypeAssignmentReference.  # noqa: E501

        The minimum allowed.  # noqa: E501

        :return: The min of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this CharacteristicTypeAssignmentReference.

        The minimum allowed.  # noqa: E501

        :param min: The min of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this CharacteristicTypeAssignmentReference.  # noqa: E501

        The maximum allowed, unlimited when null.  # noqa: E501

        :return: The max of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this CharacteristicTypeAssignmentReference.

        The maximum allowed, unlimited when null.  # noqa: E501

        :param max: The max of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def type(self):
        """Gets the type of this CharacteristicTypeAssignmentReference.  # noqa: E501

        The resource type.  # noqa: E501

        :return: The type of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CharacteristicTypeAssignmentReference.

        The resource type.  # noqa: E501

        :param type: The type of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["View", "Asset", "Community", "Domain", "AssetType", "DomainType", "Status", "User", "ClassificationMatch", "UserGroup", "Attribute", "StringAttribute", "ScriptAttribute", "BooleanAttribute", "DateAttribute", "NumericAttribute", "SingleValueListAttribute", "MultiValueListAttribute", "Comment", "Attachment", "Responsibility", "Workflow", "Job", "Relation", "RelationType", "ComplexRelation", "ComplexRelationType", "ArticulationRule", "Assignment", "Scope", "RelationTrace", "ValidationRule", "DataQualityRule", "DataQualityMetric", "Address", "InstantMessagingAccount", "Email", "PhoneNumber", "Website", "Activity", "FormProperty", "WorkflowTask", "ActivityChange", "WorkflowInstance", "Role", "AttributeType", "BooleanAttributeType", "DateAttributeType", "DateTimeAttributeType", "MultiValueListAttributeType", "NumericAttributeType", "ScriptAttributeType", "SingleValueListAttributeType", "StringAttributeType", "ViewSharingRule", "ViewAssignmentRule", "JdbcDriverFile", "JdbcDriver", "JdbcIngestionProperties", "CsvIngestionProperties", "ExcelIngestionProperties", "ConnectionStringParameter", "AssignedCharacteristicType", "Notification", "Tag", "ComplexRelationLegType", "ComplexRelationAttributeType", "ComplexRelationLeg", "BaseDataType", "AdvancedDataType", "DiagramPicture", "DiagramPictureSharingRule", "DiagramPictureAssignmentRule", "Rating", "Classification", "PhysicalDataConnector", "Context"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def relation_type_direction(self):
        """Gets the relation_type_direction of this CharacteristicTypeAssignmentReference.  # noqa: E501

        The relation type direction, if the referenced resource is a relation type; otherwise null.  # noqa: E501

        :return: The relation_type_direction of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_direction

    @relation_type_direction.setter
    def relation_type_direction(self, relation_type_direction):
        """Sets the relation_type_direction of this CharacteristicTypeAssignmentReference.

        The relation type direction, if the referenced resource is a relation type; otherwise null.  # noqa: E501

        :param relation_type_direction: The relation_type_direction of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :type: str
        """
        allowed_values = ["TO_SOURCE", "TO_TARGET", "BOTH", "NONE"]  # noqa: E501
        if relation_type_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `relation_type_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(relation_type_direction, allowed_values)
            )

        self._relation_type_direction = relation_type_direction

    @property
    def relation_type_restriction(self):
        """Gets the relation_type_restriction of this CharacteristicTypeAssignmentReference.  # noqa: E501

        The relation type restriction of the target Asset Type, if the referenced resource is a relation type; otherwise null. When specified, it effectively replaces the source asset type of the relation when relationTypeDirection = TO_SOURCE or the target asset type of the relation when relationTypeDirection = TO_TARGET.You can specify the relation type restriction only when relationTypeDirection is not null. If specified, it must be an ID of a subtype of the source or target asset type, depending on the value of relationTypeDirection.  # noqa: E501

        :return: The relation_type_restriction of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_restriction

    @relation_type_restriction.setter
    def relation_type_restriction(self, relation_type_restriction):
        """Sets the relation_type_restriction of this CharacteristicTypeAssignmentReference.

        The relation type restriction of the target Asset Type, if the referenced resource is a relation type; otherwise null. When specified, it effectively replaces the source asset type of the relation when relationTypeDirection = TO_SOURCE or the target asset type of the relation when relationTypeDirection = TO_TARGET.You can specify the relation type restriction only when relationTypeDirection is not null. If specified, it must be an ID of a subtype of the source or target asset type, depending on the value of relationTypeDirection.  # noqa: E501

        :param relation_type_restriction: The relation_type_restriction of this CharacteristicTypeAssignmentReference.  # noqa: E501
        :type: str
        """

        self._relation_type_restriction = relation_type_restriction

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
        if issubclass(CharacteristicTypeAssignmentReference, dict):
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
        if not isinstance(other, CharacteristicTypeAssignmentReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
