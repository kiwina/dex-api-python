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


class AliasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_address_from_alias(self, alias, **kwargs):  # noqa: E501
        """Given an alias, query the corresponding address  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_from_alias(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: The alias to be queried (required)
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_from_alias_with_http_info(alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_from_alias_with_http_info(alias, **kwargs)  # noqa: E501
            return data

    def get_address_from_alias_with_http_info(self, alias, **kwargs):  # noqa: E501
        """Given an alias, query the corresponding address  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_from_alias_with_http_info(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: The alias to be queried (required)
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_from_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `get_address_from_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alias/address-of-alias/{alias}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alias_params(self, **kwargs):  # noqa: E501
        """Get the current alias parameters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alias_params(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20050
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alias_params_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_alias_params_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_alias_params_with_http_info(self, **kwargs):  # noqa: E501
        """Get the current alias parameters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alias_params_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20050
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
                    " to method get_alias_params" % key
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
            '/alias/parameters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20050',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_aliases_from_address(self, address, **kwargs):  # noqa: E501
        """Given an account's address, query all the corresponding aliases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_aliases_from_address(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: The account's address to be queried (required)
        :return: InlineResponse20049
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_aliases_from_address_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_aliases_from_address_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_aliases_from_address_with_http_info(self, address, **kwargs):  # noqa: E501
        """Given an account's address, query all the corresponding aliases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_aliases_from_address_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: The account's address to be queried (required)
        :return: InlineResponse20049
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aliases_from_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_aliases_from_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alias/aliases-of-address/{address}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20049',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_alias(self, alias_update_req, **kwargs):  # noqa: E501
        """Add or remove alias for an address  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_alias(alias_update_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AliasUpdateReq alias_update_req: update an address's aliases (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_alias_with_http_info(alias_update_req, **kwargs)  # noqa: E501
        else:
            (data) = self.update_alias_with_http_info(alias_update_req, **kwargs)  # noqa: E501
            return data

    def update_alias_with_http_info(self, alias_update_req, **kwargs):  # noqa: E501
        """Add or remove alias for an address  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_alias_with_http_info(alias_update_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AliasUpdateReq alias_update_req: update an address's aliases (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias_update_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alias_update_req' is set
        if ('alias_update_req' not in params or
                params['alias_update_req'] is None):
            raise ValueError("Missing the required parameter `alias_update_req` when calling `update_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'alias_update_req' in params:
            body_params = params['alias_update_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alias/update', 'POST',
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