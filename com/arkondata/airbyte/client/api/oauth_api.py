"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints. * All `web_backend` APIs are not considered public APIs and are not guaranteeing backwards compatibility.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from com.arkondata.airbyte.client.api_client import ApiClient, Endpoint as _Endpoint
from com.arkondata.airbyte.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from com.arkondata.airbyte.client.model.complete_destination_o_auth_request import CompleteDestinationOAuthRequest
from com.arkondata.airbyte.client.model.complete_o_auth_response import CompleteOAuthResponse
from com.arkondata.airbyte.client.model.complete_source_oauth_request import CompleteSourceOauthRequest
from com.arkondata.airbyte.client.model.destination_oauth_consent_request import DestinationOauthConsentRequest
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.known_exception_info import KnownExceptionInfo
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.o_auth_consent_read import OAuthConsentRead
from com.arkondata.airbyte.client.model.set_instancewide_destination_oauth_params_request_body import SetInstancewideDestinationOauthParamsRequestBody
from com.arkondata.airbyte.client.model.set_instancewide_source_oauth_params_request_body import SetInstancewideSourceOauthParamsRequestBody
from com.arkondata.airbyte.client.model.source_oauth_consent_request import SourceOauthConsentRequest


class OauthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.complete_destination_o_auth_endpoint = _Endpoint(
            settings={
                'response_type': (CompleteOAuthResponse,),
                'auth': [],
                'endpoint_path': '/v1/destination_oauths/complete_oauth',
                'operation_id': 'complete_destination_o_auth',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'complete_destination_o_auth_request',
                ],
                'required': [
                    'complete_destination_o_auth_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'complete_destination_o_auth_request':
                        (CompleteDestinationOAuthRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'complete_destination_o_auth_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.complete_source_o_auth_endpoint = _Endpoint(
            settings={
                'response_type': (CompleteOAuthResponse,),
                'auth': [],
                'endpoint_path': '/v1/source_oauths/complete_oauth',
                'operation_id': 'complete_source_o_auth',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'complete_source_oauth_request',
                ],
                'required': [
                    'complete_source_oauth_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'complete_source_oauth_request':
                        (CompleteSourceOauthRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'complete_source_oauth_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_destination_o_auth_consent_endpoint = _Endpoint(
            settings={
                'response_type': (OAuthConsentRead,),
                'auth': [],
                'endpoint_path': '/v1/destination_oauths/get_consent_url',
                'operation_id': 'get_destination_o_auth_consent',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'destination_oauth_consent_request',
                ],
                'required': [
                    'destination_oauth_consent_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'destination_oauth_consent_request':
                        (DestinationOauthConsentRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'destination_oauth_consent_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_source_o_auth_consent_endpoint = _Endpoint(
            settings={
                'response_type': (OAuthConsentRead,),
                'auth': [],
                'endpoint_path': '/v1/source_oauths/get_consent_url',
                'operation_id': 'get_source_o_auth_consent',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'source_oauth_consent_request',
                ],
                'required': [
                    'source_oauth_consent_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'source_oauth_consent_request':
                        (SourceOauthConsentRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'source_oauth_consent_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.set_instancewide_destination_oauth_params_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/destination_oauths/oauth_params/create',
                'operation_id': 'set_instancewide_destination_oauth_params',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'set_instancewide_destination_oauth_params_request_body',
                ],
                'required': [
                    'set_instancewide_destination_oauth_params_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'set_instancewide_destination_oauth_params_request_body':
                        (SetInstancewideDestinationOauthParamsRequestBody,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'set_instancewide_destination_oauth_params_request_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.set_instancewide_source_oauth_params_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/source_oauths/oauth_params/create',
                'operation_id': 'set_instancewide_source_oauth_params',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'set_instancewide_source_oauth_params_request_body',
                ],
                'required': [
                    'set_instancewide_source_oauth_params_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'set_instancewide_source_oauth_params_request_body':
                        (SetInstancewideSourceOauthParamsRequestBody,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'set_instancewide_source_oauth_params_request_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def complete_destination_o_auth(
        self,
        complete_destination_o_auth_request,
        **kwargs
    ):
        """Given a destination def ID generate an access/refresh token etc.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.complete_destination_o_auth(complete_destination_o_auth_request, async_req=True)
        >>> result = thread.get()

        Args:
            complete_destination_o_auth_request (CompleteDestinationOAuthRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CompleteOAuthResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['complete_destination_o_auth_request'] = \
            complete_destination_o_auth_request
        return self.complete_destination_o_auth_endpoint.call_with_http_info(**kwargs)

    def complete_source_o_auth(
        self,
        complete_source_oauth_request,
        **kwargs
    ):
        """Given a source def ID generate an access/refresh token etc.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.complete_source_o_auth(complete_source_oauth_request, async_req=True)
        >>> result = thread.get()

        Args:
            complete_source_oauth_request (CompleteSourceOauthRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CompleteOAuthResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['complete_source_oauth_request'] = \
            complete_source_oauth_request
        return self.complete_source_o_auth_endpoint.call_with_http_info(**kwargs)

    def get_destination_o_auth_consent(
        self,
        destination_oauth_consent_request,
        **kwargs
    ):
        """Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_destination_o_auth_consent(destination_oauth_consent_request, async_req=True)
        >>> result = thread.get()

        Args:
            destination_oauth_consent_request (DestinationOauthConsentRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OAuthConsentRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['destination_oauth_consent_request'] = \
            destination_oauth_consent_request
        return self.get_destination_o_auth_consent_endpoint.call_with_http_info(**kwargs)

    def get_source_o_auth_consent(
        self,
        source_oauth_consent_request,
        **kwargs
    ):
        """Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_source_o_auth_consent(source_oauth_consent_request, async_req=True)
        >>> result = thread.get()

        Args:
            source_oauth_consent_request (SourceOauthConsentRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OAuthConsentRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['source_oauth_consent_request'] = \
            source_oauth_consent_request
        return self.get_source_o_auth_consent_endpoint.call_with_http_info(**kwargs)

    def set_instancewide_destination_oauth_params(
        self,
        set_instancewide_destination_oauth_params_request_body,
        **kwargs
    ):
        """Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_instancewide_destination_oauth_params(set_instancewide_destination_oauth_params_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            set_instancewide_destination_oauth_params_request_body (SetInstancewideDestinationOauthParamsRequestBody):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['set_instancewide_destination_oauth_params_request_body'] = \
            set_instancewide_destination_oauth_params_request_body
        return self.set_instancewide_destination_oauth_params_endpoint.call_with_http_info(**kwargs)

    def set_instancewide_source_oauth_params(
        self,
        set_instancewide_source_oauth_params_request_body,
        **kwargs
    ):
        """Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_instancewide_source_oauth_params(set_instancewide_source_oauth_params_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            set_instancewide_source_oauth_params_request_body (SetInstancewideSourceOauthParamsRequestBody):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['set_instancewide_source_oauth_params_request_body'] = \
            set_instancewide_source_oauth_params_request_body
        return self.set_instancewide_source_oauth_params_endpoint.call_with_http_info(**kwargs)

