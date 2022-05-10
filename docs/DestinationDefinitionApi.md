# com.arkondata.airbyte.client.DestinationDefinitionApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_destination_definition**](DestinationDefinitionApi.md#create_custom_destination_definition) | **POST** /v1/destination_definitions/create_custom | Creates a custom destinationDefinition for the given workspace
[**create_destination_definition**](DestinationDefinitionApi.md#create_destination_definition) | **POST** /v1/destination_definitions/create | Creates a destinationsDefinition
[**delete_custom_destination_definition**](DestinationDefinitionApi.md#delete_custom_destination_definition) | **POST** /v1/destination_definitions/delete_custom | Delete a custom destination definition for the given workspace
[**delete_destination_definition**](DestinationDefinitionApi.md#delete_destination_definition) | **POST** /v1/destination_definitions/delete | Delete a destination definition
[**get_destination_definition**](DestinationDefinitionApi.md#get_destination_definition) | **POST** /v1/destination_definitions/get | Get destinationDefinition
[**get_destination_definition_for_workspace**](DestinationDefinitionApi.md#get_destination_definition_for_workspace) | **POST** /v1/destination_definitions/get_for_workspace | Get a destinationDefinition that is configured for the given workspace
[**grant_destination_definition_to_workspace**](DestinationDefinitionApi.md#grant_destination_definition_to_workspace) | **POST** /v1/destination_definitions/grant_definition | grant a private, non-custom destinationDefinition to a given workspace
[**list_destination_definitions**](DestinationDefinitionApi.md#list_destination_definitions) | **POST** /v1/destination_definitions/list | List all the destinationDefinitions the current Airbyte deployment is configured to use
[**list_destination_definitions_for_workspace**](DestinationDefinitionApi.md#list_destination_definitions_for_workspace) | **POST** /v1/destination_definitions/list_for_workspace | List all the destinationDefinitions the given workspace is configured to use
[**list_latest_destination_definitions**](DestinationDefinitionApi.md#list_latest_destination_definitions) | **POST** /v1/destination_definitions/list_latest | List the latest destinationDefinitions Airbyte supports
[**list_private_destination_definitions**](DestinationDefinitionApi.md#list_private_destination_definitions) | **POST** /v1/destination_definitions/list_private | List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.
[**revoke_destination_definition_from_workspace**](DestinationDefinitionApi.md#revoke_destination_definition_from_workspace) | **POST** /v1/destination_definitions/revoke_definition | revoke a grant to a private, non-custom destinationDefinition from a given workspace
[**update_custom_destination_definition**](DestinationDefinitionApi.md#update_custom_destination_definition) | **POST** /v1/destination_definitions/update_custom | Update a custom destinationDefinition for the given workspace
[**update_destination_definition**](DestinationDefinitionApi.md#update_destination_definition) | **POST** /v1/destination_definitions/update | Update destinationDefinition


# **create_custom_destination_definition**
> DestinationDefinitionRead create_custom_destination_definition()

Creates a custom destinationDefinition for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.custom_destination_definition_create import CustomDestinationDefinitionCreate
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    custom_destination_definition_create = CustomDestinationDefinitionCreate(
        workspace_id="workspace_id_example",
        destination_definition=DestinationDefinitionCreate(
            name="name_example",
            docker_repository="docker_repository_example",
            docker_image_tag="docker_image_tag_example",
            documentation_url="documentation_url_example",
            icon="icon_example",
            resource_requirements=ActorDefinitionResourceRequirements(
                default=ResourceRequirements(
                    cpu_request="cpu_request_example",
                    cpu_limit="cpu_limit_example",
                    memory_request="memory_request_example",
                    memory_limit="memory_limit_example",
                ),
                job_specific=[
                    JobTypeResourceLimit(
                        job_type=JobType("get_spec"),
                        resource_requirements=ResourceRequirements(
                            cpu_request="cpu_request_example",
                            cpu_limit="cpu_limit_example",
                            memory_request="memory_request_example",
                            memory_limit="memory_limit_example",
                        ),
                    ),
                ],
            ),
        ),
    ) # CustomDestinationDefinitionCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a custom destinationDefinition for the given workspace
        api_response = api_instance.create_custom_destination_definition(custom_destination_definition_create=custom_destination_definition_create)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->create_custom_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_destination_definition_create** | [**CustomDestinationDefinitionCreate**](CustomDestinationDefinitionCreate.md)|  | [optional]

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_destination_definition**
> DestinationDefinitionRead create_destination_definition()

Creates a destinationsDefinition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.destination_definition_create import DestinationDefinitionCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_create = DestinationDefinitionCreate(
        name="name_example",
        docker_repository="docker_repository_example",
        docker_image_tag="docker_image_tag_example",
        documentation_url="documentation_url_example",
        icon="icon_example",
        resource_requirements=ActorDefinitionResourceRequirements(
            default=ResourceRequirements(
                cpu_request="cpu_request_example",
                cpu_limit="cpu_limit_example",
                memory_request="memory_request_example",
                memory_limit="memory_limit_example",
            ),
            job_specific=[
                JobTypeResourceLimit(
                    job_type=JobType("get_spec"),
                    resource_requirements=ResourceRequirements(
                        cpu_request="cpu_request_example",
                        cpu_limit="cpu_limit_example",
                        memory_request="memory_request_example",
                        memory_limit="memory_limit_example",
                    ),
                ),
            ],
        ),
    ) # DestinationDefinitionCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a destinationsDefinition
        api_response = api_instance.create_destination_definition(destination_definition_create=destination_definition_create)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->create_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_create** | [**DestinationDefinitionCreate**](DestinationDefinitionCreate.md)|  | [optional]

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_destination_definition**
> delete_custom_destination_definition(destination_definition_id_with_workspace_id)

Delete a custom destination definition for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_id_with_workspace_id = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    ) # DestinationDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom destination definition for the given workspace
        api_instance.delete_custom_destination_definition(destination_definition_id_with_workspace_id)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->delete_custom_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_with_workspace_id** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The destination was deleted successfully. |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination_definition**
> delete_destination_definition(destination_definition_id_request_body)

Delete a destination definition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_id_request_body = DestinationDefinitionIdRequestBody(
        destination_definition_id="destination_definition_id_example",
    ) # DestinationDefinitionIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a destination definition
        api_instance.delete_destination_definition(destination_definition_id_request_body)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->delete_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_request_body** | [**DestinationDefinitionIdRequestBody**](DestinationDefinitionIdRequestBody.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_definition**
> DestinationDefinitionRead get_destination_definition(destination_definition_id_request_body)

Get destinationDefinition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_id_request_body = DestinationDefinitionIdRequestBody(
        destination_definition_id="destination_definition_id_example",
    ) # DestinationDefinitionIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Get destinationDefinition
        api_response = api_instance.get_destination_definition(destination_definition_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->get_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_request_body** | [**DestinationDefinitionIdRequestBody**](DestinationDefinitionIdRequestBody.md)|  |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_definition_for_workspace**
> DestinationDefinitionRead get_destination_definition_for_workspace(destination_definition_id_with_workspace_id)

Get a destinationDefinition that is configured for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_id_with_workspace_id = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    ) # DestinationDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # Get a destinationDefinition that is configured for the given workspace
        api_response = api_instance.get_destination_definition_for_workspace(destination_definition_id_with_workspace_id)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->get_destination_definition_for_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_with_workspace_id** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_destination_definition_to_workspace**
> PrivateDestinationDefinitionRead grant_destination_definition_to_workspace(destination_definition_id_with_workspace_id)

grant a private, non-custom destinationDefinition to a given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from com.arkondata.airbyte.client.model.private_destination_definition_read import PrivateDestinationDefinitionRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_id_with_workspace_id = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    ) # DestinationDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # grant a private, non-custom destinationDefinition to a given workspace
        api_response = api_instance.grant_destination_definition_to_workspace(destination_definition_id_with_workspace_id)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->grant_destination_definition_to_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_with_workspace_id** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  |

### Return type

[**PrivateDestinationDefinitionRead**](PrivateDestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_destination_definitions**
> DestinationDefinitionReadList list_destination_definitions()

List all the destinationDefinitions the current Airbyte deployment is configured to use

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read_list import DestinationDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all the destinationDefinitions the current Airbyte deployment is configured to use
        api_response = api_instance.list_destination_definitions()
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_destination_definitions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_destination_definitions_for_workspace**
> DestinationDefinitionReadList list_destination_definitions_for_workspace()

List all the destinationDefinitions the given workspace is configured to use

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read_list import DestinationDefinitionReadList
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    workspace_id_request_body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    ) # WorkspaceIdRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all the destinationDefinitions the given workspace is configured to use
        api_response = api_instance.list_destination_definitions_for_workspace(workspace_id_request_body=workspace_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_destination_definitions_for_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id_request_body** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional]

### Return type

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_latest_destination_definitions**
> DestinationDefinitionReadList list_latest_destination_definitions()

List the latest destinationDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported destinations.

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read_list import DestinationDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the latest destinationDefinitions Airbyte supports
        api_response = api_instance.list_latest_destination_definitions()
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_latest_destination_definitions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_private_destination_definitions**
> PrivateDestinationDefinitionReadList list_private_destination_definitions()

List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.private_destination_definition_read_list import PrivateDestinationDefinitionReadList
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    workspace_id_request_body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    ) # WorkspaceIdRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
        api_response = api_instance.list_private_destination_definitions(workspace_id_request_body=workspace_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_private_destination_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id_request_body** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional]

### Return type

[**PrivateDestinationDefinitionReadList**](PrivateDestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_destination_definition_from_workspace**
> revoke_destination_definition_from_workspace(destination_definition_id_with_workspace_id)

revoke a grant to a private, non-custom destinationDefinition from a given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_id_with_workspace_id = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    ) # DestinationDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # revoke a grant to a private, non-custom destinationDefinition from a given workspace
        api_instance.revoke_destination_definition_from_workspace(destination_definition_id_with_workspace_id)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->revoke_destination_definition_from_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_with_workspace_id** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_destination_definition**
> DestinationDefinitionRead update_custom_destination_definition()

Update a custom destinationDefinition for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.custom_destination_definition_update import CustomDestinationDefinitionUpdate
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    custom_destination_definition_update = CustomDestinationDefinitionUpdate(
        workspace_id="workspace_id_example",
        destination_definition=DestinationDefinitionUpdate(
            destination_definition_id="destination_definition_id_example",
            docker_image_tag="docker_image_tag_example",
            resource_requirements=ActorDefinitionResourceRequirements(
                default=ResourceRequirements(
                    cpu_request="cpu_request_example",
                    cpu_limit="cpu_limit_example",
                    memory_request="memory_request_example",
                    memory_limit="memory_limit_example",
                ),
                job_specific=[
                    JobTypeResourceLimit(
                        job_type=JobType("get_spec"),
                        resource_requirements=ResourceRequirements(
                            cpu_request="cpu_request_example",
                            cpu_limit="cpu_limit_example",
                            memory_request="memory_request_example",
                            memory_limit="memory_limit_example",
                        ),
                    ),
                ],
            ),
        ),
    ) # CustomDestinationDefinitionUpdate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a custom destinationDefinition for the given workspace
        api_response = api_instance.update_custom_destination_definition(custom_destination_definition_update=custom_destination_definition_update)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->update_custom_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_destination_definition_update** | [**CustomDestinationDefinitionUpdate**](CustomDestinationDefinitionUpdate.md)|  | [optional]

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_destination_definition**
> DestinationDefinitionRead update_destination_definition(destination_definition_update)

Update destinationDefinition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_api
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.destination_definition_update import DestinationDefinitionUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
    destination_definition_update = DestinationDefinitionUpdate(
        destination_definition_id="destination_definition_id_example",
        docker_image_tag="docker_image_tag_example",
        resource_requirements=ActorDefinitionResourceRequirements(
            default=ResourceRequirements(
                cpu_request="cpu_request_example",
                cpu_limit="cpu_limit_example",
                memory_request="memory_request_example",
                memory_limit="memory_limit_example",
            ),
            job_specific=[
                JobTypeResourceLimit(
                    job_type=JobType("get_spec"),
                    resource_requirements=ResourceRequirements(
                        cpu_request="cpu_request_example",
                        cpu_limit="cpu_limit_example",
                        memory_request="memory_request_example",
                        memory_limit="memory_limit_example",
                    ),
                ),
            ],
        ),
    ) # DestinationDefinitionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update destinationDefinition
        api_response = api_instance.update_destination_definition(destination_definition_update)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->update_destination_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_update** | [**DestinationDefinitionUpdate**](DestinationDefinitionUpdate.md)|  |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Object with given id was not found. |  -  |
**422** | Input failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

