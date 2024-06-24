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

class ChangeRatingRequest(object):
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
        'rating': 'float',
        'review': 'str'
    }

    attribute_map = {
        'rating': 'rating',
        'review': 'review'
    }

    def __init__(self, rating=None, review=None):  # noqa: E501
        """ChangeRatingRequest - a model defined in Swagger"""  # noqa: E501
        self._rating = None
        self._review = None
        self.discriminator = None
        self.rating = rating
        if review is not None:
            self.review = review

    @property
    def rating(self):
        """Gets the rating of this ChangeRatingRequest.  # noqa: E501

        The value of the rating represented as a floating point number between 0 and 1.  # noqa: E501

        :return: The rating of this ChangeRatingRequest.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this ChangeRatingRequest.

        The value of the rating represented as a floating point number between 0 and 1.  # noqa: E501

        :param rating: The rating of this ChangeRatingRequest.  # noqa: E501
        :type: float
        """
        if rating is None:
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501

        self._rating = rating

    @property
    def review(self):
        """Gets the review of this ChangeRatingRequest.  # noqa: E501

        The review attached to the rating.  # noqa: E501

        :return: The review of this ChangeRatingRequest.  # noqa: E501
        :rtype: str
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this ChangeRatingRequest.

        The review attached to the rating.  # noqa: E501

        :param review: The review of this ChangeRatingRequest.  # noqa: E501
        :type: str
        """

        self._review = review

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
        if issubclass(ChangeRatingRequest, dict):
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
        if not isinstance(other, ChangeRatingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
