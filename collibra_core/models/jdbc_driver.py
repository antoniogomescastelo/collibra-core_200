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

class JdbcDriver(object):
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
        'created_by': 'str',
        'created_on': 'int',
        'last_modified_by': 'str',
        'last_modified_on': 'int',
        'system': 'bool',
        'resource_type': 'str',
        'database_name': 'str',
        'database_version': 'str',
        'driver': 'str',
        'connection_string': 'str',
        'jdbc_driver_files': 'list[JdbcDriverFile]',
        'connection_string_parameters': 'list[ConnectionStringParameter]'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'database_name': 'databaseName',
        'database_version': 'databaseVersion',
        'driver': 'driver',
        'connection_string': 'connectionString',
        'jdbc_driver_files': 'jdbcDriverFiles',
        'connection_string_parameters': 'connectionStringParameters'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, database_name=None, database_version=None, driver=None, connection_string=None, jdbc_driver_files=None, connection_string_parameters=None):  # noqa: E501
        """JdbcDriver - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._database_name = None
        self._database_version = None
        self._driver = None
        self._connection_string = None
        self._jdbc_driver_files = None
        self._connection_string_parameters = None
        self.discriminator = None
        self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if system is not None:
            self.system = system
        self.resource_type = resource_type
        if database_name is not None:
            self.database_name = database_name
        if database_version is not None:
            self.database_version = database_version
        if driver is not None:
            self.driver = driver
        if connection_string is not None:
            self.connection_string = connection_string
        if jdbc_driver_files is not None:
            self.jdbc_driver_files = jdbc_driver_files
        if connection_string_parameters is not None:
            self.connection_string_parameters = connection_string_parameters

    @property
    def id(self):
        """Gets the id of this JdbcDriver.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JdbcDriver.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this JdbcDriver.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this JdbcDriver.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JdbcDriver.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this JdbcDriver.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this JdbcDriver.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this JdbcDriver.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this JdbcDriver.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this JdbcDriver.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this JdbcDriver.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this JdbcDriver.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this JdbcDriver.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this JdbcDriver.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this JdbcDriver.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this JdbcDriver.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this JdbcDriver.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this JdbcDriver.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this JdbcDriver.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this JdbcDriver.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this JdbcDriver.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this JdbcDriver.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this JdbcDriver.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this JdbcDriver.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["View", "Asset", "Community", "Domain", "AssetType", "DomainType", "Status", "User", "ClassificationMatch", "UserGroup", "Attribute", "StringAttribute", "ScriptAttribute", "BooleanAttribute", "DateAttribute", "NumericAttribute", "SingleValueListAttribute", "MultiValueListAttribute", "Comment", "Attachment", "Responsibility", "Workflow", "Job", "Relation", "RelationType", "ComplexRelation", "ComplexRelationType", "ArticulationRule", "Assignment", "Scope", "RelationTrace", "ValidationRule", "DataQualityRule", "DataQualityMetric", "Address", "InstantMessagingAccount", "Email", "PhoneNumber", "Website", "Activity", "FormProperty", "WorkflowTask", "ActivityChange", "WorkflowInstance", "Role", "AttributeType", "BooleanAttributeType", "DateAttributeType", "DateTimeAttributeType", "MultiValueListAttributeType", "NumericAttributeType", "ScriptAttributeType", "SingleValueListAttributeType", "StringAttributeType", "ViewSharingRule", "ViewAssignmentRule", "JdbcDriverFile", "JdbcDriver", "JdbcIngestionProperties", "CsvIngestionProperties", "ExcelIngestionProperties", "ConnectionStringParameter", "AssignedCharacteristicType", "Notification", "Tag", "ComplexRelationLegType", "ComplexRelationAttributeType", "ComplexRelationLeg", "BaseDataType", "AdvancedDataType", "DiagramPicture", "DiagramPictureSharingRule", "DiagramPictureAssignmentRule", "Rating", "Classification", "PhysicalDataConnector", "Context"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def database_name(self):
        """Gets the database_name of this JdbcDriver.  # noqa: E501


        :return: The database_name of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this JdbcDriver.


        :param database_name: The database_name of this JdbcDriver.  # noqa: E501
        :type: str
        """

        self._database_name = database_name

    @property
    def database_version(self):
        """Gets the database_version of this JdbcDriver.  # noqa: E501


        :return: The database_version of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """Sets the database_version of this JdbcDriver.


        :param database_version: The database_version of this JdbcDriver.  # noqa: E501
        :type: str
        """

        self._database_version = database_version

    @property
    def driver(self):
        """Gets the driver of this JdbcDriver.  # noqa: E501


        :return: The driver of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this JdbcDriver.


        :param driver: The driver of this JdbcDriver.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def connection_string(self):
        """Gets the connection_string of this JdbcDriver.  # noqa: E501


        :return: The connection_string of this JdbcDriver.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this JdbcDriver.


        :param connection_string: The connection_string of this JdbcDriver.  # noqa: E501
        :type: str
        """

        self._connection_string = connection_string

    @property
    def jdbc_driver_files(self):
        """Gets the jdbc_driver_files of this JdbcDriver.  # noqa: E501


        :return: The jdbc_driver_files of this JdbcDriver.  # noqa: E501
        :rtype: list[JdbcDriverFile]
        """
        return self._jdbc_driver_files

    @jdbc_driver_files.setter
    def jdbc_driver_files(self, jdbc_driver_files):
        """Sets the jdbc_driver_files of this JdbcDriver.


        :param jdbc_driver_files: The jdbc_driver_files of this JdbcDriver.  # noqa: E501
        :type: list[JdbcDriverFile]
        """

        self._jdbc_driver_files = jdbc_driver_files

    @property
    def connection_string_parameters(self):
        """Gets the connection_string_parameters of this JdbcDriver.  # noqa: E501


        :return: The connection_string_parameters of this JdbcDriver.  # noqa: E501
        :rtype: list[ConnectionStringParameter]
        """
        return self._connection_string_parameters

    @connection_string_parameters.setter
    def connection_string_parameters(self, connection_string_parameters):
        """Sets the connection_string_parameters of this JdbcDriver.


        :param connection_string_parameters: The connection_string_parameters of this JdbcDriver.  # noqa: E501
        :type: list[ConnectionStringParameter]
        """

        self._connection_string_parameters = connection_string_parameters

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
        if issubclass(JdbcDriver, dict):
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
        if not isinstance(other, JdbcDriver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
