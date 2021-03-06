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


class BlockQueryBlockMeta(object):
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
        'header': 'BlockHeader',
        'block_id': 'BlockID'
    }

    attribute_map = {
        'header': 'header',
        'block_id': 'block_id'
    }

    def __init__(self, header=None, block_id=None):  # noqa: E501
        """BlockQueryBlockMeta - a model defined in Swagger"""  # noqa: E501

        self._header = None
        self._block_id = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if block_id is not None:
            self.block_id = block_id

    @property
    def header(self):
        """Gets the header of this BlockQueryBlockMeta.  # noqa: E501


        :return: The header of this BlockQueryBlockMeta.  # noqa: E501
        :rtype: BlockHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this BlockQueryBlockMeta.


        :param header: The header of this BlockQueryBlockMeta.  # noqa: E501
        :type: BlockHeader
        """

        self._header = header

    @property
    def block_id(self):
        """Gets the block_id of this BlockQueryBlockMeta.  # noqa: E501


        :return: The block_id of this BlockQueryBlockMeta.  # noqa: E501
        :rtype: BlockID
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this BlockQueryBlockMeta.


        :param block_id: The block_id of this BlockQueryBlockMeta.  # noqa: E501
        :type: BlockID
        """

        self._block_id = block_id

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
        if issubclass(BlockQueryBlockMeta, dict):
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
        if not isinstance(other, BlockQueryBlockMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
