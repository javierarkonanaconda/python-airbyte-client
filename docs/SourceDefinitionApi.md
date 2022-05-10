# com.arkondata.airbyte.client.SourceDefinitionApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_source_definition**](SourceDefinitionApi.md#create_custom_source_definition) | **POST** /v1/source_definitions/create_custom | Creates a custom sourceDefinition for the given workspace
[**create_source_definition**](SourceDefinitionApi.md#create_source_definition) | **POST** /v1/source_definitions/create | Creates a sourceDefinition
[**delete_custom_source_definition**](SourceDefinitionApi.md#delete_custom_source_definition) | **POST** /v1/source_definitions/delete_custom | Delete a custom source definition for the given workspace
[**delete_source_definition**](SourceDefinitionApi.md#delete_source_definition) | **POST** /v1/source_definitions/delete | Delete a source definition
[**get_source_definition**](SourceDefinitionApi.md#get_source_definition) | **POST** /v1/source_definitions/get | Get source
[**get_source_definition_for_workspace**](SourceDefinitionApi.md#get_source_definition_for_workspace) | **POST** /v1/source_definitions/get_for_workspace | Get a sourceDefinition that is configured for the given workspace
[**grant_source_definition_to_workspace**](SourceDefinitionApi.md#grant_source_definition_to_workspace) | **POST** /v1/source_definitions/grant_definition | grant a private, non-custom sourceDefinition to a given workspace
[**list_latest_source_definitions**](SourceDefinitionApi.md#list_latest_source_definitions) | **POST** /v1/source_definitions/list_latest | List the latest sourceDefinitions Airbyte supports
[**list_private_source_definitions**](SourceDefinitionApi.md#list_private_source_definitions) | **POST** /v1/source_definitions/list_private | List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.
[**list_source_definitions**](SourceDefinitionApi.md#list_source_definitions) | **POST** /v1/source_definitions/list | List all the sourceDefinitions the current Airbyte deployment is configured to use
[**list_source_definitions_for_workspace**](SourceDefinitionApi.md#list_source_definitions_for_workspace) | **POST** /v1/source_definitions/list_for_workspace | List all the sourceDefinitions the given workspace is configured to use
[**revoke_source_definition_from_workspace**](SourceDefinitionApi.md#revoke_source_definition_from_workspace) | **POST** /v1/source_definitions/revoke_definition | revoke a grant to a private, non-custom sourceDefinition from a given workspace
[**update_custom_source_definition**](SourceDefinitionApi.md#update_custom_source_definition) | **POST** /v1/source_definitions/update_custom | Update a custom sourceDefinition for the given workspace
[**update_source_definition**](SourceDefinitionApi.md#update_source_definition) | **POST** /v1/source_definitions/update | Update a sourceDefinition


# **create_custom_source_definition**
> SourceDefinitionRead create_custom_source_definition()

Creates a custom sourceDefinition for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.custom_source_definition_create import CustomSourceDefinitionCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    custom_source_definition_create = CustomSourceDefinitionCreate(
        workspace_id="workspace_id_example",
        source_definition=SourceDefinitionCreate(
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
    ) # CustomSourceDefinitionCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a custom sourceDefinition for the given workspace
        api_response = api_instance.create_custom_source_definition(custom_source_definition_create=custom_source_definition_create)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->create_custom_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_source_definition_create** | [**CustomSourceDefinitionCreate**](CustomSourceDefinitionCreate.md)|  | [optional]

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

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

# **create_source_definition**
> SourceDefinitionRead create_source_definition()

Creates a sourceDefinition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.source_definition_create import SourceDefinitionCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_create = SourceDefinitionCreate(
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
    ) # SourceDefinitionCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a sourceDefinition
        api_response = api_instance.create_source_definition(source_definition_create=source_definition_create)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->create_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_create** | [**SourceDefinitionCreate**](SourceDefinitionCreate.md)|  | [optional]

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

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

# **delete_custom_source_definition**
> delete_custom_source_definition(source_definition_id_with_workspace_id)

Delete a custom source definition for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_id_with_workspace_id = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    ) # SourceDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom source definition for the given workspace
        api_instance.delete_custom_source_definition(source_definition_id_with_workspace_id)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->delete_custom_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_with_workspace_id** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  |

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

# **delete_source_definition**
> delete_source_definition(source_definition_id_request_body)

Delete a source definition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.source_definition_id_request_body import SourceDefinitionIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_id_request_body = SourceDefinitionIdRequestBody(
        source_definition_id="source_definition_id_example",
    ) # SourceDefinitionIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a source definition
        api_instance.delete_source_definition(source_definition_id_request_body)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->delete_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_request_body** | [**SourceDefinitionIdRequestBody**](SourceDefinitionIdRequestBody.md)|  |

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

# **get_source_definition**
> SourceDefinitionRead get_source_definition(source_definition_id_request_body)

Get source

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.source_definition_id_request_body import SourceDefinitionIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_id_request_body = SourceDefinitionIdRequestBody(
        source_definition_id="source_definition_id_example",
    ) # SourceDefinitionIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Get source
        api_response = api_instance.get_source_definition(source_definition_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->get_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_request_body** | [**SourceDefinitionIdRequestBody**](SourceDefinitionIdRequestBody.md)|  |

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

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

# **get_source_definition_for_workspace**
> SourceDefinitionRead get_source_definition_for_workspace(source_definition_id_with_workspace_id)

Get a sourceDefinition that is configured for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
from com.arkondata.airbyte.client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_id_with_workspace_id = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    ) # SourceDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # Get a sourceDefinition that is configured for the given workspace
        api_response = api_instance.get_source_definition_for_workspace(source_definition_id_with_workspace_id)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->get_source_definition_for_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_with_workspace_id** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  |

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

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

# **grant_source_definition_to_workspace**
> PrivateSourceDefinitionRead grant_source_definition_to_workspace(source_definition_id_with_workspace_id)

grant a private, non-custom sourceDefinition to a given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.private_source_definition_read import PrivateSourceDefinitionRead
from com.arkondata.airbyte.client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_id_with_workspace_id = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    ) # SourceDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # grant a private, non-custom sourceDefinition to a given workspace
        api_response = api_instance.grant_source_definition_to_workspace(source_definition_id_with_workspace_id)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->grant_source_definition_to_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_with_workspace_id** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  |

### Return type

[**PrivateSourceDefinitionRead**](PrivateSourceDefinitionRead.md)

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

# **list_latest_source_definitions**
> SourceDefinitionReadList list_latest_source_definitions()

List the latest sourceDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported sources.

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read_list import SourceDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the latest sourceDefinitions Airbyte supports
        api_response = api_instance.list_latest_source_definitions()
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_latest_source_definitions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

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

# **list_private_source_definitions**
> PrivateSourceDefinitionReadList list_private_source_definitions()

List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody
from com.arkondata.airbyte.client.model.private_source_definition_read_list import PrivateSourceDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    workspace_id_request_body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    ) # WorkspaceIdRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
        api_response = api_instance.list_private_source_definitions(workspace_id_request_body=workspace_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_private_source_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id_request_body** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional]

### Return type

[**PrivateSourceDefinitionReadList**](PrivateSourceDefinitionReadList.md)

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

# **list_source_definitions**
> SourceDefinitionReadList list_source_definitions()

List all the sourceDefinitions the current Airbyte deployment is configured to use

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read_list import SourceDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all the sourceDefinitions the current Airbyte deployment is configured to use
        api_response = api_instance.list_source_definitions()
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_source_definitions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

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

# **list_source_definitions_for_workspace**
> SourceDefinitionReadList list_source_definitions_for_workspace()

List all the sourceDefinitions the given workspace is configured to use

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody
from com.arkondata.airbyte.client.model.source_definition_read_list import SourceDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    workspace_id_request_body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    ) # WorkspaceIdRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all the sourceDefinitions the given workspace is configured to use
        api_response = api_instance.list_source_definitions_for_workspace(workspace_id_request_body=workspace_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_source_definitions_for_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id_request_body** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional]

### Return type

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

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

# **revoke_source_definition_from_workspace**
> revoke_source_definition_from_workspace(source_definition_id_with_workspace_id)

revoke a grant to a private, non-custom sourceDefinition from a given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_id_with_workspace_id = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    ) # SourceDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # revoke a grant to a private, non-custom sourceDefinition from a given workspace
        api_instance.revoke_source_definition_from_workspace(source_definition_id_with_workspace_id)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->revoke_source_definition_from_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_with_workspace_id** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  |

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

# **update_custom_source_definition**
> SourceDefinitionRead update_custom_source_definition()

Update a custom sourceDefinition for the given workspace

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
from com.arkondata.airbyte.client.model.custom_source_definition_update import CustomSourceDefinitionUpdate
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    custom_source_definition_update = CustomSourceDefinitionUpdate(
        workspace_id="workspace_id_example",
        source_definition=SourceDefinitionUpdate(
            source_definition_id="source_definition_id_example",
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
    ) # CustomSourceDefinitionUpdate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a custom sourceDefinition for the given workspace
        api_response = api_instance.update_custom_source_definition(custom_source_definition_update=custom_source_definition_update)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->update_custom_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_source_definition_update** | [**CustomSourceDefinitionUpdate**](CustomSourceDefinitionUpdate.md)|  | [optional]

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

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

# **update_source_definition**
> SourceDefinitionRead update_source_definition()

Update a sourceDefinition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_api
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.source_definition_update import SourceDefinitionUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)
    source_definition_update = SourceDefinitionUpdate(
        source_definition_id="source_definition_id_example",
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
    ) # SourceDefinitionUpdate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a sourceDefinition
        api_response = api_instance.update_source_definition(source_definition_update=source_definition_update)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->update_source_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_update** | [**SourceDefinitionUpdate**](SourceDefinitionUpdate.md)|  | [optional]

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

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

