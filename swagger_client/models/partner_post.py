# coding: utf-8

"""
    SMApi

    SecurityMetrics' Application Programming Interface  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@securitymetrics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PartnerPost(object):
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
        'preferred_name': 'str'
    }

    attribute_map = {
        'preferred_name': 'preferred_name'
    }

    def __init__(self, preferred_name=None):  # noqa: E501
        """PartnerPost - a model defined in Swagger"""  # noqa: E501
        self._preferred_name = None
        self.discriminator = None
        if preferred_name is not None:
            self.preferred_name = preferred_name

    @property
    def preferred_name(self):
        """Gets the preferred_name of this PartnerPost.  # noqa: E501

        An optional customer-facing name of the Partner  # noqa: E501

        :return: The preferred_name of this PartnerPost.  # noqa: E501
        :rtype: str
        """
        return self._preferred_name

    @preferred_name.setter
    def preferred_name(self, preferred_name):
        """Sets the preferred_name of this PartnerPost.

        An optional customer-facing name of the Partner  # noqa: E501

        :param preferred_name: The preferred_name of this PartnerPost.  # noqa: E501
        :type: str
        """

        self._preferred_name = preferred_name

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
        if issubclass(PartnerPost, dict):
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
        if not isinstance(other, PartnerPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
