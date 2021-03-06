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


class TextProposal(object):
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
        'id': 'str',
        'content': 'TextProposalContent',
        'deposit_end_time': 'str',
        'proposal_status': 'str',
        'final_tally_result': 'TallyResult',
        'submit_time': 'str',
        'total_deposit': 'list[Coin]',
        'voting_start_time': 'str',
        'voting_end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'content': 'content',
        'deposit_end_time': 'deposit_end_time',
        'proposal_status': 'proposal_status',
        'final_tally_result': 'final_tally_result',
        'submit_time': 'submit_time',
        'total_deposit': 'total_deposit',
        'voting_start_time': 'voting_start_time',
        'voting_end_time': 'voting_end_time'
    }

    def __init__(self, id=None, content=None, deposit_end_time=None, proposal_status=None, final_tally_result=None, submit_time=None, total_deposit=None, voting_start_time=None, voting_end_time=None):  # noqa: E501
        """TextProposal - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._content = None
        self._deposit_end_time = None
        self._proposal_status = None
        self._final_tally_result = None
        self._submit_time = None
        self._total_deposit = None
        self._voting_start_time = None
        self._voting_end_time = None
        self.discriminator = None

        self.id = id
        self.content = content
        self.deposit_end_time = deposit_end_time
        self.proposal_status = proposal_status
        self.final_tally_result = final_tally_result
        self.submit_time = submit_time
        self.total_deposit = total_deposit
        self.voting_start_time = voting_start_time
        self.voting_end_time = voting_end_time

    @property
    def id(self):
        """Gets the id of this TextProposal.  # noqa: E501


        :return: The id of this TextProposal.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TextProposal.


        :param id: The id of this TextProposal.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def content(self):
        """Gets the content of this TextProposal.  # noqa: E501


        :return: The content of this TextProposal.  # noqa: E501
        :rtype: TextProposalContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TextProposal.


        :param content: The content of this TextProposal.  # noqa: E501
        :type: TextProposalContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def deposit_end_time(self):
        """Gets the deposit_end_time of this TextProposal.  # noqa: E501


        :return: The deposit_end_time of this TextProposal.  # noqa: E501
        :rtype: str
        """
        return self._deposit_end_time

    @deposit_end_time.setter
    def deposit_end_time(self, deposit_end_time):
        """Sets the deposit_end_time of this TextProposal.


        :param deposit_end_time: The deposit_end_time of this TextProposal.  # noqa: E501
        :type: str
        """
        if deposit_end_time is None:
            raise ValueError("Invalid value for `deposit_end_time`, must not be `None`")  # noqa: E501

        self._deposit_end_time = deposit_end_time

    @property
    def proposal_status(self):
        """Gets the proposal_status of this TextProposal.  # noqa: E501


        :return: The proposal_status of this TextProposal.  # noqa: E501
        :rtype: str
        """
        return self._proposal_status

    @proposal_status.setter
    def proposal_status(self, proposal_status):
        """Sets the proposal_status of this TextProposal.


        :param proposal_status: The proposal_status of this TextProposal.  # noqa: E501
        :type: str
        """
        if proposal_status is None:
            raise ValueError("Invalid value for `proposal_status`, must not be `None`")  # noqa: E501

        self._proposal_status = proposal_status

    @property
    def final_tally_result(self):
        """Gets the final_tally_result of this TextProposal.  # noqa: E501


        :return: The final_tally_result of this TextProposal.  # noqa: E501
        :rtype: TallyResult
        """
        return self._final_tally_result

    @final_tally_result.setter
    def final_tally_result(self, final_tally_result):
        """Sets the final_tally_result of this TextProposal.


        :param final_tally_result: The final_tally_result of this TextProposal.  # noqa: E501
        :type: TallyResult
        """
        if final_tally_result is None:
            raise ValueError("Invalid value for `final_tally_result`, must not be `None`")  # noqa: E501

        self._final_tally_result = final_tally_result

    @property
    def submit_time(self):
        """Gets the submit_time of this TextProposal.  # noqa: E501


        :return: The submit_time of this TextProposal.  # noqa: E501
        :rtype: str
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this TextProposal.


        :param submit_time: The submit_time of this TextProposal.  # noqa: E501
        :type: str
        """
        if submit_time is None:
            raise ValueError("Invalid value for `submit_time`, must not be `None`")  # noqa: E501

        self._submit_time = submit_time

    @property
    def total_deposit(self):
        """Gets the total_deposit of this TextProposal.  # noqa: E501


        :return: The total_deposit of this TextProposal.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._total_deposit

    @total_deposit.setter
    def total_deposit(self, total_deposit):
        """Sets the total_deposit of this TextProposal.


        :param total_deposit: The total_deposit of this TextProposal.  # noqa: E501
        :type: list[Coin]
        """
        if total_deposit is None:
            raise ValueError("Invalid value for `total_deposit`, must not be `None`")  # noqa: E501

        self._total_deposit = total_deposit

    @property
    def voting_start_time(self):
        """Gets the voting_start_time of this TextProposal.  # noqa: E501


        :return: The voting_start_time of this TextProposal.  # noqa: E501
        :rtype: str
        """
        return self._voting_start_time

    @voting_start_time.setter
    def voting_start_time(self, voting_start_time):
        """Sets the voting_start_time of this TextProposal.


        :param voting_start_time: The voting_start_time of this TextProposal.  # noqa: E501
        :type: str
        """
        if voting_start_time is None:
            raise ValueError("Invalid value for `voting_start_time`, must not be `None`")  # noqa: E501

        self._voting_start_time = voting_start_time

    @property
    def voting_end_time(self):
        """Gets the voting_end_time of this TextProposal.  # noqa: E501


        :return: The voting_end_time of this TextProposal.  # noqa: E501
        :rtype: str
        """
        return self._voting_end_time

    @voting_end_time.setter
    def voting_end_time(self, voting_end_time):
        """Sets the voting_end_time of this TextProposal.


        :param voting_end_time: The voting_end_time of this TextProposal.  # noqa: E501
        :type: str
        """
        if voting_end_time is None:
            raise ValueError("Invalid value for `voting_end_time`, must not be `None`")  # noqa: E501

        self._voting_end_time = voting_end_time

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
        if issubclass(TextProposal, dict):
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
        if not isinstance(other, TextProposal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
