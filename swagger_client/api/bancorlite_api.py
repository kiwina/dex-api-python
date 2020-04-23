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

from swagger_client.api_client import ApiClient


class BancorliteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bancor_cancel(self, bancor_cancel, **kwargs):  # noqa: E501
        """cancel bancor  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bancor_cancel(bancor_cancel, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BancorCancel bancor_cancel: cancel bancor (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bancor_cancel_with_http_info(bancor_cancel, **kwargs)  # noqa: E501
        else:
            (data) = self.bancor_cancel_with_http_info(bancor_cancel, **kwargs)  # noqa: E501
            return data

    def bancor_cancel_with_http_info(self, bancor_cancel, **kwargs):  # noqa: E501
        """cancel bancor  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bancor_cancel_with_http_info(bancor_cancel, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BancorCancel bancor_cancel: cancel bancor (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bancor_cancel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bancor_cancel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bancor_cancel' is set
        if ('bancor_cancel' not in params or
                params['bancor_cancel'] is None):
            raise ValueError("Missing the required parameter `bancor_cancel` when calling `bancor_cancel`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bancor_cancel' in params:
            body_params = params['bancor_cancel']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bancorlite/bancor-cancel', 'POST',
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

    def bancor_init(self, bancor_init, **kwargs):  # noqa: E501
        """create bancor  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bancor_init(bancor_init, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BancorInit bancor_init: create bancor (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bancor_init_with_http_info(bancor_init, **kwargs)  # noqa: E501
        else:
            (data) = self.bancor_init_with_http_info(bancor_init, **kwargs)  # noqa: E501
            return data

    def bancor_init_with_http_info(self, bancor_init, **kwargs):  # noqa: E501
        """create bancor  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bancor_init_with_http_info(bancor_init, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BancorInit bancor_init: create bancor (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bancor_init']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bancor_init" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bancor_init' is set
        if ('bancor_init' not in params or
                params['bancor_init'] is None):
            raise ValueError("Missing the required parameter `bancor_init` when calling `bancor_init`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bancor_init' in params:
            body_params = params['bancor_init']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bancorlite/bancor-init', 'POST',
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

    def bancor_trade(self, bancor_trade, **kwargs):  # noqa: E501
        """trade with bancor  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bancor_trade(bancor_trade, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BancorTrade bancor_trade: trade with bancor (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bancor_trade_with_http_info(bancor_trade, **kwargs)  # noqa: E501
        else:
            (data) = self.bancor_trade_with_http_info(bancor_trade, **kwargs)  # noqa: E501
            return data

    def bancor_trade_with_http_info(self, bancor_trade, **kwargs):  # noqa: E501
        """trade with bancor  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bancor_trade_with_http_info(bancor_trade, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BancorTrade bancor_trade: trade with bancor (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bancor_trade']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bancor_trade" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bancor_trade' is set
        if ('bancor_trade' not in params or
                params['bancor_trade'] is None):
            raise ValueError("Missing the required parameter `bancor_trade` when calling `bancor_trade`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bancor_trade' in params:
            body_params = params['bancor_trade']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bancorlite/bancor-trade', 'POST',
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

    def get_bancor_info(self, symbol, **kwargs):  # noqa: E501
        """get the bancor pool info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bancor_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: stock and money pair (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bancor_info_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bancor_info_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def get_bancor_info_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """get the bancor pool info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bancor_info_with_http_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: stock and money pair (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bancor_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `get_bancor_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []

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
            '/bancorlite/pools/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bancor_infos(self, **kwargs):  # noqa: E501
        """get all bancor infos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bancor_infos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20052
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bancor_infos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_bancor_infos_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_bancor_infos_with_http_info(self, **kwargs):  # noqa: E501
        """get all bancor infos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bancor_infos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20052
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bancor_infos" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/bancorlite/infos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20052',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bancorlite_params(self, **kwargs):  # noqa: E501
        """Get the current bancorlite parameters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bancorlite_params(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20051
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bancorlite_params_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_bancorlite_params_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_bancorlite_params_with_http_info(self, **kwargs):  # noqa: E501
        """Get the current bancorlite parameters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bancorlite_params_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20051
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bancorlite_params" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/bancorlite/parameters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20051',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)