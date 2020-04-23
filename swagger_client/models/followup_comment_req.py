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


class FollowupCommentReq(object):
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
        'token': 'str',
        'donation': 'str',
        'title': 'str',
        'content': 'str',
        'content_type': 'int',
        'id_rewarded': 'str',
        'reward_target': 'str',
        'reward_token': 'str',
        'reward_amount': 'str',
        'attitudes': 'list[int]'
    }

    attribute_map = {
        'base_req': 'base_req',
        'token': 'token',
        'donation': 'donation',
        'title': 'title',
        'content': 'content',
        'content_type': 'content_type',
        'id_rewarded': 'id_rewarded',
        'reward_target': 'reward_target',
        'reward_token': 'reward_token',
        'reward_amount': 'reward_amount',
        'attitudes': 'attitudes'
    }

    def __init__(self, base_req=None, token=None, donation=None, title=None, content=None, content_type=None, id_rewarded=None, reward_target=None, reward_token=None, reward_amount=None, attitudes=None):  # noqa: E501
        """FollowupCommentReq - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._token = None
        self._donation = None
        self._title = None
        self._content = None
        self._content_type = None
        self._id_rewarded = None
        self._reward_target = None
        self._reward_token = None
        self._reward_amount = None
        self._attitudes = None
        self.discriminator = None

        if base_req is not None:
            self.base_req = base_req
        if token is not None:
            self.token = token
        if donation is not None:
            self.donation = donation
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if content_type is not None:
            self.content_type = content_type
        if id_rewarded is not None:
            self.id_rewarded = id_rewarded
        if reward_target is not None:
            self.reward_target = reward_target
        if reward_token is not None:
            self.reward_token = reward_token
        if reward_amount is not None:
            self.reward_amount = reward_amount
        if attitudes is not None:
            self.attitudes = attitudes

    @property
    def base_req(self):
        """Gets the base_req of this FollowupCommentReq.  # noqa: E501


        :return: The base_req of this FollowupCommentReq.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this FollowupCommentReq.


        :param base_req: The base_req of this FollowupCommentReq.  # noqa: E501
        :type: BaseReq
        """

        self._base_req = base_req

    @property
    def token(self):
        """Gets the token of this FollowupCommentReq.  # noqa: E501


        :return: The token of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this FollowupCommentReq.


        :param token: The token of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def donation(self):
        """Gets the donation of this FollowupCommentReq.  # noqa: E501


        :return: The donation of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._donation

    @donation.setter
    def donation(self, donation):
        """Sets the donation of this FollowupCommentReq.


        :param donation: The donation of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._donation = donation

    @property
    def title(self):
        """Gets the title of this FollowupCommentReq.  # noqa: E501


        :return: The title of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FollowupCommentReq.


        :param title: The title of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this FollowupCommentReq.  # noqa: E501


        :return: The content of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FollowupCommentReq.


        :param content: The content of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_type(self):
        """Gets the content_type of this FollowupCommentReq.  # noqa: E501


        :return: The content_type of this FollowupCommentReq.  # noqa: E501
        :rtype: int
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FollowupCommentReq.


        :param content_type: The content_type of this FollowupCommentReq.  # noqa: E501
        :type: int
        """

        self._content_type = content_type

    @property
    def id_rewarded(self):
        """Gets the id_rewarded of this FollowupCommentReq.  # noqa: E501


        :return: The id_rewarded of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._id_rewarded

    @id_rewarded.setter
    def id_rewarded(self, id_rewarded):
        """Sets the id_rewarded of this FollowupCommentReq.


        :param id_rewarded: The id_rewarded of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._id_rewarded = id_rewarded

    @property
    def reward_target(self):
        """Gets the reward_target of this FollowupCommentReq.  # noqa: E501


        :return: The reward_target of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._reward_target

    @reward_target.setter
    def reward_target(self, reward_target):
        """Sets the reward_target of this FollowupCommentReq.


        :param reward_target: The reward_target of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._reward_target = reward_target

    @property
    def reward_token(self):
        """Gets the reward_token of this FollowupCommentReq.  # noqa: E501


        :return: The reward_token of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._reward_token

    @reward_token.setter
    def reward_token(self, reward_token):
        """Sets the reward_token of this FollowupCommentReq.


        :param reward_token: The reward_token of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._reward_token = reward_token

    @property
    def reward_amount(self):
        """Gets the reward_amount of this FollowupCommentReq.  # noqa: E501


        :return: The reward_amount of this FollowupCommentReq.  # noqa: E501
        :rtype: str
        """
        return self._reward_amount

    @reward_amount.setter
    def reward_amount(self, reward_amount):
        """Sets the reward_amount of this FollowupCommentReq.


        :param reward_amount: The reward_amount of this FollowupCommentReq.  # noqa: E501
        :type: str
        """

        self._reward_amount = reward_amount

    @property
    def attitudes(self):
        """Gets the attitudes of this FollowupCommentReq.  # noqa: E501


        :return: The attitudes of this FollowupCommentReq.  # noqa: E501
        :rtype: list[int]
        """
        return self._attitudes

    @attitudes.setter
    def attitudes(self, attitudes):
        """Sets the attitudes of this FollowupCommentReq.


        :param attitudes: The attitudes of this FollowupCommentReq.  # noqa: E501
        :type: list[int]
        """

        self._attitudes = attitudes

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
        if issubclass(FollowupCommentReq, dict):
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
        if not isinstance(other, FollowupCommentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other