# com.arkondata.airbyte.client.JobsApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **POST** /v1/jobs/cancel | Cancels a job
[**get_job_debug_info**](JobsApi.md#get_job_debug_info) | **POST** /v1/jobs/get_debug_info | Gets all information needed to debug this job
[**get_job_info**](JobsApi.md#get_job_info) | **POST** /v1/jobs/get | Get information about a job
[**list_jobs_for**](JobsApi.md#list_jobs_for) | **POST** /v1/jobs/list | Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.


# **cancel_job**
> JobInfoRead cancel_job(job_id_request_body)

Cancels a job

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import jobs_api
from com.arkondata.airbyte.client.model.job_info_read import JobInfoRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.job_id_request_body import JobIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id_request_body = JobIdRequestBody(
        id=1,
    ) # JobIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Cancels a job
        api_response = api_instance.cancel_job(job_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id_request_body** | [**JobIdRequestBody**](JobIdRequestBody.md)|  |

### Return type

[**JobInfoRead**](JobInfoRead.md)

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

# **get_job_debug_info**
> JobDebugInfoRead get_job_debug_info(job_id_request_body)

Gets all information needed to debug this job

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import jobs_api
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.job_id_request_body import JobIdRequestBody
from com.arkondata.airbyte.client.model.job_debug_info_read import JobDebugInfoRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id_request_body = JobIdRequestBody(
        id=1,
    ) # JobIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Gets all information needed to debug this job
        api_response = api_instance.get_job_debug_info(job_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling JobsApi->get_job_debug_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id_request_body** | [**JobIdRequestBody**](JobIdRequestBody.md)|  |

### Return type

[**JobDebugInfoRead**](JobDebugInfoRead.md)

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

# **get_job_info**
> JobInfoRead get_job_info(job_id_request_body)

Get information about a job

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import jobs_api
from com.arkondata.airbyte.client.model.job_info_read import JobInfoRead
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.job_id_request_body import JobIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id_request_body = JobIdRequestBody(
        id=1,
    ) # JobIdRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a job
        api_response = api_instance.get_job_info(job_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling JobsApi->get_job_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id_request_body** | [**JobIdRequestBody**](JobIdRequestBody.md)|  |

### Return type

[**JobInfoRead**](JobInfoRead.md)

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

# **list_jobs_for**
> JobReadList list_jobs_for(job_list_request_body)

Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import jobs_api
from com.arkondata.airbyte.client.model.job_list_request_body import JobListRequestBody
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.job_read_list import JobReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_list_request_body = JobListRequestBody(
        config_types=[
            JobConfigType("check_connection_source"),
        ],
        config_id="config_id_example",
        pagination=Pagination(
            page_size=1,
            row_offset=1,
        ),
    ) # JobListRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.
        api_response = api_instance.list_jobs_for(job_list_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling JobsApi->list_jobs_for: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_list_request_body** | [**JobListRequestBody**](JobListRequestBody.md)|  |

### Return type

[**JobReadList**](JobReadList.md)

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

