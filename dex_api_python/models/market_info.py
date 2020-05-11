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


class MarketInfo(object):
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
        'stock': 'str',
        'money': 'str',
        'price_precision': 'str',
        'order_precision': 'str',
        'last_executed_price': 'str',
        'creator': 'str'
    }

    attribute_map = {
        'stock': 'stock',
        'money': 'money',
        'price_precision': 'price_precision',
        'order_precision': 'order_precision',
        'last_executed_price': 'last_executed_price',
        'creator': 'creator'
    }

    def __init__(self, stock=None, money=None, price_precision=None, order_precision=None, last_executed_price=None, creator=None):  # noqa: E501
        """MarketInfo - a model defined in Swagger"""  # noqa: E501

        self._stock = None
        self._money = None
        self._price_precision = None
        self._order_precision = None
        self._last_executed_price = None
        self._creator = None
        self.discriminator = None

        self.stock = stock
        self.money = money
        self.price_precision = price_precision
        if order_precision is not None:
            self.order_precision = order_precision
        if last_executed_price is not None:
            self.last_executed_price = last_executed_price
        if creator is not None:
            self.creator = creator

    @property
    def stock(self):
        """Gets the stock of this MarketInfo.  # noqa: E501


        :return: The stock of this MarketInfo.  # noqa: E501
        :rtype: str
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this MarketInfo.


        :param stock: The stock of this MarketInfo.  # noqa: E501
        :type: str
        """
        if stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

    @property
    def money(self):
        """Gets the money of this MarketInfo.  # noqa: E501


        :return: The money of this MarketInfo.  # noqa: E501
        :rtype: str
        """
        return self._money

    @money.setter
    def money(self, money):
        """Sets the money of this MarketInfo.


        :param money: The money of this MarketInfo.  # noqa: E501
        :type: str
        """
        if money is None:
            raise ValueError("Invalid value for `money`, must not be `None`")  # noqa: E501

        self._money = money

    @property
    def price_precision(self):
        """Gets the price_precision of this MarketInfo.  # noqa: E501

        The trading-pair price precision, used to control the price accuracy of the order when token trades, valid range [0, 18]  # noqa: E501

        :return: The price_precision of this MarketInfo.  # noqa: E501
        :rtype: str
        """
        return self._price_precision

    @price_precision.setter
    def price_precision(self, price_precision):
        """Sets the price_precision of this MarketInfo.

        The trading-pair price precision, used to control the price accuracy of the order when token trades, valid range [0, 18]  # noqa: E501

        :param price_precision: The price_precision of this MarketInfo.  # noqa: E501
        :type: str
        """
        if price_precision is None:
            raise ValueError("Invalid value for `price_precision`, must not be `None`")  # noqa: E501

        self._price_precision = price_precision

    @property
    def order_precision(self):
        """Gets the order_precision of this MarketInfo.  # noqa: E501

        To control the granularity of token trade, the token amount of trade must be a multiple of granularity.  # noqa: E501

        :return: The order_precision of this MarketInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_precision

    @order_precision.setter
    def order_precision(self, order_precision):
        """Sets the order_precision of this MarketInfo.

        To control the granularity of token trade, the token amount of trade must be a multiple of granularity.  # noqa: E501

        :param order_precision: The order_precision of this MarketInfo.  # noqa: E501
        :type: str
        """

        self._order_precision = order_precision

    @property
    def last_executed_price(self):
        """Gets the last_executed_price of this MarketInfo.  # noqa: E501


        :return: The last_executed_price of this MarketInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_executed_price

    @last_executed_price.setter
    def last_executed_price(self, last_executed_price):
        """Sets the last_executed_price of this MarketInfo.


        :param last_executed_price: The last_executed_price of this MarketInfo.  # noqa: E501
        :type: str
        """

        self._last_executed_price = last_executed_price

    @property
    def creator(self):
        """Gets the creator of this MarketInfo.  # noqa: E501


        :return: The creator of this MarketInfo.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this MarketInfo.


        :param creator: The creator of this MarketInfo.  # noqa: E501
        :type: str
        """

        self._creator = creator

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
        if issubclass(MarketInfo, dict):
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
        if not isinstance(other, MarketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
