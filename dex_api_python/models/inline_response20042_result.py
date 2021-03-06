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


class InlineResponse20042Result(object):
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
        'create_market_fee': 'str',
        'fixed_trade_fee': 'str',
        'market_min_expired_time': 'str',
        'gte_order_lifetime': 'str',
        'gte_order_feature_fee_by_blocks': 'str',
        'max_executed_price_change_ratio': 'str',
        'market_fee_rate': 'str',
        'market_fee_min': 'str',
        'fee_for_zero_deal': 'str'
    }

    attribute_map = {
        'create_market_fee': 'create_market_fee',
        'fixed_trade_fee': 'fixed_trade_fee',
        'market_min_expired_time': 'market_min_expired_time',
        'gte_order_lifetime': 'gte_order_lifetime',
        'gte_order_feature_fee_by_blocks': 'gte_order_feature_fee_by_blocks',
        'max_executed_price_change_ratio': 'max_executed_price_change_ratio',
        'market_fee_rate': 'market_fee_rate',
        'market_fee_min': 'market_fee_min',
        'fee_for_zero_deal': 'fee_for_zero_deal'
    }

    def __init__(self, create_market_fee=None, fixed_trade_fee=None, market_min_expired_time=None, gte_order_lifetime=None, gte_order_feature_fee_by_blocks=None, max_executed_price_change_ratio=None, market_fee_rate=None, market_fee_min=None, fee_for_zero_deal=None):  # noqa: E501
        """InlineResponse20042Result - a model defined in Swagger"""  # noqa: E501

        self._create_market_fee = None
        self._fixed_trade_fee = None
        self._market_min_expired_time = None
        self._gte_order_lifetime = None
        self._gte_order_feature_fee_by_blocks = None
        self._max_executed_price_change_ratio = None
        self._market_fee_rate = None
        self._market_fee_min = None
        self._fee_for_zero_deal = None
        self.discriminator = None

        if create_market_fee is not None:
            self.create_market_fee = create_market_fee
        if fixed_trade_fee is not None:
            self.fixed_trade_fee = fixed_trade_fee
        if market_min_expired_time is not None:
            self.market_min_expired_time = market_min_expired_time
        if gte_order_lifetime is not None:
            self.gte_order_lifetime = gte_order_lifetime
        if gte_order_feature_fee_by_blocks is not None:
            self.gte_order_feature_fee_by_blocks = gte_order_feature_fee_by_blocks
        if max_executed_price_change_ratio is not None:
            self.max_executed_price_change_ratio = max_executed_price_change_ratio
        if market_fee_rate is not None:
            self.market_fee_rate = market_fee_rate
        if market_fee_min is not None:
            self.market_fee_min = market_fee_min
        if fee_for_zero_deal is not None:
            self.fee_for_zero_deal = fee_for_zero_deal

    @property
    def create_market_fee(self):
        """Gets the create_market_fee of this InlineResponse20042Result.  # noqa: E501


        :return: The create_market_fee of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._create_market_fee

    @create_market_fee.setter
    def create_market_fee(self, create_market_fee):
        """Sets the create_market_fee of this InlineResponse20042Result.


        :param create_market_fee: The create_market_fee of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._create_market_fee = create_market_fee

    @property
    def fixed_trade_fee(self):
        """Gets the fixed_trade_fee of this InlineResponse20042Result.  # noqa: E501


        :return: The fixed_trade_fee of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._fixed_trade_fee

    @fixed_trade_fee.setter
    def fixed_trade_fee(self, fixed_trade_fee):
        """Sets the fixed_trade_fee of this InlineResponse20042Result.


        :param fixed_trade_fee: The fixed_trade_fee of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._fixed_trade_fee = fixed_trade_fee

    @property
    def market_min_expired_time(self):
        """Gets the market_min_expired_time of this InlineResponse20042Result.  # noqa: E501


        :return: The market_min_expired_time of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._market_min_expired_time

    @market_min_expired_time.setter
    def market_min_expired_time(self, market_min_expired_time):
        """Sets the market_min_expired_time of this InlineResponse20042Result.


        :param market_min_expired_time: The market_min_expired_time of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._market_min_expired_time = market_min_expired_time

    @property
    def gte_order_lifetime(self):
        """Gets the gte_order_lifetime of this InlineResponse20042Result.  # noqa: E501


        :return: The gte_order_lifetime of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._gte_order_lifetime

    @gte_order_lifetime.setter
    def gte_order_lifetime(self, gte_order_lifetime):
        """Sets the gte_order_lifetime of this InlineResponse20042Result.


        :param gte_order_lifetime: The gte_order_lifetime of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._gte_order_lifetime = gte_order_lifetime

    @property
    def gte_order_feature_fee_by_blocks(self):
        """Gets the gte_order_feature_fee_by_blocks of this InlineResponse20042Result.  # noqa: E501


        :return: The gte_order_feature_fee_by_blocks of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._gte_order_feature_fee_by_blocks

    @gte_order_feature_fee_by_blocks.setter
    def gte_order_feature_fee_by_blocks(self, gte_order_feature_fee_by_blocks):
        """Sets the gte_order_feature_fee_by_blocks of this InlineResponse20042Result.


        :param gte_order_feature_fee_by_blocks: The gte_order_feature_fee_by_blocks of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._gte_order_feature_fee_by_blocks = gte_order_feature_fee_by_blocks

    @property
    def max_executed_price_change_ratio(self):
        """Gets the max_executed_price_change_ratio of this InlineResponse20042Result.  # noqa: E501


        :return: The max_executed_price_change_ratio of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._max_executed_price_change_ratio

    @max_executed_price_change_ratio.setter
    def max_executed_price_change_ratio(self, max_executed_price_change_ratio):
        """Sets the max_executed_price_change_ratio of this InlineResponse20042Result.


        :param max_executed_price_change_ratio: The max_executed_price_change_ratio of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._max_executed_price_change_ratio = max_executed_price_change_ratio

    @property
    def market_fee_rate(self):
        """Gets the market_fee_rate of this InlineResponse20042Result.  # noqa: E501


        :return: The market_fee_rate of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._market_fee_rate

    @market_fee_rate.setter
    def market_fee_rate(self, market_fee_rate):
        """Sets the market_fee_rate of this InlineResponse20042Result.


        :param market_fee_rate: The market_fee_rate of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._market_fee_rate = market_fee_rate

    @property
    def market_fee_min(self):
        """Gets the market_fee_min of this InlineResponse20042Result.  # noqa: E501


        :return: The market_fee_min of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._market_fee_min

    @market_fee_min.setter
    def market_fee_min(self, market_fee_min):
        """Sets the market_fee_min of this InlineResponse20042Result.


        :param market_fee_min: The market_fee_min of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._market_fee_min = market_fee_min

    @property
    def fee_for_zero_deal(self):
        """Gets the fee_for_zero_deal of this InlineResponse20042Result.  # noqa: E501


        :return: The fee_for_zero_deal of this InlineResponse20042Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_zero_deal

    @fee_for_zero_deal.setter
    def fee_for_zero_deal(self, fee_for_zero_deal):
        """Sets the fee_for_zero_deal of this InlineResponse20042Result.


        :param fee_for_zero_deal: The fee_for_zero_deal of this InlineResponse20042Result.  # noqa: E501
        :type: str
        """

        self._fee_for_zero_deal = fee_for_zero_deal

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
        if issubclass(InlineResponse20042Result, dict):
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
        if not isinstance(other, InlineResponse20042Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
