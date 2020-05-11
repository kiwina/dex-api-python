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


class InlineResponse20033Result(object):
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
        'base_proposer_reward': 'str',
        'bonus_proposer_reward': 'str',
        'community_tax': 'str'
    }

    attribute_map = {
        'base_proposer_reward': 'base_proposer_reward',
        'bonus_proposer_reward': 'bonus_proposer_reward',
        'community_tax': 'community_tax'
    }

    def __init__(self, base_proposer_reward=None, bonus_proposer_reward=None, community_tax=None):  # noqa: E501
        """InlineResponse20033Result - a model defined in Swagger"""  # noqa: E501

        self._base_proposer_reward = None
        self._bonus_proposer_reward = None
        self._community_tax = None
        self.discriminator = None

        if base_proposer_reward is not None:
            self.base_proposer_reward = base_proposer_reward
        if bonus_proposer_reward is not None:
            self.bonus_proposer_reward = bonus_proposer_reward
        if community_tax is not None:
            self.community_tax = community_tax

    @property
    def base_proposer_reward(self):
        """Gets the base_proposer_reward of this InlineResponse20033Result.  # noqa: E501


        :return: The base_proposer_reward of this InlineResponse20033Result.  # noqa: E501
        :rtype: str
        """
        return self._base_proposer_reward

    @base_proposer_reward.setter
    def base_proposer_reward(self, base_proposer_reward):
        """Sets the base_proposer_reward of this InlineResponse20033Result.


        :param base_proposer_reward: The base_proposer_reward of this InlineResponse20033Result.  # noqa: E501
        :type: str
        """

        self._base_proposer_reward = base_proposer_reward

    @property
    def bonus_proposer_reward(self):
        """Gets the bonus_proposer_reward of this InlineResponse20033Result.  # noqa: E501


        :return: The bonus_proposer_reward of this InlineResponse20033Result.  # noqa: E501
        :rtype: str
        """
        return self._bonus_proposer_reward

    @bonus_proposer_reward.setter
    def bonus_proposer_reward(self, bonus_proposer_reward):
        """Sets the bonus_proposer_reward of this InlineResponse20033Result.


        :param bonus_proposer_reward: The bonus_proposer_reward of this InlineResponse20033Result.  # noqa: E501
        :type: str
        """

        self._bonus_proposer_reward = bonus_proposer_reward

    @property
    def community_tax(self):
        """Gets the community_tax of this InlineResponse20033Result.  # noqa: E501


        :return: The community_tax of this InlineResponse20033Result.  # noqa: E501
        :rtype: str
        """
        return self._community_tax

    @community_tax.setter
    def community_tax(self, community_tax):
        """Sets the community_tax of this InlineResponse20033Result.


        :param community_tax: The community_tax of this InlineResponse20033Result.  # noqa: E501
        :type: str
        """

        self._community_tax = community_tax

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
        if issubclass(InlineResponse20033Result, dict):
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
        if not isinstance(other, InlineResponse20033Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
