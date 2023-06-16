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

class CustomReportPut(object):
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
        'attach_report': 'bool',
        'created_by': 'str',
        'email_recipients': 'str',
        'format': 'str',
        'frequency': 'str',
        'is_private': 'bool',
        'name': 'str',
        'search_object': 'object',
        'user_recipients': 'list[str]'
    }

    attribute_map = {
        'attach_report': 'attach_report',
        'created_by': 'created_by',
        'email_recipients': 'email_recipients',
        'format': 'format',
        'frequency': 'frequency',
        'is_private': 'is_private',
        'name': 'name',
        'search_object': 'search_object',
        'user_recipients': 'user_recipients'
    }

    def __init__(self, attach_report=None, created_by=None, email_recipients=None, format=None, frequency=None, is_private=None, name=None, search_object=None, user_recipients=None):  # noqa: E501
        """CustomReportPut - a model defined in Swagger"""  # noqa: E501
        self._attach_report = None
        self._created_by = None
        self._email_recipients = None
        self._format = None
        self._frequency = None
        self._is_private = None
        self._name = None
        self._search_object = None
        self._user_recipients = None
        self.discriminator = None
        if attach_report is not None:
            self.attach_report = attach_report
        if created_by is not None:
            self.created_by = created_by
        if email_recipients is not None:
            self.email_recipients = email_recipients
        if format is not None:
            self.format = format
        if frequency is not None:
            self.frequency = frequency
        if is_private is not None:
            self.is_private = is_private
        if name is not None:
            self.name = name
        if search_object is not None:
            self.search_object = search_object
        if user_recipients is not None:
            self.user_recipients = user_recipients

    @property
    def attach_report(self):
        """Gets the attach_report of this CustomReportPut.  # noqa: E501

        if user_recipients get a copy of the report  # noqa: E501

        :return: The attach_report of this CustomReportPut.  # noqa: E501
        :rtype: bool
        """
        return self._attach_report

    @attach_report.setter
    def attach_report(self, attach_report):
        """Sets the attach_report of this CustomReportPut.

        if user_recipients get a copy of the report  # noqa: E501

        :param attach_report: The attach_report of this CustomReportPut.  # noqa: E501
        :type: bool
        """

        self._attach_report = attach_report

    @property
    def created_by(self):
        """Gets the created_by of this CustomReportPut.  # noqa: E501

        The account user username of the creator of this report  # noqa: E501

        :return: The created_by of this CustomReportPut.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CustomReportPut.

        The account user username of the creator of this report  # noqa: E501

        :param created_by: The created_by of this CustomReportPut.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def email_recipients(self):
        """Gets the email_recipients of this CustomReportPut.  # noqa: E501

        the email addresses that get sent this report  # noqa: E501

        :return: The email_recipients of this CustomReportPut.  # noqa: E501
        :rtype: str
        """
        return self._email_recipients

    @email_recipients.setter
    def email_recipients(self, email_recipients):
        """Sets the email_recipients of this CustomReportPut.

        the email addresses that get sent this report  # noqa: E501

        :param email_recipients: The email_recipients of this CustomReportPut.  # noqa: E501
        :type: str
        """

        self._email_recipients = email_recipients

    @property
    def format(self):
        """Gets the format of this CustomReportPut.  # noqa: E501

        the type of file to create  # noqa: E501

        :return: The format of this CustomReportPut.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CustomReportPut.

        the type of file to create  # noqa: E501

        :param format: The format of this CustomReportPut.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def frequency(self):
        """Gets the frequency of this CustomReportPut.  # noqa: E501

        The frequency this custom report will run  # noqa: E501

        :return: The frequency of this CustomReportPut.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this CustomReportPut.

        The frequency this custom report will run  # noqa: E501

        :param frequency: The frequency of this CustomReportPut.  # noqa: E501
        :type: str
        """
        allowed_values = ["now", "monthly", "weekly", "daily"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def is_private(self):
        """Gets the is_private of this CustomReportPut.  # noqa: E501

        private means only the user that created the report can see it  # noqa: E501

        :return: The is_private of this CustomReportPut.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this CustomReportPut.

        private means only the user that created the report can see it  # noqa: E501

        :param is_private: The is_private of this CustomReportPut.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def name(self):
        """Gets the name of this CustomReportPut.  # noqa: E501

        The name of this custom report  # noqa: E501

        :return: The name of this CustomReportPut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomReportPut.

        The name of this custom report  # noqa: E501

        :param name: The name of this CustomReportPut.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def search_object(self):
        """Gets the search_object of this CustomReportPut.  # noqa: E501

        The search object that is run by this custom report  # noqa: E501

        :return: The search_object of this CustomReportPut.  # noqa: E501
        :rtype: object
        """
        return self._search_object

    @search_object.setter
    def search_object(self, search_object):
        """Sets the search_object of this CustomReportPut.

        The search object that is run by this custom report  # noqa: E501

        :param search_object: The search_object of this CustomReportPut.  # noqa: E501
        :type: object
        """

        self._search_object = search_object

    @property
    def user_recipients(self):
        """Gets the user_recipients of this CustomReportPut.  # noqa: E501

        the account_user usernames that share this report  # noqa: E501

        :return: The user_recipients of this CustomReportPut.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_recipients

    @user_recipients.setter
    def user_recipients(self, user_recipients):
        """Sets the user_recipients of this CustomReportPut.

        the account_user usernames that share this report  # noqa: E501

        :param user_recipients: The user_recipients of this CustomReportPut.  # noqa: E501
        :type: list[str]
        """

        self._user_recipients = user_recipients

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
        if issubclass(CustomReportPut, dict):
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
        if not isinstance(other, CustomReportPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
