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


class ValidatorDistInfo(object):
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
        'operator_address': 'ValidatorAddress',
        'self_bond_rewards': 'list[Coin]',
        'val_commission': 'list[Coin]'
    }

    attribute_map = {
        'operator_address': 'operator_address',
        'self_bond_rewards': 'self_bond_rewards',
        'val_commission': 'val_commission'
    }

    def __init__(self, operator_address=None, self_bond_rewards=None, val_commission=None):  # noqa: E501
        """ValidatorDistInfo - a model defined in Swagger"""  # noqa: E501

        self._operator_address = None
        self._self_bond_rewards = None
        self._val_commission = None
        self.discriminator = None

        self.operator_address = operator_address
        self.self_bond_rewards = self_bond_rewards
        self.val_commission = val_commission

    @property
    def operator_address(self):
        """Gets the operator_address of this ValidatorDistInfo.  # noqa: E501


        :return: The operator_address of this ValidatorDistInfo.  # noqa: E501
        :rtype: ValidatorAddress
        """
        return self._operator_address

    @operator_address.setter
    def operator_address(self, operator_address):
        """Sets the operator_address of this ValidatorDistInfo.


        :param operator_address: The operator_address of this ValidatorDistInfo.  # noqa: E501
        :type: ValidatorAddress
        """
        if operator_address is None:
            raise ValueError("Invalid value for `operator_address`, must not be `None`")  # noqa: E501

        self._operator_address = operator_address

    @property
    def self_bond_rewards(self):
        """Gets the self_bond_rewards of this ValidatorDistInfo.  # noqa: E501


        :return: The self_bond_rewards of this ValidatorDistInfo.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._self_bond_rewards

    @self_bond_rewards.setter
    def self_bond_rewards(self, self_bond_rewards):
        """Sets the self_bond_rewards of this ValidatorDistInfo.


        :param self_bond_rewards: The self_bond_rewards of this ValidatorDistInfo.  # noqa: E501
        :type: list[Coin]
        """
        if self_bond_rewards is None:
            raise ValueError("Invalid value for `self_bond_rewards`, must not be `None`")  # noqa: E501

        self._self_bond_rewards = self_bond_rewards

    @property
    def val_commission(self):
        """Gets the val_commission of this ValidatorDistInfo.  # noqa: E501


        :return: The val_commission of this ValidatorDistInfo.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._val_commission

    @val_commission.setter
    def val_commission(self, val_commission):
        """Sets the val_commission of this ValidatorDistInfo.


        :param val_commission: The val_commission of this ValidatorDistInfo.  # noqa: E501
        :type: list[Coin]
        """
        if val_commission is None:
            raise ValueError("Invalid value for `val_commission`, must not be `None`")  # noqa: E501

        self._val_commission = val_commission

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
        if issubclass(ValidatorDistInfo, dict):
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
        if not isinstance(other, ValidatorDistInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
