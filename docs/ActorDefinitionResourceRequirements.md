# ActorDefinitionResourceRequirements

actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**job_specific** | [**[JobTypeResourceLimit]**](JobTypeResourceLimit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


