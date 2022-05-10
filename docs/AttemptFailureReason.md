# AttemptFailureReason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**failure_origin** | [**AttemptFailureOrigin**](AttemptFailureOrigin.md) |  | [optional] 
**failure_type** | [**AttemptFailureType**](AttemptFailureType.md) |  | [optional] 
**external_message** | **str** |  | [optional] 
**stacktrace** | **str** |  | [optional] 
**retryable** | **bool** | True if it is known that retrying may succeed, e.g. for a transient failure. False if it is known that a retry will not succeed, e.g. for a configuration issue. If not set, retryable status is not well known. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


