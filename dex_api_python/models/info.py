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


class Info(object):
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
        'url': 'str',
        'description': 'str',
        'identity': 'str',
        'name': 'str',
        'total_supply': 'str',
        'mintable': 'str',
        'burnable': 'str',
        'addr_forbiddable': 'str',
        'token_forbiddable': 'str'
    }

    attribute_map = {
        'base_req': 'base_req',
        'url': 'url',
        'description': 'description',
        'identity': 'identity',
        'name': 'name',
        'total_supply': 'total_supply',
        'mintable': 'mintable',
        'burnable': 'burnable',
        'addr_forbiddable': 'addr_forbiddable',
        'token_forbiddable': 'token_forbiddable'
    }

    def __init__(self, base_req=None, url=None, description=None, identity=None, name=None, total_supply=None, mintable=None, burnable=None, addr_forbiddable=None, token_forbiddable=None):  # noqa: E501
        """Info - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._url = None
        self._description = None
        self._identity = None
        self._name = None
        self._total_supply = None
        self._mintable = None
        self._burnable = None
        self._addr_forbiddable = None
        self._token_forbiddable = None
        self.discriminator = None

        if base_req is not None:
            self.base_req = base_req
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if identity is not None:
            self.identity = identity
        if name is not None:
            self.name = name
        if total_supply is not None:
            self.total_supply = total_supply
        if mintable is not None:
            self.mintable = mintable
        if burnable is not None:
            self.burnable = burnable
        if addr_forbiddable is not None:
            self.addr_forbiddable = addr_forbiddable
        if token_forbiddable is not None:
            self.token_forbiddable = token_forbiddable

    @property
    def base_req(self):
        """Gets the base_req of this Info.  # noqa: E501


        :return: The base_req of this Info.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this Info.


        :param base_req: The base_req of this Info.  # noqa: E501
        :type: BaseReq
        """

        self._base_req = base_req

    @property
    def url(self):
        """Gets the url of this Info.  # noqa: E501


        :return: The url of this Info.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Info.


        :param url: The url of this Info.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this Info.  # noqa: E501


        :return: The description of this Info.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Info.


        :param description: The description of this Info.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def identity(self):
        """Gets the identity of this Info.  # noqa: E501


        :return: The identity of this Info.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this Info.


        :param identity: The identity of this Info.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def name(self):
        """Gets the name of this Info.  # noqa: E501


        :return: The name of this Info.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Info.


        :param name: The name of this Info.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def total_supply(self):
        """Gets the total_supply of this Info.  # noqa: E501


        :return: The total_supply of this Info.  # noqa: E501
        :rtype: str
        """
        return self._total_supply

    @total_supply.setter
    def total_supply(self, total_supply):
        """Sets the total_supply of this Info.


        :param total_supply: The total_supply of this Info.  # noqa: E501
        :type: str
        """

        self._total_supply = total_supply

    @property
    def mintable(self):
        """Gets the mintable of this Info.  # noqa: E501


        :return: The mintable of this Info.  # noqa: E501
        :rtype: str
        """
        return self._mintable

    @mintable.setter
    def mintable(self, mintable):
        """Sets the mintable of this Info.


        :param mintable: The mintable of this Info.  # noqa: E501
        :type: str
        """

        self._mintable = mintable

    @property
    def burnable(self):
        """Gets the burnable of this Info.  # noqa: E501


        :return: The burnable of this Info.  # noqa: E501
        :rtype: str
        """
        return self._burnable

    @burnable.setter
    def burnable(self, burnable):
        """Sets the burnable of this Info.


        :param burnable: The burnable of this Info.  # noqa: E501
        :type: str
        """

        self._burnable = burnable

    @property
    def addr_forbiddable(self):
        """Gets the addr_forbiddable of this Info.  # noqa: E501


        :return: The addr_forbiddable of this Info.  # noqa: E501
        :rtype: str
        """
        return self._addr_forbiddable

    @addr_forbiddable.setter
    def addr_forbiddable(self, addr_forbiddable):
        """Sets the addr_forbiddable of this Info.


        :param addr_forbiddable: The addr_forbiddable of this Info.  # noqa: E501
        :type: str
        """

        self._addr_forbiddable = addr_forbiddable

    @property
    def token_forbiddable(self):
        """Gets the token_forbiddable of this Info.  # noqa: E501


        :return: The token_forbiddable of this Info.  # noqa: E501
        :rtype: str
        """
        return self._token_forbiddable

    @token_forbiddable.setter
    def token_forbiddable(self, token_forbiddable):
        """Sets the token_forbiddable of this Info.


        :param token_forbiddable: The token_forbiddable of this Info.  # noqa: E501
        :type: str
        """

        self._token_forbiddable = token_forbiddable

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
        if issubclass(Info, dict):
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
        if not isinstance(other, Info):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
