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

class DataQualityRulePagedResponse(object):
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
        'total': 'int',
        'offset': 'int',
        'limit': 'int',
        'results': 'list[DataQualityRuleImpl]'
    }

    attribute_map = {
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit',
        'results': 'results'
    }

    def __init__(self, total=None, offset=None, limit=None, results=None):  # noqa: E501
        """DataQualityRulePagedResponse - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._offset = None
        self._limit = None
        self._results = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if results is not None:
            self.results = results

    @property
    def total(self):
        """Gets the total of this DataQualityRulePagedResponse.  # noqa: E501

        The total number of results.  # noqa: E501

        :return: The total of this DataQualityRulePagedResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DataQualityRulePagedResponse.

        The total number of results.  # noqa: E501

        :param total: The total of this DataQualityRulePagedResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def offset(self):
        """Gets the offset of this DataQualityRulePagedResponse.  # noqa: E501

        The offset for the results.  # noqa: E501

        :return: The offset of this DataQualityRulePagedResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DataQualityRulePagedResponse.

        The offset for the results.  # noqa: E501

        :param offset: The offset of this DataQualityRulePagedResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this DataQualityRulePagedResponse.  # noqa: E501

        The maximum number of results to be returned.  # noqa: E501

        :return: The limit of this DataQualityRulePagedResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DataQualityRulePagedResponse.

        The maximum number of results to be returned.  # noqa: E501

        :param limit: The limit of this DataQualityRulePagedResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def results(self):
        """Gets the results of this DataQualityRulePagedResponse.  # noqa: E501

        The list of results.  # noqa: E501

        :return: The results of this DataQualityRulePagedResponse.  # noqa: E501
        :rtype: list[DataQualityRuleImpl]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DataQualityRulePagedResponse.

        The list of results.  # noqa: E501

        :param results: The results of this DataQualityRulePagedResponse.  # noqa: E501
        :type: list[DataQualityRuleImpl]
        """

        self._results = results

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
        if issubclass(DataQualityRulePagedResponse, dict):
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
        if not isinstance(other, DataQualityRulePagedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
