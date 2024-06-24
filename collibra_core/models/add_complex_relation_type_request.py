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

class AddComplexRelationTypeRequest(object):
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
        'name': 'str',
        'description': 'str',
        'color': 'str',
        'symbol_type': 'str',
        'icon_code': 'str',
        'acronym_code': 'str',
        'attribute_types': 'list[ComplexRelationAttributeTypeRequest]',
        'leg_types': 'list[ComplexRelationLegTypeRequest]'
    }

    attribute_map = {
        'id': 'id',
        'public_id': 'publicId',
        'name': 'name',
        'description': 'description',
        'color': 'color',
        'symbol_type': 'symbolType',
        'icon_code': 'iconCode',
        'acronym_code': 'acronymCode',
        'attribute_types': 'attributeTypes',
        'leg_types': 'legTypes'
    }

    def __init__(self, id=None, public_id=None, name=None, description=None, color=None, symbol_type=None, icon_code=None, acronym_code=None, attribute_types=None, leg_types=None):  # noqa: E501
        """AddComplexRelationTypeRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._public_id = None
        self._name = None
        self._description = None
        self._color = None
        self._symbol_type = None
        self._icon_code = None
        self._acronym_code = None
        self._attribute_types = None
        self._leg_types = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if public_id is not None:
            self.public_id = public_id
        self.name = name
        if description is not None:
            self.description = description
        if color is not None:
            self.color = color
        self.symbol_type = symbol_type
        if icon_code is not None:
            self.icon_code = icon_code
        if acronym_code is not None:
            self.acronym_code = acronym_code
        self.attribute_types = attribute_types
        self.leg_types = leg_types

    @property
    def id(self):
        """Gets the id of this AddComplexRelationTypeRequest.  # noqa: E501

        The ID of the new Complex Relation Type. Should be unique within all Complex Relation Types.<br/>It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :return: The id of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddComplexRelationTypeRequest.

        The ID of the new Complex Relation Type. Should be unique within all Complex Relation Types.<br/>It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :param id: The id of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def public_id(self):
        """Gets the public_id of this AddComplexRelationTypeRequest.  # noqa: E501

        The public id that will be assigned to the new Complex Relation Type. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \"_C\". If no public id is provided, a valid public id will be generated.  # noqa: E501

        :return: The public_id of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this AddComplexRelationTypeRequest.

        The public id that will be assigned to the new Complex Relation Type. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \"_C\". If no public id is provided, a valid public id will be generated.  # noqa: E501

        :param public_id: The public_id of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._public_id = public_id

    @property
    def name(self):
        """Gets the name of this AddComplexRelationTypeRequest.  # noqa: E501

        The name of the new Complex Relation Type. Should be unique within all Complex Relation Types.  # noqa: E501

        :return: The name of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddComplexRelationTypeRequest.

        The name of the new Complex Relation Type. Should be unique within all Complex Relation Types.  # noqa: E501

        :param name: The name of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this AddComplexRelationTypeRequest.  # noqa: E501

        The description of the new Complex Relation Type.  # noqa: E501

        :return: The description of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddComplexRelationTypeRequest.

        The description of the new Complex Relation Type.  # noqa: E501

        :param description: The description of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def color(self):
        """Gets the color of this AddComplexRelationTypeRequest.  # noqa: E501

        The color of the symbol, in a hex format e.g. '#000000'.  This format always includes the '#' and has a size of 7.  # noqa: E501

        :return: The color of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AddComplexRelationTypeRequest.

        The color of the symbol, in a hex format e.g. '#000000'.  This format always includes the '#' and has a size of 7.  # noqa: E501

        :param color: The color of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def symbol_type(self):
        """Gets the symbol_type of this AddComplexRelationTypeRequest.  # noqa: E501

        The symbol type.  # noqa: E501

        :return: The symbol_type of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._symbol_type

    @symbol_type.setter
    def symbol_type(self, symbol_type):
        """Sets the symbol_type of this AddComplexRelationTypeRequest.

        The symbol type.  # noqa: E501

        :param symbol_type: The symbol_type of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if symbol_type is None:
            raise ValueError("Invalid value for `symbol_type`, must not be `None`")  # noqa: E501
        allowed_values = ["NONE", "ICON_CODE", "ACRONYM_CODE"]  # noqa: E501
        if symbol_type not in allowed_values:
            raise ValueError(
                "Invalid value for `symbol_type` ({0}), must be one of {1}"  # noqa: E501
                .format(symbol_type, allowed_values)
            )

        self._symbol_type = symbol_type

    @property
    def icon_code(self):
        """Gets the icon_code of this AddComplexRelationTypeRequest.  # noqa: E501

        The icon code of the new Complex Relation Type.  # noqa: E501

        :return: The icon_code of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._icon_code

    @icon_code.setter
    def icon_code(self, icon_code):
        """Sets the icon_code of this AddComplexRelationTypeRequest.

        The icon code of the new Complex Relation Type.  # noqa: E501

        :param icon_code: The icon_code of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._icon_code = icon_code

    @property
    def acronym_code(self):
        """Gets the acronym_code of this AddComplexRelationTypeRequest.  # noqa: E501

        The acronym code of the new Complex Relation Type.  # noqa: E501

        :return: The acronym_code of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._acronym_code

    @acronym_code.setter
    def acronym_code(self, acronym_code):
        """Sets the acronym_code of this AddComplexRelationTypeRequest.

        The acronym code of the new Complex Relation Type.  # noqa: E501

        :param acronym_code: The acronym_code of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._acronym_code = acronym_code

    @property
    def attribute_types(self):
        """Gets the attribute_types of this AddComplexRelationTypeRequest.  # noqa: E501

        The list of attribute types for the new Complex Relation Type.  # noqa: E501

        :return: The attribute_types of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: list[ComplexRelationAttributeTypeRequest]
        """
        return self._attribute_types

    @attribute_types.setter
    def attribute_types(self, attribute_types):
        """Sets the attribute_types of this AddComplexRelationTypeRequest.

        The list of attribute types for the new Complex Relation Type.  # noqa: E501

        :param attribute_types: The attribute_types of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: list[ComplexRelationAttributeTypeRequest]
        """
        if attribute_types is None:
            raise ValueError("Invalid value for `attribute_types`, must not be `None`")  # noqa: E501

        self._attribute_types = attribute_types

    @property
    def leg_types(self):
        """Gets the leg_types of this AddComplexRelationTypeRequest.  # noqa: E501

        The list of leg types for the new Complex Relation Type.  # noqa: E501

        :return: The leg_types of this AddComplexRelationTypeRequest.  # noqa: E501
        :rtype: list[ComplexRelationLegTypeRequest]
        """
        return self._leg_types

    @leg_types.setter
    def leg_types(self, leg_types):
        """Sets the leg_types of this AddComplexRelationTypeRequest.

        The list of leg types for the new Complex Relation Type.  # noqa: E501

        :param leg_types: The leg_types of this AddComplexRelationTypeRequest.  # noqa: E501
        :type: list[ComplexRelationLegTypeRequest]
        """
        if leg_types is None:
            raise ValueError("Invalid value for `leg_types`, must not be `None`")  # noqa: E501

        self._leg_types = leg_types

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
        if issubclass(AddComplexRelationTypeRequest, dict):
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
        if not isinstance(other, AddComplexRelationTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
