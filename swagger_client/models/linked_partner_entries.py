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

class LinkedPartnerEntries(object):
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
        'links': 'list[Link]',
        'entries': 'list[PartnerWithoutLinks]'
    }

    attribute_map = {
        'links': 'links',
        'entries': 'entries'
    }

    def __init__(self, links=None, entries=None):  # noqa: E501
        """LinkedPartnerEntries - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._entries = None
        self.discriminator = None
        self.links = links
        self.entries = entries

    @property
    def links(self):
        """Gets the links of this LinkedPartnerEntries.  # noqa: E501


        :return: The links of this LinkedPartnerEntries.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LinkedPartnerEntries.


        :param links: The links of this LinkedPartnerEntries.  # noqa: E501
        :type: list[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def entries(self):
        """Gets the entries of this LinkedPartnerEntries.  # noqa: E501


        :return: The entries of this LinkedPartnerEntries.  # noqa: E501
        :rtype: list[PartnerWithoutLinks]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this LinkedPartnerEntries.


        :param entries: The entries of this LinkedPartnerEntries.  # noqa: E501
        :type: list[PartnerWithoutLinks]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

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
        if issubclass(LinkedPartnerEntries, dict):
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
        if not isinstance(other, LinkedPartnerEntries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
