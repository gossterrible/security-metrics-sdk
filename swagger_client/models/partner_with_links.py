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

class PartnerWithLinks(object):
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
        'auto_emails': 'bool',
        'date_created': 'date',
        'disable_mcc_export': 'bool',
        'do_not_call': 'bool',
        'do_not_change_customer_info': 'bool',
        'enable_qir': 'bool',
        'enable_shopping_cart': 'bool',
        'id_and_verify_items': 'str',
        'instructions': 'str',
        'landing_merchant_creation': 'bool',
        'masquerade': 'bool',
        'max_emails_per_day': 'int',
        'mid_match_required': 'bool',
        'misc1_field_name': 'str',
        'misc2_field_name': 'str',
        'misc3_field_name': 'str',
        'misc4_field_name': 'str',
        'name': 'str',
        'preferred_name': 'str',
        'reports_discover': 'bool',
        'reports_fastpass': 'bool',
        'reports_first_data_l4': 'bool',
        'reports_mastercard': 'bool',
        'reports_visa_asia_pacific': 'bool',
        'reports_visa_europe': 'bool',
        'reports_visa_north_america': 'bool',
        'reports_weekly_stats': 'bool',
        'require_id_and_verify': 'bool',
        'saq3_confirm_all': 'bool',
        'saq_d_support': 'bool',
        'saq_response_options': 'str',
        'show_goals': 'bool',
        'uuid': 'str'
    }

    attribute_map = {
        'links': 'links',
        'auto_emails': 'auto_emails',
        'date_created': 'date_created',
        'disable_mcc_export': 'disable_mcc_export',
        'do_not_call': 'do_not_call',
        'do_not_change_customer_info': 'do_not_change_customer_info',
        'enable_qir': 'enable_qir',
        'enable_shopping_cart': 'enable_shopping_cart',
        'id_and_verify_items': 'id_and_verify_items',
        'instructions': 'instructions',
        'landing_merchant_creation': 'landing_merchant_creation',
        'masquerade': 'masquerade',
        'max_emails_per_day': 'max_emails_per_day',
        'mid_match_required': 'mid_match_required',
        'misc1_field_name': 'misc1_field_name',
        'misc2_field_name': 'misc2_field_name',
        'misc3_field_name': 'misc3_field_name',
        'misc4_field_name': 'misc4_field_name',
        'name': 'name',
        'preferred_name': 'preferred_name',
        'reports_discover': 'reports_discover',
        'reports_fastpass': 'reports_fastpass',
        'reports_first_data_l4': 'reports_first_data_l4',
        'reports_mastercard': 'reports_mastercard',
        'reports_visa_asia_pacific': 'reports_visa_asia_pacific',
        'reports_visa_europe': 'reports_visa_europe',
        'reports_visa_north_america': 'reports_visa_north_america',
        'reports_weekly_stats': 'reports_weekly_stats',
        'require_id_and_verify': 'require_id_and_verify',
        'saq3_confirm_all': 'saq3_confirm_all',
        'saq_d_support': 'saq_d_support',
        'saq_response_options': 'saq_response_options',
        'show_goals': 'show_goals',
        'uuid': 'uuid'
    }

    def __init__(self, links=None, auto_emails=None, date_created=None, disable_mcc_export=None, do_not_call=None, do_not_change_customer_info=None, enable_qir=None, enable_shopping_cart=None, id_and_verify_items=None, instructions=None, landing_merchant_creation=None, masquerade=None, max_emails_per_day=None, mid_match_required=None, misc1_field_name=None, misc2_field_name=None, misc3_field_name=None, misc4_field_name=None, name=None, preferred_name=None, reports_discover=None, reports_fastpass=None, reports_first_data_l4=None, reports_mastercard=None, reports_visa_asia_pacific=None, reports_visa_europe=None, reports_visa_north_america=None, reports_weekly_stats=None, require_id_and_verify=None, saq3_confirm_all=None, saq_d_support=None, saq_response_options=None, show_goals=None, uuid=None):  # noqa: E501
        """PartnerWithLinks - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._auto_emails = None
        self._date_created = None
        self._disable_mcc_export = None
        self._do_not_call = None
        self._do_not_change_customer_info = None
        self._enable_qir = None
        self._enable_shopping_cart = None
        self._id_and_verify_items = None
        self._instructions = None
        self._landing_merchant_creation = None
        self._masquerade = None
        self._max_emails_per_day = None
        self._mid_match_required = None
        self._misc1_field_name = None
        self._misc2_field_name = None
        self._misc3_field_name = None
        self._misc4_field_name = None
        self._name = None
        self._preferred_name = None
        self._reports_discover = None
        self._reports_fastpass = None
        self._reports_first_data_l4 = None
        self._reports_mastercard = None
        self._reports_visa_asia_pacific = None
        self._reports_visa_europe = None
        self._reports_visa_north_america = None
        self._reports_weekly_stats = None
        self._require_id_and_verify = None
        self._saq3_confirm_all = None
        self._saq_d_support = None
        self._saq_response_options = None
        self._show_goals = None
        self._uuid = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if auto_emails is not None:
            self.auto_emails = auto_emails
        if date_created is not None:
            self.date_created = date_created
        if disable_mcc_export is not None:
            self.disable_mcc_export = disable_mcc_export
        if do_not_call is not None:
            self.do_not_call = do_not_call
        if do_not_change_customer_info is not None:
            self.do_not_change_customer_info = do_not_change_customer_info
        if enable_qir is not None:
            self.enable_qir = enable_qir
        if enable_shopping_cart is not None:
            self.enable_shopping_cart = enable_shopping_cart
        if id_and_verify_items is not None:
            self.id_and_verify_items = id_and_verify_items
        if instructions is not None:
            self.instructions = instructions
        if landing_merchant_creation is not None:
            self.landing_merchant_creation = landing_merchant_creation
        if masquerade is not None:
            self.masquerade = masquerade
        if max_emails_per_day is not None:
            self.max_emails_per_day = max_emails_per_day
        if mid_match_required is not None:
            self.mid_match_required = mid_match_required
        if misc1_field_name is not None:
            self.misc1_field_name = misc1_field_name
        if misc2_field_name is not None:
            self.misc2_field_name = misc2_field_name
        if misc3_field_name is not None:
            self.misc3_field_name = misc3_field_name
        if misc4_field_name is not None:
            self.misc4_field_name = misc4_field_name
        if name is not None:
            self.name = name
        if preferred_name is not None:
            self.preferred_name = preferred_name
        if reports_discover is not None:
            self.reports_discover = reports_discover
        if reports_fastpass is not None:
            self.reports_fastpass = reports_fastpass
        if reports_first_data_l4 is not None:
            self.reports_first_data_l4 = reports_first_data_l4
        if reports_mastercard is not None:
            self.reports_mastercard = reports_mastercard
        if reports_visa_asia_pacific is not None:
            self.reports_visa_asia_pacific = reports_visa_asia_pacific
        if reports_visa_europe is not None:
            self.reports_visa_europe = reports_visa_europe
        if reports_visa_north_america is not None:
            self.reports_visa_north_america = reports_visa_north_america
        if reports_weekly_stats is not None:
            self.reports_weekly_stats = reports_weekly_stats
        if require_id_and_verify is not None:
            self.require_id_and_verify = require_id_and_verify
        if saq3_confirm_all is not None:
            self.saq3_confirm_all = saq3_confirm_all
        if saq_d_support is not None:
            self.saq_d_support = saq_d_support
        if saq_response_options is not None:
            self.saq_response_options = saq_response_options
        if show_goals is not None:
            self.show_goals = show_goals
        if uuid is not None:
            self.uuid = uuid

    @property
    def links(self):
        """Gets the links of this PartnerWithLinks.  # noqa: E501


        :return: The links of this PartnerWithLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PartnerWithLinks.


        :param links: The links of this PartnerWithLinks.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def auto_emails(self):
        """Gets the auto_emails of this PartnerWithLinks.  # noqa: E501

        If True, we will send automated emails to merchants of this Partner  # noqa: E501

        :return: The auto_emails of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._auto_emails

    @auto_emails.setter
    def auto_emails(self, auto_emails):
        """Sets the auto_emails of this PartnerWithLinks.

        If True, we will send automated emails to merchants of this Partner  # noqa: E501

        :param auto_emails: The auto_emails of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._auto_emails = auto_emails

    @property
    def date_created(self):
        """Gets the date_created of this PartnerWithLinks.  # noqa: E501

        The date this Partner was created  # noqa: E501

        :return: The date_created of this PartnerWithLinks.  # noqa: E501
        :rtype: date
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this PartnerWithLinks.

        The date this Partner was created  # noqa: E501

        :param date_created: The date_created of this PartnerWithLinks.  # noqa: E501
        :type: date
        """

        self._date_created = date_created

    @property
    def disable_mcc_export(self):
        """Gets the disable_mcc_export of this PartnerWithLinks.  # noqa: E501

        If True, then the Partner cannot export merchants in Partner+  # noqa: E501

        :return: The disable_mcc_export of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._disable_mcc_export

    @disable_mcc_export.setter
    def disable_mcc_export(self, disable_mcc_export):
        """Sets the disable_mcc_export of this PartnerWithLinks.

        If True, then the Partner cannot export merchants in Partner+  # noqa: E501

        :param disable_mcc_export: The disable_mcc_export of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._disable_mcc_export = disable_mcc_export

    @property
    def do_not_call(self):
        """Gets the do_not_call of this PartnerWithLinks.  # noqa: E501

        If True, then we should not call this Partner's merchants  # noqa: E501

        :return: The do_not_call of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._do_not_call

    @do_not_call.setter
    def do_not_call(self, do_not_call):
        """Sets the do_not_call of this PartnerWithLinks.

        If True, then we should not call this Partner's merchants  # noqa: E501

        :param do_not_call: The do_not_call of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._do_not_call = do_not_call

    @property
    def do_not_change_customer_info(self):
        """Gets the do_not_change_customer_info of this PartnerWithLinks.  # noqa: E501

        Do not allow certain customer info to be changed  # noqa: E501

        :return: The do_not_change_customer_info of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._do_not_change_customer_info

    @do_not_change_customer_info.setter
    def do_not_change_customer_info(self, do_not_change_customer_info):
        """Sets the do_not_change_customer_info of this PartnerWithLinks.

        Do not allow certain customer info to be changed  # noqa: E501

        :param do_not_change_customer_info: The do_not_change_customer_info of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._do_not_change_customer_info = do_not_change_customer_info

    @property
    def enable_qir(self):
        """Gets the enable_qir of this PartnerWithLinks.  # noqa: E501

        The QIR program is applicable for the Partner and merchants  # noqa: E501

        :return: The enable_qir of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._enable_qir

    @enable_qir.setter
    def enable_qir(self, enable_qir):
        """Sets the enable_qir of this PartnerWithLinks.

        The QIR program is applicable for the Partner and merchants  # noqa: E501

        :param enable_qir: The enable_qir of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._enable_qir = enable_qir

    @property
    def enable_shopping_cart(self):
        """Gets the enable_shopping_cart of this PartnerWithLinks.  # noqa: E501

        Ability to enable the online shopping cart for users  # noqa: E501

        :return: The enable_shopping_cart of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._enable_shopping_cart

    @enable_shopping_cart.setter
    def enable_shopping_cart(self, enable_shopping_cart):
        """Sets the enable_shopping_cart of this PartnerWithLinks.

        Ability to enable the online shopping cart for users  # noqa: E501

        :param enable_shopping_cart: The enable_shopping_cart of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._enable_shopping_cart = enable_shopping_cart

    @property
    def id_and_verify_items(self):
        """Gets the id_and_verify_items of this PartnerWithLinks.  # noqa: E501

        The items that the Partner wants identified and verified when merchants call in  # noqa: E501

        :return: The id_and_verify_items of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._id_and_verify_items

    @id_and_verify_items.setter
    def id_and_verify_items(self, id_and_verify_items):
        """Sets the id_and_verify_items of this PartnerWithLinks.

        The items that the Partner wants identified and verified when merchants call in  # noqa: E501

        :param id_and_verify_items: The id_and_verify_items of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._id_and_verify_items = id_and_verify_items

    @property
    def instructions(self):
        """Gets the instructions of this PartnerWithLinks.  # noqa: E501

        Instructions for SecurityMetrics Agents when working with Merchants of this Partner  # noqa: E501

        :return: The instructions of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this PartnerWithLinks.

        Instructions for SecurityMetrics Agents when working with Merchants of this Partner  # noqa: E501

        :param instructions: The instructions of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._instructions = instructions

    @property
    def landing_merchant_creation(self):
        """Gets the landing_merchant_creation of this PartnerWithLinks.  # noqa: E501

        Whether this Partner has allowed merchant records to be created from their custom landing page  # noqa: E501

        :return: The landing_merchant_creation of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._landing_merchant_creation

    @landing_merchant_creation.setter
    def landing_merchant_creation(self, landing_merchant_creation):
        """Sets the landing_merchant_creation of this PartnerWithLinks.

        Whether this Partner has allowed merchant records to be created from their custom landing page  # noqa: E501

        :param landing_merchant_creation: The landing_merchant_creation of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._landing_merchant_creation = landing_merchant_creation

    @property
    def masquerade(self):
        """Gets the masquerade of this PartnerWithLinks.  # noqa: E501

        The Partner has Masquerade abilities  # noqa: E501

        :return: The masquerade of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._masquerade

    @masquerade.setter
    def masquerade(self, masquerade):
        """Sets the masquerade of this PartnerWithLinks.

        The Partner has Masquerade abilities  # noqa: E501

        :param masquerade: The masquerade of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._masquerade = masquerade

    @property
    def max_emails_per_day(self):
        """Gets the max_emails_per_day of this PartnerWithLinks.  # noqa: E501

        The max number of emals we send to the Merchants of this Partner per day. 0 means no limit  # noqa: E501

        :return: The max_emails_per_day of this PartnerWithLinks.  # noqa: E501
        :rtype: int
        """
        return self._max_emails_per_day

    @max_emails_per_day.setter
    def max_emails_per_day(self, max_emails_per_day):
        """Sets the max_emails_per_day of this PartnerWithLinks.

        The max number of emals we send to the Merchants of this Partner per day. 0 means no limit  # noqa: E501

        :param max_emails_per_day: The max_emails_per_day of this PartnerWithLinks.  # noqa: E501
        :type: int
        """

        self._max_emails_per_day = max_emails_per_day

    @property
    def mid_match_required(self):
        """Gets the mid_match_required of this PartnerWithLinks.  # noqa: E501

        Whether this Partner requires MID matching as a part of the online setup and purchase process  # noqa: E501

        :return: The mid_match_required of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._mid_match_required

    @mid_match_required.setter
    def mid_match_required(self, mid_match_required):
        """Sets the mid_match_required of this PartnerWithLinks.

        Whether this Partner requires MID matching as a part of the online setup and purchase process  # noqa: E501

        :param mid_match_required: The mid_match_required of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._mid_match_required = mid_match_required

    @property
    def misc1_field_name(self):
        """Gets the misc1_field_name of this PartnerWithLinks.  # noqa: E501

        The Partner-chosen name of the Merchant misc1 field  # noqa: E501

        :return: The misc1_field_name of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._misc1_field_name

    @misc1_field_name.setter
    def misc1_field_name(self, misc1_field_name):
        """Sets the misc1_field_name of this PartnerWithLinks.

        The Partner-chosen name of the Merchant misc1 field  # noqa: E501

        :param misc1_field_name: The misc1_field_name of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._misc1_field_name = misc1_field_name

    @property
    def misc2_field_name(self):
        """Gets the misc2_field_name of this PartnerWithLinks.  # noqa: E501

        The Partner-chosen name of the Merchant misc2 field  # noqa: E501

        :return: The misc2_field_name of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._misc2_field_name

    @misc2_field_name.setter
    def misc2_field_name(self, misc2_field_name):
        """Sets the misc2_field_name of this PartnerWithLinks.

        The Partner-chosen name of the Merchant misc2 field  # noqa: E501

        :param misc2_field_name: The misc2_field_name of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._misc2_field_name = misc2_field_name

    @property
    def misc3_field_name(self):
        """Gets the misc3_field_name of this PartnerWithLinks.  # noqa: E501

        The Partner-chosen name of the Merchant misc3 field  # noqa: E501

        :return: The misc3_field_name of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._misc3_field_name

    @misc3_field_name.setter
    def misc3_field_name(self, misc3_field_name):
        """Sets the misc3_field_name of this PartnerWithLinks.

        The Partner-chosen name of the Merchant misc3 field  # noqa: E501

        :param misc3_field_name: The misc3_field_name of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._misc3_field_name = misc3_field_name

    @property
    def misc4_field_name(self):
        """Gets the misc4_field_name of this PartnerWithLinks.  # noqa: E501

        The Partner-chosen name of the Merchant misc4 field  # noqa: E501

        :return: The misc4_field_name of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._misc4_field_name

    @misc4_field_name.setter
    def misc4_field_name(self, misc4_field_name):
        """Sets the misc4_field_name of this PartnerWithLinks.

        The Partner-chosen name of the Merchant misc4 field  # noqa: E501

        :param misc4_field_name: The misc4_field_name of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._misc4_field_name = misc4_field_name

    @property
    def name(self):
        """Gets the name of this PartnerWithLinks.  # noqa: E501

        The name of the Partner  # noqa: E501

        :return: The name of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartnerWithLinks.

        The name of the Partner  # noqa: E501

        :param name: The name of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preferred_name(self):
        """Gets the preferred_name of this PartnerWithLinks.  # noqa: E501

        An optional customer-facing name of the Partner  # noqa: E501

        :return: The preferred_name of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._preferred_name

    @preferred_name.setter
    def preferred_name(self, preferred_name):
        """Sets the preferred_name of this PartnerWithLinks.

        An optional customer-facing name of the Partner  # noqa: E501

        :param preferred_name: The preferred_name of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._preferred_name = preferred_name

    @property
    def reports_discover(self):
        """Gets the reports_discover of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the Discover report  # noqa: E501

        :return: The reports_discover of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_discover

    @reports_discover.setter
    def reports_discover(self, reports_discover):
        """Sets the reports_discover of this PartnerWithLinks.

        This Partner has access to the Discover report  # noqa: E501

        :param reports_discover: The reports_discover of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_discover = reports_discover

    @property
    def reports_fastpass(self):
        """Gets the reports_fastpass of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the Fastpass Responses report  # noqa: E501

        :return: The reports_fastpass of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_fastpass

    @reports_fastpass.setter
    def reports_fastpass(self, reports_fastpass):
        """Sets the reports_fastpass of this PartnerWithLinks.

        This Partner has access to the Fastpass Responses report  # noqa: E501

        :param reports_fastpass: The reports_fastpass of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_fastpass = reports_fastpass

    @property
    def reports_first_data_l4(self):
        """Gets the reports_first_data_l4 of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the First Data Opt Out report  # noqa: E501

        :return: The reports_first_data_l4 of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_first_data_l4

    @reports_first_data_l4.setter
    def reports_first_data_l4(self, reports_first_data_l4):
        """Sets the reports_first_data_l4 of this PartnerWithLinks.

        This Partner has access to the First Data Opt Out report  # noqa: E501

        :param reports_first_data_l4: The reports_first_data_l4 of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_first_data_l4 = reports_first_data_l4

    @property
    def reports_mastercard(self):
        """Gets the reports_mastercard of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the MasterCard report  # noqa: E501

        :return: The reports_mastercard of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_mastercard

    @reports_mastercard.setter
    def reports_mastercard(self, reports_mastercard):
        """Sets the reports_mastercard of this PartnerWithLinks.

        This Partner has access to the MasterCard report  # noqa: E501

        :param reports_mastercard: The reports_mastercard of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_mastercard = reports_mastercard

    @property
    def reports_visa_asia_pacific(self):
        """Gets the reports_visa_asia_pacific of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the Visa Asia Pacific report  # noqa: E501

        :return: The reports_visa_asia_pacific of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_visa_asia_pacific

    @reports_visa_asia_pacific.setter
    def reports_visa_asia_pacific(self, reports_visa_asia_pacific):
        """Sets the reports_visa_asia_pacific of this PartnerWithLinks.

        This Partner has access to the Visa Asia Pacific report  # noqa: E501

        :param reports_visa_asia_pacific: The reports_visa_asia_pacific of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_visa_asia_pacific = reports_visa_asia_pacific

    @property
    def reports_visa_europe(self):
        """Gets the reports_visa_europe of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the Visa Europe report  # noqa: E501

        :return: The reports_visa_europe of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_visa_europe

    @reports_visa_europe.setter
    def reports_visa_europe(self, reports_visa_europe):
        """Sets the reports_visa_europe of this PartnerWithLinks.

        This Partner has access to the Visa Europe report  # noqa: E501

        :param reports_visa_europe: The reports_visa_europe of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_visa_europe = reports_visa_europe

    @property
    def reports_visa_north_america(self):
        """Gets the reports_visa_north_america of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the Visa North America report  # noqa: E501

        :return: The reports_visa_north_america of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_visa_north_america

    @reports_visa_north_america.setter
    def reports_visa_north_america(self, reports_visa_north_america):
        """Sets the reports_visa_north_america of this PartnerWithLinks.

        This Partner has access to the Visa North America report  # noqa: E501

        :param reports_visa_north_america: The reports_visa_north_america of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_visa_north_america = reports_visa_north_america

    @property
    def reports_weekly_stats(self):
        """Gets the reports_weekly_stats of this PartnerWithLinks.  # noqa: E501

        This Partner has access to the Weekly Stats report  # noqa: E501

        :return: The reports_weekly_stats of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._reports_weekly_stats

    @reports_weekly_stats.setter
    def reports_weekly_stats(self, reports_weekly_stats):
        """Sets the reports_weekly_stats of this PartnerWithLinks.

        This Partner has access to the Weekly Stats report  # noqa: E501

        :param reports_weekly_stats: The reports_weekly_stats of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._reports_weekly_stats = reports_weekly_stats

    @property
    def require_id_and_verify(self):
        """Gets the require_id_and_verify of this PartnerWithLinks.  # noqa: E501

        The Partner requires SecurityMetrics to identify and verify certain information of merchants when they call in  # noqa: E501

        :return: The require_id_and_verify of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._require_id_and_verify

    @require_id_and_verify.setter
    def require_id_and_verify(self, require_id_and_verify):
        """Sets the require_id_and_verify of this PartnerWithLinks.

        The Partner requires SecurityMetrics to identify and verify certain information of merchants when they call in  # noqa: E501

        :param require_id_and_verify: The require_id_and_verify of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._require_id_and_verify = require_id_and_verify

    @property
    def saq3_confirm_all(self):
        """Gets the saq3_confirm_all of this PartnerWithLinks.  # noqa: E501

        Allow customers the option to answer \"yes\" to all questions in each section of the SAQ  # noqa: E501

        :return: The saq3_confirm_all of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._saq3_confirm_all

    @saq3_confirm_all.setter
    def saq3_confirm_all(self, saq3_confirm_all):
        """Sets the saq3_confirm_all of this PartnerWithLinks.

        Allow customers the option to answer \"yes\" to all questions in each section of the SAQ  # noqa: E501

        :param saq3_confirm_all: The saq3_confirm_all of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._saq3_confirm_all = saq3_confirm_all

    @property
    def saq_d_support(self):
        """Gets the saq_d_support of this PartnerWithLinks.  # noqa: E501

        Whether the Merchants of this Partner are required to purchase support for SAQ D  # noqa: E501

        :return: The saq_d_support of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._saq_d_support

    @saq_d_support.setter
    def saq_d_support(self, saq_d_support):
        """Sets the saq_d_support of this PartnerWithLinks.

        Whether the Merchants of this Partner are required to purchase support for SAQ D  # noqa: E501

        :param saq_d_support: The saq_d_support of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._saq_d_support = saq_d_support

    @property
    def saq_response_options(self):
        """Gets the saq_response_options of this PartnerWithLinks.  # noqa: E501

        The type of response options available to a Partner's merchants on SAQs  # noqa: E501

        :return: The saq_response_options of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._saq_response_options

    @saq_response_options.setter
    def saq_response_options(self, saq_response_options):
        """Sets the saq_response_options of this PartnerWithLinks.

        The type of response options available to a Partner's merchants on SAQs  # noqa: E501

        :param saq_response_options: The saq_response_options of this PartnerWithLinks.  # noqa: E501
        :type: str
        """
        allowed_values = ["2", "3", "5"]  # noqa: E501
        if saq_response_options not in allowed_values:
            raise ValueError(
                "Invalid value for `saq_response_options` ({0}), must be one of {1}"  # noqa: E501
                .format(saq_response_options, allowed_values)
            )

        self._saq_response_options = saq_response_options

    @property
    def show_goals(self):
        """Gets the show_goals of this PartnerWithLinks.  # noqa: E501

        Show goals  # noqa: E501

        :return: The show_goals of this PartnerWithLinks.  # noqa: E501
        :rtype: bool
        """
        return self._show_goals

    @show_goals.setter
    def show_goals(self, show_goals):
        """Sets the show_goals of this PartnerWithLinks.

        Show goals  # noqa: E501

        :param show_goals: The show_goals of this PartnerWithLinks.  # noqa: E501
        :type: bool
        """

        self._show_goals = show_goals

    @property
    def uuid(self):
        """Gets the uuid of this PartnerWithLinks.  # noqa: E501

        The Universal Unique IDentifier for this Partner  # noqa: E501

        :return: The uuid of this PartnerWithLinks.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PartnerWithLinks.

        The Universal Unique IDentifier for this Partner  # noqa: E501

        :param uuid: The uuid of this PartnerWithLinks.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(PartnerWithLinks, dict):
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
        if not isinstance(other, PartnerWithLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other