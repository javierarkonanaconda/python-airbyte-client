from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.destination_definition_api import DestinationDefinitionApi


class DestinationDefinition:

    def __init__(self, destination_definition_api: DestinationDefinitionApi):
        if destination_definition_api is not None:
            self.destination_definition_api = destination_definition_api
        else:
            raise Exception("error on destination_definition_api")

    def list_destination_definitions(self):
        try:
            api_response = self.destination_definition_api.list_destination_definitions()
            return api_response
        except ApiException as e:
            print("Exception when calling DestinationDefinitionApi->list_destination_definitions: %s\n" % e)
