# coding: utf-8

"""
    CET-Lite for CoinEx Chain

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dex_api_python.api_client import ApiClient


class CommentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def followup_comment(self, followup_comment_req, **kwargs):  # noqa: E501
        """Post a follow-up comment under some thread  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.followup_comment(followup_comment_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FollowupCommentReq followup_comment_req: Post a follow-up comment (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.followup_comment_with_http_info(followup_comment_req, **kwargs)  # noqa: E501
        else:
            (data) = self.followup_comment_with_http_info(followup_comment_req, **kwargs)  # noqa: E501
            return data

    def followup_comment_with_http_info(self, followup_comment_req, **kwargs):  # noqa: E501
        """Post a follow-up comment under some thread  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.followup_comment_with_http_info(followup_comment_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FollowupCommentReq followup_comment_req: Post a follow-up comment (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['followup_comment_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method followup_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'followup_comment_req' is set
        if ('followup_comment_req' not in params or
                params['followup_comment_req'] is None):
            raise ValueError("Missing the required parameter `followup_comment_req` when calling `followup_comment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'followup_comment_req' in params:
            body_params = params['followup_comment_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/comment/followup-comment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StdTx',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def new_thread(self, new_thread_req, **kwargs):  # noqa: E501
        """Post a new comment to open a new thread  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_thread(new_thread_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewThreadReq new_thread_req: open a new thread (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.new_thread_with_http_info(new_thread_req, **kwargs)  # noqa: E501
        else:
            (data) = self.new_thread_with_http_info(new_thread_req, **kwargs)  # noqa: E501
            return data

    def new_thread_with_http_info(self, new_thread_req, **kwargs):  # noqa: E501
        """Post a new comment to open a new thread  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_thread_with_http_info(new_thread_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewThreadReq new_thread_req: open a new thread (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_thread_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method new_thread" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_thread_req' is set
        if ('new_thread_req' not in params or
                params['new_thread_req'] is None):
            raise ValueError("Missing the required parameter `new_thread_req` when calling `new_thread`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_thread_req' in params:
            body_params = params['new_thread_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/comment/new-thread', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StdTx',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_comment(self, token, time, sid, count, **kwargs):  # noqa: E501
        """Query token comment  # noqa: E501

        Query all comments about given token until to time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_comment(token, time, sid, count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Symbol (required)
        :param int time: Unix timestamp (required)
        :param int sid: Sequence id (required)
        :param int count: Querier comment count limited to 1024 (required)
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_comment_with_http_info(token, time, sid, count, **kwargs)  # noqa: E501
        else:
            (data) = self.query_comment_with_http_info(token, time, sid, count, **kwargs)  # noqa: E501
            return data

    def query_comment_with_http_info(self, token, time, sid, count, **kwargs):  # noqa: E501
        """Query token comment  # noqa: E501

        Query all comments about given token until to time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_comment_with_http_info(token, time, sid, count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Symbol (required)
        :param int time: Unix timestamp (required)
        :param int sid: Sequence id (required)
        :param int count: Querier comment count limited to 1024 (required)
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'time', 'sid', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `query_comment`")  # noqa: E501
        # verify the required parameter 'time' is set
        if ('time' not in params or
                params['time'] is None):
            raise ValueError("Missing the required parameter `time` when calling `query_comment`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `query_comment`")  # noqa: E501
        # verify the required parameter 'count' is set
        if ('count' not in params or
                params['count'] is None):
            raise ValueError("Missing the required parameter `count` when calling `query_comment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'sid' in params:
            query_params.append(('sid', params['sid']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/comment/comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20063',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reward_comments(self, reward_comments_req, **kwargs):  # noqa: E501
        """reward some comments with coins  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reward_comments(reward_comments_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RewardCommentsReq reward_comments_req: reward some comments (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reward_comments_with_http_info(reward_comments_req, **kwargs)  # noqa: E501
        else:
            (data) = self.reward_comments_with_http_info(reward_comments_req, **kwargs)  # noqa: E501
            return data

    def reward_comments_with_http_info(self, reward_comments_req, **kwargs):  # noqa: E501
        """reward some comments with coins  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reward_comments_with_http_info(reward_comments_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RewardCommentsReq reward_comments_req: reward some comments (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reward_comments_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reward_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reward_comments_req' is set
        if ('reward_comments_req' not in params or
                params['reward_comments_req'] is None):
            raise ValueError("Missing the required parameter `reward_comments_req` when calling `reward_comments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reward_comments_req' in params:
            body_params = params['reward_comments_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/comment/reward-comments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StdTx',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
