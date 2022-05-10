from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.source_definition_specification_api import SourceDefinitionSpecificationApi
from com.arkondata.airbyte.client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId


class SourceDefinitionSpecification:

    def __init__(self, source_definition_specification_api: SourceDefinitionSpecificationApi):
        if source_definition_specification_api is not None:
            self.source_definition_specification_api = source_definition_specification_api
        else:
            raise Exception("error on source_api_instance ")

    def get_source_definition_specification(self, source_definition_id):
        try:
            source_definition_id_with_workspace_id = SourceDefinitionIdWithWorkspaceId(source_definition_id=source_definition_id)
            api_response = self.source_definition_specification_api.get_source_definition_specification(source_definition_id_with_workspace_id)
            return api_response
        except ApiException as e:
            print("Exception when calling SourceDefinitionSpecificationApi->get_source_definition_specification: %s\n" % e)

