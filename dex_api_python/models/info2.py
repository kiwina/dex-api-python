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


class Info2(object):
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
        'base_req': 'BaseReq',
        'trading_pair': 'str',
        'time': 'str'
    }

    attribute_map = {
        'base_req': 'base_req',
        'trading_pair': 'trading_pair',
        'time': 'time'
    }

    def __init__(self, base_req=None, trading_pair=None, time=None):  # noqa: E501
        """Info2 - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._trading_pair = None
        self._time = None
        self.discriminator = None

        self.base_req = base_req
        self.trading_pair = trading_pair
        self.time = time

    @property
    def base_req(self):
        """Gets the base_req of this Info2.  # noqa: E501


        :return: The base_req of this Info2.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this Info2.


        :param base_req: The base_req of this Info2.  # noqa: E501
        :type: BaseReq
        """
        if base_req is None:
            raise ValueError("Invalid value for `base_req`, must not be `None`")  # noqa: E501

        self._base_req = base_req

    @property
    def trading_pair(self):
        """Gets the trading_pair of this Info2.  # noqa: E501


        :return: The trading_pair of this Info2.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this Info2.


        :param trading_pair: The trading_pair of this Info2.  # noqa: E501
        :type: str
        """
        if trading_pair is None:
            raise ValueError("Invalid value for `trading_pair`, must not be `None`")  # noqa: E501

        self._trading_pair = trading_pair

    @property
    def time(self):
        """Gets the time of this Info2.  # noqa: E501


        :return: The time of this Info2.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Info2.


        :param time: The time of this Info2.  # noqa: E501
        :type: str
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if issubclass(Info2, dict):
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
        if not isinstance(other, Info2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
