# coding: utf-8

"""
    My Title

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class GroupApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def group_create_group(self, group, **kwargs):
        """
        Create group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_create_group(group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Group group: Group object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.group_create_group_with_http_info(group, **kwargs)
        else:
            (data) = self.group_create_group_with_http_info(group, **kwargs)
            return data

    def group_create_group_with_http_info(self, group, **kwargs):
        """
        Create group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_create_group_with_http_info(group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Group group: Group object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_create_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params) or (params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `group_create_group`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group' in params:
            body_params = params['group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/group', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Group',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def group_get_group(self, group_id, **kwargs):
        """
        Get group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_get_group(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.group_get_group_with_http_info(group_id, **kwargs)
        else:
            (data) = self.group_get_group_with_http_info(group_id, **kwargs)
            return data

    def group_get_group_with_http_info(self, group_id, **kwargs):
        """
        Get group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_get_group_with_http_info(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_get_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `group_get_group`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/group/{groupId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Group',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def group_get_group_avatar(self, group_id, **kwargs):
        """
        Get group avatar
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_get_group_avatar(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param int image_size: Avatar size (all avatars are square - one dimension is enough, default is 256)
        :param str authorization: Authorization header
        :param str e_tag: EntityTag header
        :param str x_impersonate_user: Impersonation header
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.group_get_group_avatar_with_http_info(group_id, **kwargs)
        else:
            (data) = self.group_get_group_avatar_with_http_info(group_id, **kwargs)
            return data

    def group_get_group_avatar_with_http_info(self, group_id, **kwargs):
        """
        Get group avatar
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_get_group_avatar_with_http_info(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param int image_size: Avatar size (all avatars are square - one dimension is enough, default is 256)
        :param str authorization: Authorization header
        :param str e_tag: EntityTag header
        :param str x_impersonate_user: Impersonation header
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'image_size', 'authorization', 'e_tag', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_get_group_avatar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `group_get_group_avatar`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = []
        if 'image_size' in params:
            query_params.append(('imageSize', params['image_size']))

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'e_tag' in params:
            header_params['ETag'] = params['e_tag']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/group/{groupId}/avatar', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def group_get_list_of_groups(self, offset, size, **kwargs):
        """
        Get list of groups
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_get_list_of_groups(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset. (required)
        :param int size: Requested page size. (required)
        :param str search_query: Plaintext search query to filter list of groups by.
        :param list[str] tags: List of tags to filter card list by.
        :param str authorization: Authorization header.
        :param str x_impersonate_user: Impersonation header.
        :return: ListOfResourcesOfGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.group_get_list_of_groups_with_http_info(offset, size, **kwargs)
        else:
            (data) = self.group_get_list_of_groups_with_http_info(offset, size, **kwargs)
            return data

    def group_get_list_of_groups_with_http_info(self, offset, size, **kwargs):
        """
        Get list of groups
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_get_list_of_groups_with_http_info(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset. (required)
        :param int size: Requested page size. (required)
        :param str search_query: Plaintext search query to filter list of groups by.
        :param list[str] tags: List of tags to filter card list by.
        :param str authorization: Authorization header.
        :param str x_impersonate_user: Impersonation header.
        :return: ListOfResourcesOfGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'size', 'search_query', 'tags', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_get_list_of_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `group_get_list_of_groups`")
        # verify the required parameter 'size' is set
        if ('size' not in params) or (params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `group_get_list_of_groups`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'search_query' in params:
            query_params.append(('searchQuery', params['search_query']))
        if 'tags' in params:
            query_params.append(('tags', params['tags']))
            collection_formats['tags'] = 'multi'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/group/list', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListOfResourcesOfGroup',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def group_update_group(self, group_id, group, **kwargs):
        """
        Update group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_update_group(group_id, group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param Group group: Group object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.group_update_group_with_http_info(group_id, group, **kwargs)
        else:
            (data) = self.group_update_group_with_http_info(group_id, group, **kwargs)
            return data

    def group_update_group_with_http_info(self, group_id, group, **kwargs):
        """
        Update group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_update_group_with_http_info(group_id, group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param Group group: Group object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'group', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_update_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `group_update_group`")
        # verify the required parameter 'group' is set
        if ('group' not in params) or (params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `group_update_group`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group' in params:
            body_params = params['group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/group/{groupId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Group',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def group_update_group_avatar(self, group_id, **kwargs):
        """
        Update group avatar
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_update_group_avatar(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param file file: Avatar object
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.group_update_group_avatar_with_http_info(group_id, **kwargs)
        else:
            (data) = self.group_update_group_avatar_with_http_info(group_id, **kwargs)
            return data

    def group_update_group_avatar_with_http_info(self, group_id, **kwargs):
        """
        Update group avatar
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.group_update_group_avatar_with_http_info(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: Group id (required)
        :param file file: Avatar object
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'file', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_update_group_avatar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `group_update_group_avatar`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/group/{groupId}/avatar', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
