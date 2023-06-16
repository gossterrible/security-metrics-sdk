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

class CampaignEmailPut(object):
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
        'start': 'bool'
    }

    attribute_map = {
        'start': 'start'
    }

    def __init__(self, start=None):  # noqa: E501
        """CampaignEmailPut - a model defined in Swagger"""  # noqa: E501
        self._start = None
        self.discriminator = None
        self.start = start

    @property
    def start(self):
        """Gets the start of this CampaignEmailPut.  # noqa: E501

        The pass to activate this Campaign Email Set.  # noqa: E501

        :return: The start of this CampaignEmailPut.  # noqa: E501
        :rtype: bool
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this CampaignEmailPut.

        The pass to activate this Campaign Email Set.  # noqa: E501

        :param start: The start of this CampaignEmailPut.  # noqa: E501
        :type: bool
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

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
        if issubclass(CampaignEmailPut, dict):
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
        if not isinstance(other, CampaignEmailPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
