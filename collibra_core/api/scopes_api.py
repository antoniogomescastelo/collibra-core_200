# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from collibra_core.api_client import ApiClient


class ScopesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_scope(self, **kwargs):  # noqa: E501
        """Add scope  # noqa: E501

        Adds a new scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_scope(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddScopeRequest body: the properties of the scope to be added
        :return: ScopeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_scope_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_scope_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_scope_with_http_info(self, **kwargs):  # noqa: E501
        """Add scope  # noqa: E501

        Adds a new scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_scope_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddScopeRequest body: the properties of the scope to be added
        :return: ScopeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_scope" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/scopes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScopeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_scope(self, scope_id, **kwargs):  # noqa: E501
        """Change scope  # noqa: E501

        Changes the scope with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_scope(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: the id of the scope to be changed (required)
        :param ChangeScopeRequest body: the properties of the scope to be changed
        :return: ScopeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_scope_with_http_info(scope_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_scope_with_http_info(scope_id, **kwargs)  # noqa: E501
            return data

    def change_scope_with_http_info(self, scope_id, **kwargs):  # noqa: E501
        """Change scope  # noqa: E501

        Changes the scope with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_scope_with_http_info(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: the id of the scope to be changed (required)
        :param ChangeScopeRequest body: the properties of the scope to be changed
        :return: ScopeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_scope" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `change_scope`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/scopes/{scopeId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScopeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_scopes(self, **kwargs):  # noqa: E501
        """Find scopes  # noqa: E501

        Returns all scopes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_scopes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ScopePagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_scopes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_scopes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_scopes_with_http_info(self, **kwargs):  # noqa: E501
        """Find scopes  # noqa: E501

        Returns all scopes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_scopes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ScopePagedResponse
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
                    " to method get_all_scopes" % key
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
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/scopes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScopePagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scope(self, scope_id, **kwargs):  # noqa: E501
        """Get scope  # noqa: E501

        Returns scope identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scope(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The unique identifier of the scope. (required)
        :return: ScopeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scope_with_http_info(scope_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scope_with_http_info(scope_id, **kwargs)  # noqa: E501
            return data

    def get_scope_with_http_info(self, scope_id, **kwargs):  # noqa: E501
        """Get scope  # noqa: E501

        Returns scope identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scope_with_http_info(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The unique identifier of the scope. (required)
        :return: ScopeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scope" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `get_scope`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/scopes/{scopeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScopeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_scope(self, scope_id, **kwargs):  # noqa: E501
        """Remove scope  # noqa: E501

        Removes scope identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_scope(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: the id of the scope (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_scope_with_http_info(scope_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_scope_with_http_info(scope_id, **kwargs)  # noqa: E501
            return data

    def remove_scope_with_http_info(self, scope_id, **kwargs):  # noqa: E501
        """Remove scope  # noqa: E501

        Removes scope identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_scope_with_http_info(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: the id of the scope (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_scope" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `remove_scope`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/scopes/{scopeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
