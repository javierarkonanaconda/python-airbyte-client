from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.destination_definition_specification_api import \
    DestinationDefinitionSpecificationApi
from com.arkondata.airbyte.client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId


class DestinationDefinitionSpecification:

    def __init__(self, destination_definition_specification_api: DestinationDefinitionSpecificationApi):
        if destination_definition_specification_api is not None:
            self.destination_definition_specification_api = destination_definition_specification_api
        else:
            raise Exception("error on destination_definition_api")

    def get_destination_definition_specification(self, destination_definition_id):
        try:
            destination_definition_id_with_workspace_id = DestinationDefinitionIdWithWorkspaceId(
                destination_definition_id=destination_definition_id
            )
            api_response = self.destination_definition_specification_api.get_destination_definition_specification(
                destination_definition_id_with_workspace_id)
            return api_response
        except ApiException as e:
            print("Exception when calling DestinationDefinitionSpecificationApi->get_destination_definition_specification: %s\n" % e)