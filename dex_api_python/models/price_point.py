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


class PricePoint(object):
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
        'price': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'price': 'price',
        'amount': 'amount'
    }

    def __init__(self, price=None, amount=None):  # noqa: E501
        """PricePoint - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._amount = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if amount is not None:
            self.amount = amount

    @property
    def price(self):
        """Gets the price of this PricePoint.  # noqa: E501

        Price of depth without precision consolidation  # noqa: E501

        :return: The price of this PricePoint.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PricePoint.

        Price of depth without precision consolidation  # noqa: E501

        :param price: The price of this PricePoint.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def amount(self):
        """Gets the amount of this PricePoint.  # noqa: E501

        Amount of all the unfilled orders  # noqa: E501

        :return: The amount of this PricePoint.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PricePoint.

        Amount of all the unfilled orders  # noqa: E501

        :param amount: The amount of this PricePoint.  # noqa: E501
        :type: str
        """

        self._amount = amount

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
        if issubclass(PricePoint, dict):
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
        if not isinstance(other, PricePoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
