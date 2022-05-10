# com.arkondata.airbyte.client.DestinationDefinitionSpecificationApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_destination_definition_specification**](DestinationDefinitionSpecificationApi.md#get_destination_definition_specification) | **POST** /v1/destination_definition_specifications/get | Get specification for a destinationDefinition


# **get_destination_definition_specification**
> DestinationDefinitionSpecificationRead get_destination_definition_specification(destination_definition_id_with_workspace_id)

Get specification for a destinationDefinition

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import destination_definition_specification_api
from com.arkondata.airbyte.client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.destination_definition_specification_read import DestinationDefinitionSpecificationRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_specification_api.DestinationDefinitionSpecificationApi(api_client)
    destination_definition_id_with_workspace_id = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    ) # DestinationDefinitionIdWithWorkspaceId | 

    # example passing only required values which don't have defaults set
    try:
        # Get specification for a destinationDefinition
        api_response = api_instance.get_destination_definition_specification(destination_definition_id_with_workspace_id)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationDefinitionSpecificationApi->get_destination_definition_specification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_definition_id_with_workspace_id** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  |

### Return type

[**DestinationDefinitionSpecificationRead**](DestinationDefinitionSpecificationRead.md)

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

