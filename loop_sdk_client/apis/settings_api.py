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


class SettingsApi(object):
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

    def settings_create_exchange_settings(self, settings_exchange, **kwargs):
        """
        Create sync settings for MS Exchange account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_create_exchange_settings(settings_exchange, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsExchange settings_exchange: Exchange sync settings (required)
        :param str authorization: Authorization header
        :return: SyncSettingsExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_create_exchange_settings_with_http_info(settings_exchange, **kwargs)
        else:
            (data) = self.settings_create_exchange_settings_with_http_info(settings_exchange, **kwargs)
            return data

    def settings_create_exchange_settings_with_http_info(self, settings_exchange, **kwargs):
        """
        Create sync settings for MS Exchange account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_create_exchange_settings_with_http_info(settings_exchange, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsExchange settings_exchange: Exchange sync settings (required)
        :param str authorization: Authorization header
        :return: SyncSettingsExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_exchange', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_create_exchange_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_exchange' is set
        if ('settings_exchange' not in params) or (params['settings_exchange'] is None):
            raise ValueError("Missing the required parameter `settings_exchange` when calling `settings_create_exchange_settings`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_exchange' in params:
            body_params = params['settings_exchange']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/settings/exchange', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SyncSettingsExchange',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def settings_create_gmail_settings(self, settings_gmail, **kwargs):
        """
        Create sync settings for Gmail account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_create_gmail_settings(settings_gmail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsGmail settings_gmail: Gmail sync settings (required)
        :param str authorization:
        :return: SyncSettingsGmail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_create_gmail_settings_with_http_info(settings_gmail, **kwargs)
        else:
            (data) = self.settings_create_gmail_settings_with_http_info(settings_gmail, **kwargs)
            return data

    def settings_create_gmail_settings_with_http_info(self, settings_gmail, **kwargs):
        """
        Create sync settings for Gmail account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_create_gmail_settings_with_http_info(settings_gmail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsGmail settings_gmail: Gmail sync settings (required)
        :param str authorization:
        :return: SyncSettingsGmail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_gmail', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_create_gmail_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_gmail' is set
        if ('settings_gmail' not in params) or (params['settings_gmail'] is None):
            raise ValueError("Missing the required parameter `settings_gmail` when calling `settings_create_gmail_settings`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_gmail' in params:
            body_params = params['settings_gmail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/settings/gmail', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SyncSettingsGmail',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def settings_get_sync_settings(self, **kwargs):
        """
        Get sync settings. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_get_sync_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Authorization header
        :return: SyncSettingsBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_get_sync_settings_with_http_info(**kwargs)
        else:
            (data) = self.settings_get_sync_settings_with_http_info(**kwargs)
            return data

    def settings_get_sync_settings_with_http_info(self, **kwargs):
        """
        Get sync settings. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_get_sync_settings_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Authorization header
        :return: SyncSettingsBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_get_sync_settings" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

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

        return self.api_client.call_api('/api/v1/settings/sync', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SyncSettingsBase',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def settings_get_user_settings(self, **kwargs):
        """
        Get user settings. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_get_user_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization:
        :param str x_impersonate_user: Impersonation header
        :return: UserSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_get_user_settings_with_http_info(**kwargs)
        else:
            (data) = self.settings_get_user_settings_with_http_info(**kwargs)
            return data

    def settings_get_user_settings_with_http_info(self, **kwargs):
        """
        Get user settings. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_get_user_settings_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization:
        :param str x_impersonate_user: Impersonation header
        :return: UserSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_impersonate_user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_get_user_settings" % key
                )
            params[key] = val
        del params['kwargs']


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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/settings/user', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserSettings',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def settings_update_exchange_settings(self, settings_exchange, **kwargs):
        """
        Update sync settings for MS Exchange account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_update_exchange_settings(settings_exchange, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsExchange settings_exchange: Exchange sync settings (required)
        :param str authorization: Authorization header
        :return: SyncSettingsExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_update_exchange_settings_with_http_info(settings_exchange, **kwargs)
        else:
            (data) = self.settings_update_exchange_settings_with_http_info(settings_exchange, **kwargs)
            return data

    def settings_update_exchange_settings_with_http_info(self, settings_exchange, **kwargs):
        """
        Update sync settings for MS Exchange account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_update_exchange_settings_with_http_info(settings_exchange, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsExchange settings_exchange: Exchange sync settings (required)
        :param str authorization: Authorization header
        :return: SyncSettingsExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_exchange', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_update_exchange_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_exchange' is set
        if ('settings_exchange' not in params) or (params['settings_exchange'] is None):
            raise ValueError("Missing the required parameter `settings_exchange` when calling `settings_update_exchange_settings`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_exchange' in params:
            body_params = params['settings_exchange']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/settings/exchange', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SyncSettingsExchange',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def settings_update_gmail_settings(self, settings_gmail, **kwargs):
        """
        Update sync settings for Gmail account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_update_gmail_settings(settings_gmail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsGmail settings_gmail: Gmail sync settings (required)
        :param str authorization: Authorization header
        :return: SyncSettingsGmail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_update_gmail_settings_with_http_info(settings_gmail, **kwargs)
        else:
            (data) = self.settings_update_gmail_settings_with_http_info(settings_gmail, **kwargs)
            return data

    def settings_update_gmail_settings_with_http_info(self, settings_gmail, **kwargs):
        """
        Update sync settings for Gmail account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_update_gmail_settings_with_http_info(settings_gmail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SyncSettingsGmail settings_gmail: Gmail sync settings (required)
        :param str authorization: Authorization header
        :return: SyncSettingsGmail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_gmail', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_update_gmail_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_gmail' is set
        if ('settings_gmail' not in params) or (params['settings_gmail'] is None):
            raise ValueError("Missing the required parameter `settings_gmail` when calling `settings_update_gmail_settings`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_gmail' in params:
            body_params = params['settings_gmail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/settings/gmail', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SyncSettingsGmail',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def settings_update_user_settings(self, settings_user, **kwargs):
        """
        Update user settings. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_update_user_settings(settings_user, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserSettings settings_user: User settings (required)
        :param str authorization: Authorization header
        :return: UserSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.settings_update_user_settings_with_http_info(settings_user, **kwargs)
        else:
            (data) = self.settings_update_user_settings_with_http_info(settings_user, **kwargs)
            return data

    def settings_update_user_settings_with_http_info(self, settings_user, **kwargs):
        """
        Update user settings. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.settings_update_user_settings_with_http_info(settings_user, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserSettings settings_user: User settings (required)
        :param str authorization: Authorization header
        :return: UserSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_user', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_update_user_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_user' is set
        if ('settings_user' not in params) or (params['settings_user'] is None):
            raise ValueError("Missing the required parameter `settings_user` when calling `settings_update_user_settings`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_user' in params:
            body_params = params['settings_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/v1/settings/user', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserSettings',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
