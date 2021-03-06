# coding: utf-8

"""
    CET-Lite for CoinEx Chain

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20014Result(object):
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
        'max_entries': 'int',
        'unbonding_time': 'str',
        'max_validators': 'int',
        'bond_denom': 'str',
        'min_self_delegation': 'str',
        'min_mandatory_commission_rate': 'str'
    }

    attribute_map = {
        'max_entries': 'max_entries',
        'unbonding_time': 'unbonding_time',
        'max_validators': 'max_validators',
        'bond_denom': 'bond_denom',
        'min_self_delegation': 'min_self_delegation',
        'min_mandatory_commission_rate': 'min_mandatory_commission_rate'
    }

    def __init__(self, max_entries=None, unbonding_time=None, max_validators=None, bond_denom=None, min_self_delegation=None, min_mandatory_commission_rate=None):  # noqa: E501
        """InlineResponse20014Result - a model defined in Swagger"""  # noqa: E501

        self._max_entries = None
        self._unbonding_time = None
        self._max_validators = None
        self._bond_denom = None
        self._min_self_delegation = None
        self._min_mandatory_commission_rate = None
        self.discriminator = None

        self.max_entries = max_entries
        self.unbonding_time = unbonding_time
        self.max_validators = max_validators
        self.bond_denom = bond_denom
        self.min_self_delegation = min_self_delegation
        self.min_mandatory_commission_rate = min_mandatory_commission_rate

    @property
    def max_entries(self):
        """Gets the max_entries of this InlineResponse20014Result.  # noqa: E501


        :return: The max_entries of this InlineResponse20014Result.  # noqa: E501
        :rtype: int
        """
        return self._max_entries

    @max_entries.setter
    def max_entries(self, max_entries):
        """Sets the max_entries of this InlineResponse20014Result.


        :param max_entries: The max_entries of this InlineResponse20014Result.  # noqa: E501
        :type: int
        """
        if max_entries is None:
            raise ValueError("Invalid value for `max_entries`, must not be `None`")  # noqa: E501

        self._max_entries = max_entries

    @property
    def unbonding_time(self):
        """Gets the unbonding_time of this InlineResponse20014Result.  # noqa: E501


        :return: The unbonding_time of this InlineResponse20014Result.  # noqa: E501
        :rtype: str
        """
        return self._unbonding_time

    @unbonding_time.setter
    def unbonding_time(self, unbonding_time):
        """Sets the unbonding_time of this InlineResponse20014Result.


        :param unbonding_time: The unbonding_time of this InlineResponse20014Result.  # noqa: E501
        :type: str
        """
        if unbonding_time is None:
            raise ValueError("Invalid value for `unbonding_time`, must not be `None`")  # noqa: E501

        self._unbonding_time = unbonding_time

    @property
    def max_validators(self):
        """Gets the max_validators of this InlineResponse20014Result.  # noqa: E501


        :return: The max_validators of this InlineResponse20014Result.  # noqa: E501
        :rtype: int
        """
        return self._max_validators

    @max_validators.setter
    def max_validators(self, max_validators):
        """Sets the max_validators of this InlineResponse20014Result.


        :param max_validators: The max_validators of this InlineResponse20014Result.  # noqa: E501
        :type: int
        """
        if max_validators is None:
            raise ValueError("Invalid value for `max_validators`, must not be `None`")  # noqa: E501

        self._max_validators = max_validators

    @property
    def bond_denom(self):
        """Gets the bond_denom of this InlineResponse20014Result.  # noqa: E501


        :return: The bond_denom of this InlineResponse20014Result.  # noqa: E501
        :rtype: str
        """
        return self._bond_denom

    @bond_denom.setter
    def bond_denom(self, bond_denom):
        """Sets the bond_denom of this InlineResponse20014Result.


        :param bond_denom: The bond_denom of this InlineResponse20014Result.  # noqa: E501
        :type: str
        """
        if bond_denom is None:
            raise ValueError("Invalid value for `bond_denom`, must not be `None`")  # noqa: E501

        self._bond_denom = bond_denom

    @property
    def min_self_delegation(self):
        """Gets the min_self_delegation of this InlineResponse20014Result.  # noqa: E501


        :return: The min_self_delegation of this InlineResponse20014Result.  # noqa: E501
        :rtype: str
        """
        return self._min_self_delegation

    @min_self_delegation.setter
    def min_self_delegation(self, min_self_delegation):
        """Sets the min_self_delegation of this InlineResponse20014Result.


        :param min_self_delegation: The min_self_delegation of this InlineResponse20014Result.  # noqa: E501
        :type: str
        """
        if min_self_delegation is None:
            raise ValueError("Invalid value for `min_self_delegation`, must not be `None`")  # noqa: E501

        self._min_self_delegation = min_self_delegation

    @property
    def min_mandatory_commission_rate(self):
        """Gets the min_mandatory_commission_rate of this InlineResponse20014Result.  # noqa: E501


        :return: The min_mandatory_commission_rate of this InlineResponse20014Result.  # noqa: E501
        :rtype: str
        """
        return self._min_mandatory_commission_rate

    @min_mandatory_commission_rate.setter
    def min_mandatory_commission_rate(self, min_mandatory_commission_rate):
        """Sets the min_mandatory_commission_rate of this InlineResponse20014Result.


        :param min_mandatory_commission_rate: The min_mandatory_commission_rate of this InlineResponse20014Result.  # noqa: E501
        :type: str
        """
        if min_mandatory_commission_rate is None:
            raise ValueError("Invalid value for `min_mandatory_commission_rate`, must not be `None`")  # noqa: E501

        self._min_mandatory_commission_rate = min_mandatory_commission_rate

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
        if issubclass(InlineResponse20014Result, dict):
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
        if not isinstance(other, InlineResponse20014Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
