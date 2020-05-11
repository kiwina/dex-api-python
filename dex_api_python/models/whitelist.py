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


class Whitelist(object):
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
        'whitelist': 'list[Address]'
    }

    attribute_map = {
        'base_req': 'base_req',
        'whitelist': 'whitelist'
    }

    def __init__(self, base_req=None, whitelist=None):  # noqa: E501
        """Whitelist - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._whitelist = None
        self.discriminator = None

        self.base_req = base_req
        self.whitelist = whitelist

    @property
    def base_req(self):
        """Gets the base_req of this Whitelist.  # noqa: E501


        :return: The base_req of this Whitelist.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this Whitelist.


        :param base_req: The base_req of this Whitelist.  # noqa: E501
        :type: BaseReq
        """
        if base_req is None:
            raise ValueError("Invalid value for `base_req`, must not be `None`")  # noqa: E501

        self._base_req = base_req

    @property
    def whitelist(self):
        """Gets the whitelist of this Whitelist.  # noqa: E501


        :return: The whitelist of this Whitelist.  # noqa: E501
        :rtype: list[Address]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this Whitelist.


        :param whitelist: The whitelist of this Whitelist.  # noqa: E501
        :type: list[Address]
        """
        if whitelist is None:
            raise ValueError("Invalid value for `whitelist`, must not be `None`")  # noqa: E501

        self._whitelist = whitelist

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
        if issubclass(Whitelist, dict):
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
        if not isinstance(other, Whitelist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
