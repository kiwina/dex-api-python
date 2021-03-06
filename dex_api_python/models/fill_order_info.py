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


class FillOrderInfo(object):
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
        'order_id': 'str',
        'trading_pair': 'str',
        'height': 'int',
        'side': 'int',
        'price': 'str',
        'left_stock': 'int',
        'freeze': 'int',
        'deal_stock': 'int',
        'deal_money': 'int',
        'curr_stock': 'int',
        'curr_money': 'int'
    }

    attribute_map = {
        'order_id': 'order_id',
        'trading_pair': 'trading_pair',
        'height': 'height',
        'side': 'side',
        'price': 'price',
        'left_stock': 'left_stock',
        'freeze': 'freeze',
        'deal_stock': 'deal_stock',
        'deal_money': 'deal_money',
        'curr_stock': 'curr_stock',
        'curr_money': 'curr_money'
    }

    def __init__(self, order_id=None, trading_pair=None, height=None, side=None, price=None, left_stock=None, freeze=None, deal_stock=None, deal_money=None, curr_stock=None, curr_money=None):  # noqa: E501
        """FillOrderInfo - a model defined in Swagger"""  # noqa: E501

        self._order_id = None
        self._trading_pair = None
        self._height = None
        self._side = None
        self._price = None
        self._left_stock = None
        self._freeze = None
        self._deal_stock = None
        self._deal_money = None
        self._curr_stock = None
        self._curr_money = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if trading_pair is not None:
            self.trading_pair = trading_pair
        if height is not None:
            self.height = height
        if side is not None:
            self.side = side
        if price is not None:
            self.price = price
        if left_stock is not None:
            self.left_stock = left_stock
        if freeze is not None:
            self.freeze = freeze
        if deal_stock is not None:
            self.deal_stock = deal_stock
        if deal_money is not None:
            self.deal_money = deal_money
        if curr_stock is not None:
            self.curr_stock = curr_stock
        if curr_money is not None:
            self.curr_money = curr_money

    @property
    def order_id(self):
        """Gets the order_id of this FillOrderInfo.  # noqa: E501


        :return: The order_id of this FillOrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this FillOrderInfo.


        :param order_id: The order_id of this FillOrderInfo.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def trading_pair(self):
        """Gets the trading_pair of this FillOrderInfo.  # noqa: E501


        :return: The trading_pair of this FillOrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this FillOrderInfo.


        :param trading_pair: The trading_pair of this FillOrderInfo.  # noqa: E501
        :type: str
        """

        self._trading_pair = trading_pair

    @property
    def height(self):
        """Gets the height of this FillOrderInfo.  # noqa: E501


        :return: The height of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this FillOrderInfo.


        :param height: The height of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def side(self):
        """Gets the side of this FillOrderInfo.  # noqa: E501

        BUY:1/SELL:2  # noqa: E501

        :return: The side of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this FillOrderInfo.

        BUY:1/SELL:2  # noqa: E501

        :param side: The side of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._side = side

    @property
    def price(self):
        """Gets the price of this FillOrderInfo.  # noqa: E501


        :return: The price of this FillOrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this FillOrderInfo.


        :param price: The price of this FillOrderInfo.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def left_stock(self):
        """Gets the left_stock of this FillOrderInfo.  # noqa: E501

        Order left stock  # noqa: E501

        :return: The left_stock of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._left_stock

    @left_stock.setter
    def left_stock(self, left_stock):
        """Sets the left_stock of this FillOrderInfo.

        Order left stock  # noqa: E501

        :param left_stock: The left_stock of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._left_stock = left_stock

    @property
    def freeze(self):
        """Gets the freeze of this FillOrderInfo.  # noqa: E501

        Freeze sato.CET amount  # noqa: E501

        :return: The freeze of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._freeze

    @freeze.setter
    def freeze(self, freeze):
        """Sets the freeze of this FillOrderInfo.

        Freeze sato.CET amount  # noqa: E501

        :param freeze: The freeze of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._freeze = freeze

    @property
    def deal_stock(self):
        """Gets the deal_stock of this FillOrderInfo.  # noqa: E501

        Order accumulated deal stock amount  # noqa: E501

        :return: The deal_stock of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._deal_stock

    @deal_stock.setter
    def deal_stock(self, deal_stock):
        """Sets the deal_stock of this FillOrderInfo.

        Order accumulated deal stock amount  # noqa: E501

        :param deal_stock: The deal_stock of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._deal_stock = deal_stock

    @property
    def deal_money(self):
        """Gets the deal_money of this FillOrderInfo.  # noqa: E501

        Order accumulated deal money amount  # noqa: E501

        :return: The deal_money of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._deal_money

    @deal_money.setter
    def deal_money(self, deal_money):
        """Sets the deal_money of this FillOrderInfo.

        Order accumulated deal money amount  # noqa: E501

        :param deal_money: The deal_money of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._deal_money = deal_money

    @property
    def curr_stock(self):
        """Gets the curr_stock of this FillOrderInfo.  # noqa: E501

        Current block deal stock amount  # noqa: E501

        :return: The curr_stock of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._curr_stock

    @curr_stock.setter
    def curr_stock(self, curr_stock):
        """Sets the curr_stock of this FillOrderInfo.

        Current block deal stock amount  # noqa: E501

        :param curr_stock: The curr_stock of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._curr_stock = curr_stock

    @property
    def curr_money(self):
        """Gets the curr_money of this FillOrderInfo.  # noqa: E501

        Current block deal money amount  # noqa: E501

        :return: The curr_money of this FillOrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._curr_money

    @curr_money.setter
    def curr_money(self, curr_money):
        """Sets the curr_money of this FillOrderInfo.

        Current block deal money amount  # noqa: E501

        :param curr_money: The curr_money of this FillOrderInfo.  # noqa: E501
        :type: int
        """

        self._curr_money = curr_money

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
        if issubclass(FillOrderInfo, dict):
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
        if not isinstance(other, FillOrderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
