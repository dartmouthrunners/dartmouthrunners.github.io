# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ActivitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_activity_by_id(self, id, **kwargs):  # noqa: E501
        """Get Activity  # noqa: E501

        Returns an activity that is owned by the authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_activity_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param bool include_all_efforts: Whether all segments efforts should be included in the response
        :return: DetailedActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_activity_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_activity_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_activity_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Activity  # noqa: E501

        Returns an activity that is owned by the authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_activity_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param bool include_all_efforts: Whether all segments efforts should be included in the response
        :return: DetailedActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include_all_efforts']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activity_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_activity_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'include_all_efforts' in params:
            query_params.append(('include_all_efforts', params['include_all_efforts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedActivity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_comments_by_activity_id(self, id, **kwargs):  # noqa: E501
        """List Activity Comments  # noqa: E501

        Returns the comments of an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_comments_by_activity_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[Comment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_comments_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_comments_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_comments_by_activity_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Activity Comments  # noqa: E501

        Returns the comments of an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_comments_by_activity_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[Comment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_comments_by_activity_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_comments_by_activity_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}/comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Comment]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_kudoers_by_activity_id(self, id, **kwargs):  # noqa: E501
        """List Activity Kudoers  # noqa: E501

        Returns the athletes who kudoed an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_kudoers_by_activity_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryAthlete]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_kudoers_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_kudoers_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_kudoers_by_activity_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Activity Kudoers  # noqa: E501

        Returns the athletes who kudoed an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_kudoers_by_activity_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryAthlete]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_kudoers_by_activity_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_kudoers_by_activity_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}/kudos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummaryAthlete]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_laps_by_activity_id(self, id, **kwargs):  # noqa: E501
        """List Activity Laps  # noqa: E501

        Returns the laps of an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_laps_by_activity_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :return: list[Lap]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_laps_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_laps_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_laps_by_activity_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Activity Laps  # noqa: E501

        Returns the laps of an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_laps_by_activity_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :return: list[Lap]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_laps_by_activity_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_laps_by_activity_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}/laps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Lap]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_logged_in_athlete_activities(self, **kwargs):  # noqa: E501
        """List Athlete Activities  # noqa: E501

        Returns the activities of an athlete for a specific identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_activities(async=True)
        >>> result = thread.get()

        :param async bool
        :param int before: An epoch timestamp to use for filtering activities that have taken place before a certain time
        :param int after: An epoch timestamp to use for filtering activities that have taken place after a certain time
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryActivity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_logged_in_athlete_activities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_logged_in_athlete_activities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_logged_in_athlete_activities_with_http_info(self, **kwargs):  # noqa: E501
        """List Athlete Activities  # noqa: E501

        Returns the activities of an athlete for a specific identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_activities_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int before: An epoch timestamp to use for filtering activities that have taken place before a certain time
        :param int after: An epoch timestamp to use for filtering activities that have taken place after a certain time
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryActivity]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['before', 'after', 'page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_logged_in_athlete_activities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/athlete/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummaryActivity]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zones_by_activity_id(self, id, **kwargs):  # noqa: E501
        """Get Activity Zones  # noqa: E501

        Returns the zones of an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zones_by_activity_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :return: list[ActivityZone]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_zones_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zones_by_activity_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_zones_by_activity_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Activity Zones  # noqa: E501

        Returns the zones of an activity identified by an identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zones_by_activity_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :return: list[ActivityZone]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zones_by_activity_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_zones_by_activity_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}/zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ActivityZone]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_activity_by_id(self, id, **kwargs):  # noqa: E501
        """Update Activity  # noqa: E501

        Updates an activity for a given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_activity_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param UpdatableActivity body:
        :return: DetailedActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_activity_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_activity_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_activity_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Activity  # noqa: E501

        Updates an activity for a given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_activity_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the activity. (required)
        :param UpdatableActivity body:
        :return: DetailedActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_activity_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_activity_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedActivity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
