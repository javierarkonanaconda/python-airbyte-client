from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.destination_api import DestinationApi
from com.arkondata.airbyte.client.model.destination_create import DestinationCreate
from com.arkondata.airbyte.client.model.destination_id_request_body import DestinationIdRequestBody
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody


class Destination:

    def __init__(self, destination_api_instance: DestinationApi):
        if destination_api_instance is not None:
            self.destination_api_instance = destination_api_instance
        else:
            raise Exception("error on destination_api_instance")

    def check_connection_to_destination(self, destination_id):
        try:
            destination_id_request_body = DestinationIdRequestBody(
                destination_id=destination_id,
            )
            api_response = self.destination_api_instance.check_connection_to_destination(destination_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling DestinationApi->check_connection_to_destination: %s\n" % e)

    def create_destination(self, workspace_id, name, destination_definition_id, connection_configuration):
        try:
            destination_create = DestinationCreate(
                workspace_id=workspace_id,
                name=name,
                destination_definition_id=destination_definition_id,
                connection_configuration=connection_configuration,
            )
            api_response = self.destination_api_instance.create_destination(destination_create)
            return api_response
        except ApiException as e:
            print("Exception when calling DestinationApi->create_destination: %s\n" % e)

    def delete_destination(self, destination_id):
        try:
            destination_id_request_body = DestinationIdRequestBody(
                destination_id=destination_id,
            )
            self.destination_api_instance.delete_destination(destination_id_request_body)
        except ApiException as e:
            print("Exception when calling DestinationApi->delete_destination: %s\n" % e)

    def get_destination(self, destination_id):
        try:
            destination_id_request_body = DestinationIdRequestBody(
                destination_id=destination_id,
            )
            api_response = self.destination_api_instance.get_destination(destination_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling DestinationApi->get_destination: %s\n" % e)

    def list_destinations_for_workspace(self, workspace_id):
        try:
            workspace_id_request_body = WorkspaceIdRequestBody(
                workspace_id=workspace_id,
            )
            api_response = self.destination_api_instance.list_destinations_for_workspace(workspace_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling DestinationApi->list_destinations_for_workspace: %s\n" % e)
