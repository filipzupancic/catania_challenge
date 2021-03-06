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


class TagApi(object):
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

    def tag_create_tag(self, tag, **kwargs):
        """
        Create new tag
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_create_tag(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Tag tag: Tag object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_create_tag_with_http_info(tag, **kwargs)
        else:
            (data) = self.tag_create_tag_with_http_info(tag, **kwargs)
            return data

    def tag_create_tag_with_http_info(self, tag, **kwargs):
        """
        Create new tag
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_create_tag_with_http_info(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Tag tag: Tag object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_create_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `tag_create_tag`")


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
        if 'tag' in params:
            body_params = params['tag']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/tag', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def tag_delete_tag(self, id, **kwargs):
        """
        Delete tag object
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_delete_tag(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Tag id (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_delete_tag_with_http_info(id, **kwargs)
        else:
            (data) = self.tag_delete_tag_with_http_info(id, **kwargs)
            return data

    def tag_delete_tag_with_http_info(self, id, **kwargs):
        """
        Delete tag object
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_delete_tag_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Tag id (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_delete_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `tag_delete_tag`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/api/v1/tag/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def tag_get(self, id, **kwargs):
        """
        Get tag by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Tag id (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_get_with_http_info(id, **kwargs)
        else:
            (data) = self.tag_get_with_http_info(id, **kwargs)
            return data

    def tag_get_with_http_info(self, id, **kwargs):
        """
        Get tag by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Tag id (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `tag_get`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/api/v1/tag/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def tag_get_list_of_tags(self, offset, size, **kwargs):
        """
        Get list of all existing tags for user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_get_list_of_tags(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Paging offset (required)
        :param int size: Paging size (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: ListOfResourcesOfTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_get_list_of_tags_with_http_info(offset, size, **kwargs)
        else:
            (data) = self.tag_get_list_of_tags_with_http_info(offset, size, **kwargs)
            return data

    def tag_get_list_of_tags_with_http_info(self, offset, size, **kwargs):
        """
        Get list of all existing tags for user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_get_list_of_tags_with_http_info(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Paging offset (required)
        :param int size: Paging size (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: ListOfResourcesOfTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'size', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_get_list_of_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `tag_get_list_of_tags`")
        # verify the required parameter 'size' is set
        if ('size' not in params) or (params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `tag_get_list_of_tags`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'size' in params:
            query_params.append(('size', params['size']))

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

        return self.api_client.call_api('/api/v1/tag/list', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListOfResourcesOfTag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def tag_update_tag(self, id, tag, **kwargs):
        """
        Update existing tag
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_update_tag(id, tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Tag id (required)
        :param Tag tag: Updated tag object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_update_tag_with_http_info(id, tag, **kwargs)
        else:
            (data) = self.tag_update_tag_with_http_info(id, tag, **kwargs)
            return data

    def tag_update_tag_with_http_info(self, id, tag, **kwargs):
        """
        Update existing tag
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_update_tag_with_http_info(id, tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Tag id (required)
        :param Tag tag: Updated tag object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tag', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_update_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `tag_update_tag`")
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `tag_update_tag`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag' in params:
            body_params = params['tag']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/tag/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def tag_update_tags(self, tags, **kwargs):
        """
        Update List of tags on their parent resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_update_tags(tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[ListOfTags] tags: List of resources that need to be modified (required)
        :param bool process_async: If true, backend will process the request asynchrounosly and return HTTP accepted if everything is OK with request
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: list[ListOfTags]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_update_tags_with_http_info(tags, **kwargs)
        else:
            (data) = self.tag_update_tags_with_http_info(tags, **kwargs)
            return data

    def tag_update_tags_with_http_info(self, tags, **kwargs):
        """
        Update List of tags on their parent resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_update_tags_with_http_info(tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[ListOfTags] tags: List of resources that need to be modified (required)
        :param bool process_async: If true, backend will process the request asynchrounosly and return HTTP accepted if everything is OK with request
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: list[ListOfTags]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tags', 'process_async', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_update_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tags' is set
        if ('tags' not in params) or (params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `tag_update_tags`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'process_async' in params:
            query_params.append(('processAsync', params['process_async']))

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_impersonate_user' in params:
            header_params['X-Impersonate-User'] = params['x_impersonate_user']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tags' in params:
            body_params = params['tags']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/tag/list', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ListOfTags]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def tag_update_tags_on_card_comments(self, batch_update, **kwargs):
        """
        Change one tag for another for all comments on card
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_update_tags_on_card_comments(batch_update, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CardCommentsBatchUpdate batch_update: Change object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardCommentsBatchUpdate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_update_tags_on_card_comments_with_http_info(batch_update, **kwargs)
        else:
            (data) = self.tag_update_tags_on_card_comments_with_http_info(batch_update, **kwargs)
            return data

    def tag_update_tags_on_card_comments_with_http_info(self, batch_update, **kwargs):
        """
        Change one tag for another for all comments on card
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_update_tags_on_card_comments_with_http_info(batch_update, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CardCommentsBatchUpdate batch_update: Change object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardCommentsBatchUpdate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_update', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_update_tags_on_card_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_update' is set
        if ('batch_update' not in params) or (params['batch_update'] is None):
            raise ValueError("Missing the required parameter `batch_update` when calling `tag_update_tags_on_card_comments`")


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
        if 'batch_update' in params:
            body_params = params['batch_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/tag/card', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CardCommentsBatchUpdate',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
