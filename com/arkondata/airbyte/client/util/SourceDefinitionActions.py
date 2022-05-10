from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.source_definition_api import SourceDefinitionApi


class SourceDefinition:

    def __init__(self, source_definition_api: SourceDefinitionApi):
        if source_definition_api is not None:
            self.source_definition_api = source_definition_api
        else:
            raise Exception("error on source_definition_api")

    def list_source_definitions(self):
        try:
            api_response = self.source_definition_api.list_source_definitions()
            return api_response
        except ApiException as e:
            print("Exception when calling SourceDefinitionApi->list_source_definitions: %s\n" % e)
