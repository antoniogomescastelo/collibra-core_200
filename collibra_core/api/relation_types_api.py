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


class RelationTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_relation_type(self, **kwargs):  # noqa: E501
        """Adds a new relation type.  # noqa: E501

        Adds a new relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_relation_type(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddRelationTypeRequest body:
        :return: RelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_relation_type_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_relation_type_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_relation_type_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new relation type.  # noqa: E501

        Adds a new relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_relation_type_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddRelationTypeRequest body:
        :return: RelationTypeImpl
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
                    " to method add_relation_type" % key
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
            '/relationTypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_relation_types(self, **kwargs):  # noqa: E501
        """Adds multiple new relation type.  # noqa: E501

        Adds multiple new relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_relation_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[AddRelationTypeRequest] body:
        :return: list[RelationTypeImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_relation_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_relation_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_relation_types_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple new relation type.  # noqa: E501

        Adds multiple new relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_relation_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[AddRelationTypeRequest] body:
        :return: list[RelationTypeImpl]
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
                    " to method add_relation_types" % key
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
            '/relationTypes/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RelationTypeImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_relation_type(self, relation_type_id, **kwargs):  # noqa: E501
        """Changes the relation type.  # noqa: E501

        Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_relation_type(relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type_id: The unique identifier of the relationType (required)
        :param ChangeRelationTypeRequest body:
        :return: RelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_relation_type_with_http_info(relation_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_relation_type_with_http_info(relation_type_id, **kwargs)  # noqa: E501
            return data

    def change_relation_type_with_http_info(self, relation_type_id, **kwargs):  # noqa: E501
        """Changes the relation type.  # noqa: E501

        Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_relation_type_with_http_info(relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type_id: The unique identifier of the relationType (required)
        :param ChangeRelationTypeRequest body:
        :return: RelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_relation_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type_id' is set
        if ('relation_type_id' not in params or
                params['relation_type_id'] is None):
            raise ValueError("Missing the required parameter `relation_type_id` when calling `change_relation_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type_id' in params:
            path_params['relationTypeId'] = params['relation_type_id']  # noqa: E501

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
            '/relationTypes/{relationTypeId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_relation_types(self, **kwargs):  # noqa: E501
        """Changes the relation types.  # noqa: E501

        Changes the relation types with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_relation_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ChangeRelationTypeRequest] body:
        :return: list[RelationTypeImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_relation_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.change_relation_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def change_relation_types_with_http_info(self, **kwargs):  # noqa: E501
        """Changes the relation types.  # noqa: E501

        Changes the relation types with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_relation_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ChangeRelationTypeRequest] body:
        :return: list[RelationTypeImpl]
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
                    " to method change_relation_types" % key
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
            '/relationTypes/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RelationTypeImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_relation_types(self, **kwargs):  # noqa: E501
        """Finds all the relation types matching the given criteria.  # noqa: E501

        Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_relation_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000.
        :param int count_limit: Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped
        :param str source_type_id: The ID of the source type of the Relation Type to search for.
        :param str source_type_name: The name of the source type of the Relation Type to search for.
        :param str role: The name of the role that the source plays to search for.
        :param str target_type_id: The ID of the target type of the Relation Type to search for.
        :param str target_type_name: The name of the target type of the Relation Type to search for.
        :param str co_role: The name of the role that the target plays to search for.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param str role_co_role_logical_operator: The logical operator determining how to combine the role and coRole criteria: AND or OR.
        :return: RelationTypePagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_relation_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.find_relation_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def find_relation_types_with_http_info(self, **kwargs):  # noqa: E501
        """Finds all the relation types matching the given criteria.  # noqa: E501

        Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_relation_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000.
        :param int count_limit: Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped
        :param str source_type_id: The ID of the source type of the Relation Type to search for.
        :param str source_type_name: The name of the source type of the Relation Type to search for.
        :param str role: The name of the role that the source plays to search for.
        :param str target_type_id: The ID of the target type of the Relation Type to search for.
        :param str target_type_name: The name of the target type of the Relation Type to search for.
        :param str co_role: The name of the role that the target plays to search for.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param str role_co_role_logical_operator: The logical operator determining how to combine the role and coRole criteria: AND or OR.
        :return: RelationTypePagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'count_limit', 'source_type_id', 'source_type_name', 'role', 'target_type_id', 'target_type_name', 'co_role', 'sort_field', 'sort_order', 'role_co_role_logical_operator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_relation_types" % key
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
        if 'source_type_id' in params:
            query_params.append(('sourceTypeId', params['source_type_id']))  # noqa: E501
        if 'source_type_name' in params:
            query_params.append(('sourceTypeName', params['source_type_name']))  # noqa: E501
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501
        if 'target_type_id' in params:
            query_params.append(('targetTypeId', params['target_type_id']))  # noqa: E501
        if 'target_type_name' in params:
            query_params.append(('targetTypeName', params['target_type_name']))  # noqa: E501
        if 'co_role' in params:
            query_params.append(('coRole', params['co_role']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'role_co_role_logical_operator' in params:
            query_params.append(('roleCoRoleLogicalOperator', params['role_co_role_logical_operator']))  # noqa: E501

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
            '/relationTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelationTypePagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_relation_type(self, relation_type_id, **kwargs):  # noqa: E501
        """Returns relation type identified by given UUID.  # noqa: E501

        Returns relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_relation_type(relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type_id: The unique identifier of the relationType (required)
        :return: RelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_relation_type_with_http_info(relation_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_relation_type_with_http_info(relation_type_id, **kwargs)  # noqa: E501
            return data

    def get_relation_type_with_http_info(self, relation_type_id, **kwargs):  # noqa: E501
        """Returns relation type identified by given UUID.  # noqa: E501

        Returns relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_relation_type_with_http_info(relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type_id: The unique identifier of the relationType (required)
        :return: RelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_relation_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type_id' is set
        if ('relation_type_id' not in params or
                params['relation_type_id'] is None):
            raise ValueError("Missing the required parameter `relation_type_id` when calling `get_relation_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type_id' in params:
            path_params['relationTypeId'] = params['relation_type_id']  # noqa: E501

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
            '/relationTypes/{relationTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_relation_type(self, relation_type_id, **kwargs):  # noqa: E501
        """Removes relation type identified by given UUID.  # noqa: E501

        Removes relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_relation_type(relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type_id: The unique identifier of the relationType (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_relation_type_with_http_info(relation_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_relation_type_with_http_info(relation_type_id, **kwargs)  # noqa: E501
            return data

    def remove_relation_type_with_http_info(self, relation_type_id, **kwargs):  # noqa: E501
        """Removes relation type identified by given UUID.  # noqa: E501

        Removes relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_relation_type_with_http_info(relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type_id: The unique identifier of the relationType (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_relation_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type_id' is set
        if ('relation_type_id' not in params or
                params['relation_type_id'] is None):
            raise ValueError("Missing the required parameter `relation_type_id` when calling `remove_relation_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type_id' in params:
            path_params['relationTypeId'] = params['relation_type_id']  # noqa: E501

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
            '/relationTypes/{relationTypeId}', 'DELETE',
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

    def remove_relation_types(self, **kwargs):  # noqa: E501
        """Removes multiple relation types.  # noqa: E501

        Removes multiple relation types identified by the UUIDs passed as parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_relation_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: The unique identifiers of the relationTypes
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_relation_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_relation_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_relation_types_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple relation types.  # noqa: E501

        Removes multiple relation types identified by the UUIDs passed as parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_relation_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: The unique identifiers of the relationTypes
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
                    " to method remove_relation_types" % key
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
            '/relationTypes/bulk', 'DELETE',
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
