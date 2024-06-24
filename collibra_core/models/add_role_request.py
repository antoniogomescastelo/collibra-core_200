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

class AddRoleRequest(object):
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
        '_global': 'bool',
        'description': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        '_global': 'global',
        'description': 'description',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, name=None, _global=None, description=None, permissions=None):  # noqa: E501
        """AddRoleRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self.__global = None
        self._description = None
        self._permissions = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if _global is not None:
            self._global = _global
        if description is not None:
            self.description = description
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this AddRoleRequest.  # noqa: E501

        The ID of the new role. Should be unique within all roles<br/><p><br/>It should have a format of universally unique identifier (UUID) and should not start<br/>with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :return: The id of this AddRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddRoleRequest.

        The ID of the new role. Should be unique within all roles<br/><p><br/>It should have a format of universally unique identifier (UUID) and should not start<br/>with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :param id: The id of this AddRoleRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AddRoleRequest.  # noqa: E501

        The name of the new role. Should be unique within all roles.  # noqa: E501

        :return: The name of this AddRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddRoleRequest.

        The name of the new role. Should be unique within all roles.  # noqa: E501

        :param name: The name of this AddRoleRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def _global(self):
        """Gets the _global of this AddRoleRequest.  # noqa: E501

        Whether the role should be a global or resource role.  # noqa: E501

        :return: The _global of this AddRoleRequest.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this AddRoleRequest.

        Whether the role should be a global or resource role.  # noqa: E501

        :param _global: The _global of this AddRoleRequest.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def description(self):
        """Gets the description of this AddRoleRequest.  # noqa: E501

        The description of the role.  # noqa: E501

        :return: The description of this AddRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddRoleRequest.

        The description of the role.  # noqa: E501

        :param description: The description of this AddRoleRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """Gets the permissions of this AddRoleRequest.  # noqa: E501

        The permissions to be granted for this role.  # noqa: E501

        :return: The permissions of this AddRoleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AddRoleRequest.

        The permissions to be granted for this role.  # noqa: E501

        :param permissions: The permissions of this AddRoleRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["EDGE", "EDGE_SITE_CONNECT", "EDGE_SITE_MANAGE", "EDGE_SITE_ADMINISTER", "EDGE_INTEGRATION_CAPABILITY_MANAGE", "EDGE_VIEW_CONNECTIONS_AND_CAPABILITIES", "EDGE_VIEW_LOGS", "ASSET_GRID_ADMINISTRATION", "ATTACHMENT_ADD", "ATTACHMENT_CHANGE", "ATTACHMENT_REMOVE", "COMMENT_ADD", "COMMENT_CHANGE", "COMMENT_REMOVE", "RATING_ADD", "RATING_CHANGE", "RATING_REMOVE", "RESOURCE_EXPORT", "RESOURCE_IMPORT", "COMMUNITY_ADD", "COMMUNITY_CHANGE", "COMMUNITY_REMOVE", "COMMUNITY_CONFIGURE_EXTERNAL_SYSTEM", "COMMUNITY_RESPONSIBILITY_ADD", "COMMUNITY_RESPONSIBILITY_CHANGE", "COMMUNITY_RESPONSIBILITY_REMOVE", "DOMAIN_ADD", "DOMAIN_CHANGE", "DOMAIN_REMOVE", "DOMAIN_RESPONSIBILITY_ADD", "DOMAIN_RESPONSIBILITY_CHANGE", "DOMAIN_RESPONSIBILITY_REMOVE", "WORKFLOW_MANAGE", "WORKFLOW_DESIGNER_ACCESS", "ASSET_ADD", "ASSET_CHANGE", "ASSET_REMOVE", "ASSET_STATUS_CHANGE", "ASSET_TYPE_CHANGE", "ASSET_TAG_CHANGE", "ASSET_ATTRIBUTE_ADD", "ASSET_ATTRIBUTE_CHANGE", "ASSET_ATTRIBUTE_REMOVE", "ASSET_RESPONSIBILITY_ADD", "ASSET_RESPONSIBILITY_CHANGE", "ASSET_RESPONSIBILITY_REMOVE", "VIEW_PERMISSIONS_CHANGE", "BUSINESS_SEMANTICS_GLOSSARY", "REFERENCE_DATA_MANAGER", "DATA_STEWARDSHIP_MANAGER", "SYSTEM_ADMINISTRATION", "USER_ADMINISTRATION", "WORKFLOW_ADMINISTRATION", "DATA_HELPDESK", "POLICY_MANAGER", "DATA_DICTIONARY", "CATALOG", "WORKFLOW_MANAGE_ALL", "WORKFLOW_MESSAGE_EVENTS_USE", "VIEW_PERMISSIONS_VIEW_ALL", "VIEW_MANAGE", "VIEW_SHARE", "VIEW_MANAGE_ALL", "DATA_CLASSES_READ", "DATA_CLASSES_ADD", "DATA_CLASSES_EDIT", "DATA_CLASSES_REMOVE", "DATA_CLASSES_LIST_VALUES", "ADVANCED_DATA_TYPE_ADD", "ADVANCED_DATA_TYPE_EDIT", "ADVANCED_DATA_TYPE_REMOVE", "TAGS_VIEW", "TAGS_MANAGE", "VALIDATION_EXECUTION", "ACCESS_DATA", "VIEW_SAMPLES", "RELATION_TYPE_ADD", "RELATION_TYPE_REMOVE", "RELATION_TYPE_CHANGE", "REGISTER_PROFILING_INFORMATION", "REPORTING_DOWNLOAD_INSIGHTS_DATA", "REPORTING_VIEW_INSIGHTS_REPORTS", "INSIGHTS_VIEW", "INSIGHTS_SUMMARY", "TECHNICAL_LINEAGE", "LOGS_VIEW", "RESOURCE_MANAGE_ALL", "CONFIGURATION_VIEW", "CONFIGURATION_EDIT", "BACKSTORE_VIEW", "BACKSTORE_EDIT", "ASSESSMENTS", "ASSESSMENTS_ADMINISTRATION", "ASSESSMENTS_CONDUCT_ASSESSMENTS", "ASSESSMENTS_MANAGE_TEMPLATES", "METADATA_LAKE", "PROTECT", "PROTECT_EDIT", "PROTECT_ADMINISTRATION", "AI_GOVERNANCE", "PRIVACY", "DATA_MARKETPLACE", "CLASSIFY", "WORKFLOW_START", "WORKFLOW_PARTICIPATION", "DATA_NOTEBOOK", "DATA_NOTEBOOK_MANAGE_DATA_SOURCES", "DATA_NOTEBOOK_MANAGE_SETTINGS", "DATA_NOTEBOOK_MANAGE_ALL_NOTEBOOKS", "VIEW_NOTEBOOK", "GUIDED_STEWARDSHIP", "DATA_QUALITY"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

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
        if issubclass(AddRoleRequest, dict):
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
        if not isinstance(other, AddRoleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
