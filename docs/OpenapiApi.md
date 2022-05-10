# com.arkondata.airbyte.client.OpenapiApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api_spec**](OpenapiApi.md#get_open_api_spec) | **GET** /v1/openapi | Returns the openapi specification


# **get_open_api_spec**
> file_type get_open_api_spec()

Returns the openapi specification

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import openapi_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the openapi specification
        api_response = api_instance.get_open_api_spec()
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling OpenapiApi->get_open_api_spec: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the openapi specification file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

