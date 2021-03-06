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


class EventApi(object):
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

    def event_get_list(self, offset, size, **kwargs):
        """
        Get event list.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.event_get_list(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset (required)
        :param int size: Requested page size (required)
        :param str since_id: Retturn events with an id greater than (that is, more recent than) the specified id for ascending sort order              or vice versa (events with an id lesser than or older than) for descending sort order.
        :param bool long_polling: Connection should be open until a new event (or max 50 seconds) or return immediately (default is false)
        :param str sort_order: Order of events by created date time (default is ascending)
        :param datetime skip_older_than: Skip all events that were created before given dateTime
        :param list[str] event_type_list: Types of events to return
        :param list[str] skip_event_type_list: Types of events to skip
        :param str html_format: Html format of comment body
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: EventList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.event_get_list_with_http_info(offset, size, **kwargs)
        else:
            (data) = self.event_get_list_with_http_info(offset, size, **kwargs)
            return data

    def event_get_list_with_http_info(self, offset, size, **kwargs):
        """
        Get event list.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.event_get_list_with_http_info(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset (required)
        :param int size: Requested page size (required)
        :param str since_id: Retturn events with an id greater than (that is, more recent than) the specified id for ascending sort order              or vice versa (events with an id lesser than or older than) for descending sort order.
        :param bool long_polling: Connection should be open until a new event (or max 50 seconds) or return immediately (default is false)
        :param str sort_order: Order of events by created date time (default is ascending)
        :param datetime skip_older_than: Skip all events that were created before given dateTime
        :param list[str] event_type_list: Types of events to return
        :param list[str] skip_event_type_list: Types of events to skip
        :param str html_format: Html format of comment body
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: EventList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'size', 'since_id', 'long_polling', 'sort_order', 'skip_older_than', 'event_type_list', 'skip_event_type_list', 'html_format', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method event_get_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `event_get_list`")
        # verify the required parameter 'size' is set
        if ('size' not in params) or (params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `event_get_list`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'since_id' in params:
            query_params.append(('sinceId', params['since_id']))
        if 'long_polling' in params:
            query_params.append(('longPolling', params['long_polling']))
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))
        if 'skip_older_than' in params:
            query_params.append(('skipOlderThan', params['skip_older_than']))
        if 'event_type_list' in params:
            query_params.append(('eventTypeList', params['event_type_list']))
            collection_formats['eventTypeList'] = 'multi'
        if 'skip_event_type_list' in params:
            query_params.append(('skipEventTypeList', params['skip_event_type_list']))
            collection_formats['skipEventTypeList'] = 'multi'
        if 'html_format' in params:
            query_params.append(('htmlFormat', params['html_format']))

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

        return self.api_client.call_api('/api/v1/event/list', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EventList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
