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


class StatusesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_status(self, **kwargs):  # noqa: E501
        """Adds a new Status.  # noqa: E501

        Adds a new Status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddStatusRequest body:
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_status_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new Status.  # noqa: E501

        Adds a new Status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddStatusRequest body:
        :return: StatusImpl
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
                    " to method add_status" % key
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
            '/statuses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_statuses(self, **kwargs):  # noqa: E501
        """Adds multiple statuses in one go.  # noqa: E501

        Adds multiple statuses in one go.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_statuses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[AddStatusRequest] body:
        :return: list[StatusImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_statuses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_statuses_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_statuses_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple statuses in one go.  # noqa: E501

        Adds multiple statuses in one go.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_statuses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[AddStatusRequest] body:
        :return: list[StatusImpl]
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
                    " to method add_statuses" % key
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
            '/statuses/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[StatusImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_status(self, status_id, **kwargs):  # noqa: E501
        """Changes the status with the information that is present in the request.  # noqa: E501

        Changes the status with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_status(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_id: The unique identifier of the status. (required)
        :param ChangeStatusRequest body:
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_status_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_status_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def change_status_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """Changes the status with the information that is present in the request.  # noqa: E501

        Changes the status with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_status_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_id: The unique identifier of the status. (required)
        :param ChangeStatusRequest body:
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if ('status_id' not in params or
                params['status_id'] is None):
            raise ValueError("Missing the required parameter `status_id` when calling `change_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status_id' in params:
            path_params['statusId'] = params['status_id']  # noqa: E501

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
            '/statuses/{statusId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_statuses(self, **kwargs):  # noqa: E501
        """Changes multiple statuses in one go.  # noqa: E501

        Changes multiple statuses in one go.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_statuses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ChangeStatusRequest] body:
        :return: list[StatusImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_statuses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.change_statuses_with_http_info(**kwargs)  # noqa: E501
            return data

    def change_statuses_with_http_info(self, **kwargs):  # noqa: E501
        """Changes multiple statuses in one go.  # noqa: E501

        Changes multiple statuses in one go.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_statuses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ChangeStatusRequest] body:
        :return: list[StatusImpl]
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
                    " to method change_statuses" % key
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
            '/statuses/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[StatusImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_statuses(self, **kwargs):  # noqa: E501
        """Returns statuses matching the given search criteria.  # noqa: E501

        Returns statuses matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned statuses satisfy all constraints that are specified in this search criteria. By default a result containing 1000 statuses is returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_statuses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000.
        :param int count_limit: Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped
        :param str name: The name of the Status to search for.
        :param str name_match_mode: The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive.
        :param str description: The description of the Status to search for.
        :return: StatusPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_statuses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.find_statuses_with_http_info(**kwargs)  # noqa: E501
            return data

    def find_statuses_with_http_info(self, **kwargs):  # noqa: E501
        """Returns statuses matching the given search criteria.  # noqa: E501

        Returns statuses matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned statuses satisfy all constraints that are specified in this search criteria. By default a result containing 1000 statuses is returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_statuses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000.
        :param int count_limit: Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped
        :param str name: The name of the Status to search for.
        :param str name_match_mode: The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive.
        :param str description: The description of the Status to search for.
        :return: StatusPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'count_limit', 'name', 'name_match_mode', 'description']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_statuses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'count_limit' in params:
            query_params.append(('countLimit', params['count_limit']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name_match_mode' in params:
            query_params.append(('nameMatchMode', params['name_match_mode']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501

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
            '/statuses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusPagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status(self, status_id, **kwargs):  # noqa: E501
        """Returns the Status identified by the given id.  # noqa: E501

        Returns the Status identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_id: The <code>id</code> of the Status (required)
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def get_status_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """Returns the Status identified by the given id.  # noqa: E501

        Returns the Status identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_id: The <code>id</code> of the Status (required)
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if ('status_id' not in params or
                params['status_id'] is None):
            raise ValueError("Missing the required parameter `status_id` when calling `get_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status_id' in params:
            path_params['statusId'] = params['status_id']  # noqa: E501

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
            '/statuses/{statusId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status_by_name(self, status_name, **kwargs):  # noqa: E501
        """Returns the Status identified by the given name.  # noqa: E501

        Returns the Status identified by the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_by_name(status_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_name: The name that identifies the Status. (required)
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_by_name_with_http_info(status_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_by_name_with_http_info(status_name, **kwargs)  # noqa: E501
            return data

    def get_status_by_name_with_http_info(self, status_name, **kwargs):  # noqa: E501
        """Returns the Status identified by the given name.  # noqa: E501

        Returns the Status identified by the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_by_name_with_http_info(status_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_name: The name that identifies the Status. (required)
        :return: StatusImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_name' is set
        if ('status_name' not in params or
                params['status_name'] is None):
            raise ValueError("Missing the required parameter `status_name` when calling `get_status_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status_name' in params:
            path_params['statusName'] = params['status_name']  # noqa: E501

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
            '/statuses/name/{statusName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_status(self, status_id, **kwargs):  # noqa: E501
        """Removes the Status identified by the given id.  # noqa: E501

        Removes the Status identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_status(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_id: The <code>id</code> of the Status. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_status_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_status_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def remove_status_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """Removes the Status identified by the given id.  # noqa: E501

        Removes the Status identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_status_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_id: The <code>id</code> of the Status. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if ('status_id' not in params or
                params['status_id'] is None):
            raise ValueError("Missing the required parameter `status_id` when calling `remove_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status_id' in params:
            path_params['statusId'] = params['status_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/statuses/{statusId}', 'DELETE',
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

    def remove_statuses(self, **kwargs):  # noqa: E501
        """Removes multiple statuses.  # noqa: E501

        Removes multiple statuses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_statuses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: The indentifiers of the Statuses.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_statuses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_statuses_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_statuses_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple statuses.  # noqa: E501

        Removes multiple statuses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_statuses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: The indentifiers of the Statuses.
        :return: None
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
                    " to method remove_statuses" % key
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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/statuses/bulk', 'DELETE',
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
