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


class CardApi(object):
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

    def card_create_card(self, card_chat, **kwargs):
        """
        Create chat card
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_create_card(card_chat, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CardChat card_chat: Card chat object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardChat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.card_create_card_with_http_info(card_chat, **kwargs)
        else:
            (data) = self.card_create_card_with_http_info(card_chat, **kwargs)
            return data

    def card_create_card_with_http_info(self, card_chat, **kwargs):
        """
        Create chat card
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_create_card_with_http_info(card_chat, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CardChat card_chat: Card chat object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardChat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['card_chat', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method card_create_card" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'card_chat' is set
        if ('card_chat' not in params) or (params['card_chat'] is None):
            raise ValueError("Missing the required parameter `card_chat` when calling `card_create_card`")


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
        if 'card_chat' in params:
            body_params = params['card_chat']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/card/chat', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CardChat',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def card_create_card2(self, card_appointment, **kwargs):
        """
        Create chat appointment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_create_card2(card_appointment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CardAppointment card_appointment: Card appointment object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardChat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.card_create_card2_with_http_info(card_appointment, **kwargs)
        else:
            (data) = self.card_create_card2_with_http_info(card_appointment, **kwargs)
            return data

    def card_create_card2_with_http_info(self, card_appointment, **kwargs):
        """
        Create chat appointment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_create_card2_with_http_info(card_appointment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CardAppointment card_appointment: Card appointment object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardChat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['card_appointment', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method card_create_card2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'card_appointment' is set
        if ('card_appointment' not in params) or (params['card_appointment'] is None):
            raise ValueError("Missing the required parameter `card_appointment` when calling `card_create_card2`")


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
        if 'card_appointment' in params:
            body_params = params['card_appointment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/card/appointment', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CardChat',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def card_get(self, id, **kwargs):
        """
        Get card by id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Card id (required)
        :param int offset_comments: Requested page offset on Comments resource
        :param int size_comments: Requested page size of Comments resource
        :param str order_comments: Order of comments by created date time (default is ascending).
        :param int offset_copied_comments: Requested page offset on CopiedComments resource
        :param int size_copied_comments: Requested page size of CopiedComments resource
        :param str order_copied_comments: Order of copied comments by created date time (default is ascending).
        :param str html_format: HTML format of comment body
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.card_get_with_http_info(id, **kwargs)
        else:
            (data) = self.card_get_with_http_info(id, **kwargs)
            return data

    def card_get_with_http_info(self, id, **kwargs):
        """
        Get card by id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Card id (required)
        :param int offset_comments: Requested page offset on Comments resource
        :param int size_comments: Requested page size of Comments resource
        :param str order_comments: Order of comments by created date time (default is ascending).
        :param int offset_copied_comments: Requested page offset on CopiedComments resource
        :param int size_copied_comments: Requested page size of CopiedComments resource
        :param str order_copied_comments: Order of copied comments by created date time (default is ascending).
        :param str html_format: HTML format of comment body
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: CardBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'offset_comments', 'size_comments', 'order_comments', 'offset_copied_comments', 'size_copied_comments', 'order_copied_comments', 'html_format', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method card_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `card_get`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'offset_comments' in params:
            query_params.append(('offsetComments', params['offset_comments']))
        if 'size_comments' in params:
            query_params.append(('sizeComments', params['size_comments']))
        if 'order_comments' in params:
            query_params.append(('orderComments', params['order_comments']))
        if 'offset_copied_comments' in params:
            query_params.append(('offsetCopiedComments', params['offset_copied_comments']))
        if 'size_copied_comments' in params:
            query_params.append(('sizeCopiedComments', params['size_copied_comments']))
        if 'order_copied_comments' in params:
            query_params.append(('orderCopiedComments', params['order_copied_comments']))
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

        return self.api_client.call_api('/api/v1/card/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CardBase',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def card_get_agenda_list(self, offset, size, date_time_start, **kwargs):
        """
        Get appointment cards sorted by date time (agenda view).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_get_agenda_list(offset, size, date_time_start, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset. (required)
        :param int size: Requested page size. (required)
        :param datetime date_time_start: Minimum start date time of appointment (required)
        :param datetime date_time_end: Maximum end time of appointment (if not defined you get all appointments from dateTimeStart onwards)
        :param str authorization: Authorization header.
        :param str x_impersonate_user: Impersonation header.
        :return: ListOfResourcesOfCardAppointment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.card_get_agenda_list_with_http_info(offset, size, date_time_start, **kwargs)
        else:
            (data) = self.card_get_agenda_list_with_http_info(offset, size, date_time_start, **kwargs)
            return data

    def card_get_agenda_list_with_http_info(self, offset, size, date_time_start, **kwargs):
        """
        Get appointment cards sorted by date time (agenda view).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_get_agenda_list_with_http_info(offset, size, date_time_start, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset. (required)
        :param int size: Requested page size. (required)
        :param datetime date_time_start: Minimum start date time of appointment (required)
        :param datetime date_time_end: Maximum end time of appointment (if not defined you get all appointments from dateTimeStart onwards)
        :param str authorization: Authorization header.
        :param str x_impersonate_user: Impersonation header.
        :return: ListOfResourcesOfCardAppointment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'size', 'date_time_start', 'date_time_end', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method card_get_agenda_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `card_get_agenda_list`")
        # verify the required parameter 'size' is set
        if ('size' not in params) or (params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `card_get_agenda_list`")
        # verify the required parameter 'date_time_start' is set
        if ('date_time_start' not in params) or (params['date_time_start'] is None):
            raise ValueError("Missing the required parameter `date_time_start` when calling `card_get_agenda_list`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'date_time_start' in params:
            query_params.append(('dateTimeStart', params['date_time_start']))
        if 'date_time_end' in params:
            query_params.append(('dateTimeEnd', params['date_time_end']))

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

        return self.api_client.call_api('/api/v1/card/appointment/list', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListOfResourcesOfCardAppointment',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def card_get_list(self, offset, size, **kwargs):
        """
        Get card list.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_get_list(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset. (required)
        :param int size: Requested page size. (required)
        :param str search_query: Plain text search query to filter comment list by cards title.
        :param list[str] card_ids: List of card ids to filter card list by.
        :param list[str] recipient_ids: List of recipient ids (either a user or a group) to filter comment list by.
        :param list[str] tags: List of tags to filter card list by.
        :param list[CardType] card_types: List of card types to filter card list by.
        :param str html_format: HTML format of comment body.
        :param str authorization: Authorization header.
        :param str x_impersonate_user: Impersonation header.
        :return: ListOfResourcesOfCardBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.card_get_list_with_http_info(offset, size, **kwargs)
        else:
            (data) = self.card_get_list_with_http_info(offset, size, **kwargs)
            return data

    def card_get_list_with_http_info(self, offset, size, **kwargs):
        """
        Get card list.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_get_list_with_http_info(offset, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Requested page offset. (required)
        :param int size: Requested page size. (required)
        :param str search_query: Plain text search query to filter comment list by cards title.
        :param list[str] card_ids: List of card ids to filter card list by.
        :param list[str] recipient_ids: List of recipient ids (either a user or a group) to filter comment list by.
        :param list[str] tags: List of tags to filter card list by.
        :param list[CardType] card_types: List of card types to filter card list by.
        :param str html_format: HTML format of comment body.
        :param str authorization: Authorization header.
        :param str x_impersonate_user: Impersonation header.
        :return: ListOfResourcesOfCardBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'size', 'search_query', 'card_ids', 'recipient_ids', 'tags', 'card_types', 'html_format', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method card_get_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `card_get_list`")
        # verify the required parameter 'size' is set
        if ('size' not in params) or (params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `card_get_list`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'search_query' in params:
            query_params.append(('searchQuery', params['search_query']))
        if 'card_ids' in params:
            query_params.append(('cardIds', params['card_ids']))
            collection_formats['cardIds'] = 'multi'
        if 'recipient_ids' in params:
            query_params.append(('recipientIds', params['recipient_ids']))
            collection_formats['recipientIds'] = 'multi'
        if 'tags' in params:
            query_params.append(('tags', params['tags']))
            collection_formats['tags'] = 'multi'
        if 'card_types' in params:
            query_params.append(('cardTypes', params['card_types']))
            collection_formats['cardTypes'] = 'multi'
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

        return self.api_client.call_api('/api/v1/card/list', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListOfResourcesOfCardBase',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def card_update_appointment_response(self, id, appointment_response, **kwargs):
        """
        Update appointment response for appointment card
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_update_appointment_response(id, appointment_response, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Card id (required)
        :param AppointmentResponse appointment_response: Appointment response object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: AppointmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.card_update_appointment_response_with_http_info(id, appointment_response, **kwargs)
        else:
            (data) = self.card_update_appointment_response_with_http_info(id, appointment_response, **kwargs)
            return data

    def card_update_appointment_response_with_http_info(self, id, appointment_response, **kwargs):
        """
        Update appointment response for appointment card
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.card_update_appointment_response_with_http_info(id, appointment_response, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Card id (required)
        :param AppointmentResponse appointment_response: Appointment response object (required)
        :param str authorization: Authorization header
        :param str x_impersonate_user: Impersonation header
        :return: AppointmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'appointment_response', 'authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method card_update_appointment_response" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `card_update_appointment_response`")
        # verify the required parameter 'appointment_response' is set
        if ('appointment_response' not in params) or (params['appointment_response'] is None):
            raise ValueError("Missing the required parameter `appointment_response` when calling `card_update_appointment_response`")


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
        if 'appointment_response' in params:
            body_params = params['appointment_response']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/card/appointment/{id}/response', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AppointmentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
