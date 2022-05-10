# com.arkondata.airbyte.client.NotificationsApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**try_notification_config**](NotificationsApi.md#try_notification_config) | **POST** /v1/notifications/try | Try sending a notifications


# **try_notification_config**
> NotificationRead try_notification_config(notification)

Try sending a notifications

### Example


```python
import time
import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import notifications_api
from com.arkondata.airbyte.client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from com.arkondata.airbyte.client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from com.arkondata.airbyte.client.model.notification_read import NotificationRead
from com.arkondata.airbyte.client.model.notification import Notification
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host = "http://localhost:8000/api"
)


# Enter a context with an instance of the API client
with com.arkondata.airbyte.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = notifications_api.NotificationsApi(api_client)
    notification = Notification(
        notification_type=NotificationType("slack"),
        send_on_success=False,
        send_on_failure=True,
        slack_configuration=SlackNotificationConfiguration(
            webhook="webhook_example",
        ),
        customerio_configuration={},
    ) # Notification | 

    # example passing only required values which don't have defaults set
    try:
        # Try sending a notifications
        api_response = api_instance.try_notification_config(notification)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling NotificationsApi->try_notification_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**Notification**](Notification.md)|  |

### Return type

[**NotificationRead**](NotificationRead.md)

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

