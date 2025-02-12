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

class WorkflowInstance(object):
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
        'workflow_definition': 'WorkflowDefinitionReference',
        'sub_instances': 'list[WorkflowInstance]',
        'sub_process_instances_count': 'int',
        'parent_workflow_instance_id': 'str',
        'business_item': 'ResourceReference',
        'tasks': 'list[WorkflowTask]',
        'start_date': 'int',
        'ended': 'bool',
        'created_asset_id': 'str',
        'in_error': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'workflow_definition': 'workflowDefinition',
        'sub_instances': 'subInstances',
        'sub_process_instances_count': 'subProcessInstancesCount',
        'parent_workflow_instance_id': 'parentWorkflowInstanceId',
        'business_item': 'businessItem',
        'tasks': 'tasks',
        'start_date': 'startDate',
        'ended': 'ended',
        'created_asset_id': 'createdAssetId',
        'in_error': 'inError',
        'error_message': 'errorMessage'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, workflow_definition=None, sub_instances=None, sub_process_instances_count=None, parent_workflow_instance_id=None, business_item=None, tasks=None, start_date=None, ended=None, created_asset_id=None, in_error=None, error_message=None):  # noqa: E501
        """WorkflowInstance - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._workflow_definition = None
        self._sub_instances = None
        self._sub_process_instances_count = None
        self._parent_workflow_instance_id = None
        self._business_item = None
        self._tasks = None
        self._start_date = None
        self._ended = None
        self._created_asset_id = None
        self._in_error = None
        self._error_message = None
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
        if workflow_definition is not None:
            self.workflow_definition = workflow_definition
        if sub_instances is not None:
            self.sub_instances = sub_instances
        if sub_process_instances_count is not None:
            self.sub_process_instances_count = sub_process_instances_count
        if parent_workflow_instance_id is not None:
            self.parent_workflow_instance_id = parent_workflow_instance_id
        if business_item is not None:
            self.business_item = business_item
        if tasks is not None:
            self.tasks = tasks
        if start_date is not None:
            self.start_date = start_date
        if ended is not None:
            self.ended = ended
        if created_asset_id is not None:
            self.created_asset_id = created_asset_id
        if in_error is not None:
            self.in_error = in_error
        if error_message is not None:
            self.error_message = error_message

    @property
    def id(self):
        """Gets the id of this WorkflowInstance.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowInstance.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this WorkflowInstance.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowInstance.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowInstance.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this WorkflowInstance.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this WorkflowInstance.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this WorkflowInstance.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this WorkflowInstance.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this WorkflowInstance.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this WorkflowInstance.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this WorkflowInstance.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this WorkflowInstance.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this WorkflowInstance.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this WorkflowInstance.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this WorkflowInstance.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this WorkflowInstance.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this WorkflowInstance.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this WorkflowInstance.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this WorkflowInstance.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this WorkflowInstance.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this WorkflowInstance.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this WorkflowInstance.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this WorkflowInstance.  # noqa: E501
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
    def workflow_definition(self):
        """Gets the workflow_definition of this WorkflowInstance.  # noqa: E501


        :return: The workflow_definition of this WorkflowInstance.  # noqa: E501
        :rtype: WorkflowDefinitionReference
        """
        return self._workflow_definition

    @workflow_definition.setter
    def workflow_definition(self, workflow_definition):
        """Sets the workflow_definition of this WorkflowInstance.


        :param workflow_definition: The workflow_definition of this WorkflowInstance.  # noqa: E501
        :type: WorkflowDefinitionReference
        """

        self._workflow_definition = workflow_definition

    @property
    def sub_instances(self):
        """Gets the sub_instances of this WorkflowInstance.  # noqa: E501

        The sub process instances of this instance.  # noqa: E501

        :return: The sub_instances of this WorkflowInstance.  # noqa: E501
        :rtype: list[WorkflowInstance]
        """
        return self._sub_instances

    @sub_instances.setter
    def sub_instances(self, sub_instances):
        """Sets the sub_instances of this WorkflowInstance.

        The sub process instances of this instance.  # noqa: E501

        :param sub_instances: The sub_instances of this WorkflowInstance.  # noqa: E501
        :type: list[WorkflowInstance]
        """

        self._sub_instances = sub_instances

    @property
    def sub_process_instances_count(self):
        """Gets the sub_process_instances_count of this WorkflowInstance.  # noqa: E501

        The count of sub process instances of this instance.  # noqa: E501

        :return: The sub_process_instances_count of this WorkflowInstance.  # noqa: E501
        :rtype: int
        """
        return self._sub_process_instances_count

    @sub_process_instances_count.setter
    def sub_process_instances_count(self, sub_process_instances_count):
        """Sets the sub_process_instances_count of this WorkflowInstance.

        The count of sub process instances of this instance.  # noqa: E501

        :param sub_process_instances_count: The sub_process_instances_count of this WorkflowInstance.  # noqa: E501
        :type: int
        """

        self._sub_process_instances_count = sub_process_instances_count

    @property
    def parent_workflow_instance_id(self):
        """Gets the parent_workflow_instance_id of this WorkflowInstance.  # noqa: E501

        The Id of the parent workflow instance.  # noqa: E501

        :return: The parent_workflow_instance_id of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._parent_workflow_instance_id

    @parent_workflow_instance_id.setter
    def parent_workflow_instance_id(self, parent_workflow_instance_id):
        """Sets the parent_workflow_instance_id of this WorkflowInstance.

        The Id of the parent workflow instance.  # noqa: E501

        :param parent_workflow_instance_id: The parent_workflow_instance_id of this WorkflowInstance.  # noqa: E501
        :type: str
        """

        self._parent_workflow_instance_id = parent_workflow_instance_id

    @property
    def business_item(self):
        """Gets the business_item of this WorkflowInstance.  # noqa: E501


        :return: The business_item of this WorkflowInstance.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._business_item

    @business_item.setter
    def business_item(self, business_item):
        """Sets the business_item of this WorkflowInstance.


        :param business_item: The business_item of this WorkflowInstance.  # noqa: E501
        :type: ResourceReference
        """

        self._business_item = business_item

    @property
    def tasks(self):
        """Gets the tasks of this WorkflowInstance.  # noqa: E501

        The list of workflow tasks in this process instance.  # noqa: E501

        :return: The tasks of this WorkflowInstance.  # noqa: E501
        :rtype: list[WorkflowTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this WorkflowInstance.

        The list of workflow tasks in this process instance.  # noqa: E501

        :param tasks: The tasks of this WorkflowInstance.  # noqa: E501
        :type: list[WorkflowTask]
        """

        self._tasks = tasks

    @property
    def start_date(self):
        """Gets the start_date of this WorkflowInstance.  # noqa: E501

        The start date of this process instance.  # noqa: E501

        :return: The start_date of this WorkflowInstance.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this WorkflowInstance.

        The start date of this process instance.  # noqa: E501

        :param start_date: The start_date of this WorkflowInstance.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def ended(self):
        """Gets the ended of this WorkflowInstance.  # noqa: E501

        Whether this process instance is already ended.  # noqa: E501

        :return: The ended of this WorkflowInstance.  # noqa: E501
        :rtype: bool
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this WorkflowInstance.

        Whether this process instance is already ended.  # noqa: E501

        :param ended: The ended of this WorkflowInstance.  # noqa: E501
        :type: bool
        """

        self._ended = ended

    @property
    def created_asset_id(self):
        """Gets the created_asset_id of this WorkflowInstance.  # noqa: E501

        The optional identifier of the created asset if the process instance ended, created a term and it is configured for it.  # noqa: E501

        :return: The created_asset_id of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._created_asset_id

    @created_asset_id.setter
    def created_asset_id(self, created_asset_id):
        """Sets the created_asset_id of this WorkflowInstance.

        The optional identifier of the created asset if the process instance ended, created a term and it is configured for it.  # noqa: E501

        :param created_asset_id: The created_asset_id of this WorkflowInstance.  # noqa: E501
        :type: str
        """

        self._created_asset_id = created_asset_id

    @property
    def in_error(self):
        """Gets the in_error of this WorkflowInstance.  # noqa: E501

        Whether this process instance is in error. This means that there was a problem with a async continuation of the process instance.  # noqa: E501

        :return: The in_error of this WorkflowInstance.  # noqa: E501
        :rtype: bool
        """
        return self._in_error

    @in_error.setter
    def in_error(self, in_error):
        """Sets the in_error of this WorkflowInstance.

        Whether this process instance is in error. This means that there was a problem with a async continuation of the process instance.  # noqa: E501

        :param in_error: The in_error of this WorkflowInstance.  # noqa: E501
        :type: bool
        """

        self._in_error = in_error

    @property
    def error_message(self):
        """Gets the error_message of this WorkflowInstance.  # noqa: E501

        The optional error message of any error in a async continuation of this process instance. Only present if inError is true.  # noqa: E501

        :return: The error_message of this WorkflowInstance.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this WorkflowInstance.

        The optional error message of any error in a async continuation of this process instance. Only present if inError is true.  # noqa: E501

        :param error_message: The error_message of this WorkflowInstance.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(WorkflowInstance, dict):
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
        if not isinstance(other, WorkflowInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
