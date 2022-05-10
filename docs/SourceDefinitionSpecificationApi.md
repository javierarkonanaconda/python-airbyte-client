# com.arkondata.airbyte.client.SourceDefinitionSpecificationApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source_definition_specification**](SourceDefinitionSpecificationApi.md#get_source_definition_specification) | **POST** /v1/source_definition_specifications/get | Get specification for a SourceDefinition.


# **get_source_definition_specification**
> SourceDefinitionSpecificationRead get_source_definition_specification(source_definition_id_with_workspace_id)

Get specification for a SourceDefinition.

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import source_definition_specification_api
from com.arkondata.airbyte.client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.source_definition_specification_read import SourceDefinitionSpecificationRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = source_definition_specification_api.SourceDefinitionSpecificationApi(api_client)
    source_definition_id_with_workspace_id = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    ) # SourceDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # Get specification for a SourceDefinition.
        api_response = api_instance.get_source_definition_specification(source_definition_id_with_workspace_id)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling SourceDefinitionSpecificationApi->get_source_definition_specification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_definition_id_with_workspace_id** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  |

### Return type

[**SourceDefinitionSpecificationRead**](SourceDefinitionSpecificationRead.md)

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

