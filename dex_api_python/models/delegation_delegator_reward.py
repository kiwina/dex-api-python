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


class DelegationDelegatorReward(object):
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
        'validator_address': 'ValidatorAddress',
        'reward': 'list[Coin]'
    }

    attribute_map = {
        'validator_address': 'validator_address',
        'reward': 'reward'
    }

    def __init__(self, validator_address=None, reward=None):  # noqa: E501
        """DelegationDelegatorReward - a model defined in Swagger"""  # noqa: E501

        self._validator_address = None
        self._reward = None
        self.discriminator = None

        self.validator_address = validator_address
        self.reward = reward

    @property
    def validator_address(self):
        """Gets the validator_address of this DelegationDelegatorReward.  # noqa: E501


        :return: The validator_address of this DelegationDelegatorReward.  # noqa: E501
        :rtype: ValidatorAddress
        """
        return self._validator_address

    @validator_address.setter
    def validator_address(self, validator_address):
        """Sets the validator_address of this DelegationDelegatorReward.


        :param validator_address: The validator_address of this DelegationDelegatorReward.  # noqa: E501
        :type: ValidatorAddress
        """
        if validator_address is None:
            raise ValueError("Invalid value for `validator_address`, must not be `None`")  # noqa: E501

        self._validator_address = validator_address

    @property
    def reward(self):
        """Gets the reward of this DelegationDelegatorReward.  # noqa: E501


        :return: The reward of this DelegationDelegatorReward.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._reward

    @reward.setter
    def reward(self, reward):
        """Sets the reward of this DelegationDelegatorReward.


        :param reward: The reward of this DelegationDelegatorReward.  # noqa: E501
        :type: list[Coin]
        """
        if reward is None:
            raise ValueError("Invalid value for `reward`, must not be `None`")  # noqa: E501

        self._reward = reward

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
        if issubclass(DelegationDelegatorReward, dict):
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
        if not isinstance(other, DelegationDelegatorReward):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
