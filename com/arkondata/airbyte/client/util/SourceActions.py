from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.source_api import SourceApi
from com.arkondata.airbyte.client.model.source_create import SourceCreate
from com.arkondata.airbyte.client.model.source_id_request_body import SourceIdRequestBody
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody


class Source:

    def __init__(self, source_api_instance: SourceApi):
        if source_api_instance is not None:
            self.source_api_instance = source_api_instance
        else:
            raise Exception("error on source_api_instance ")

    def check_connection_to_source(self, source_id):
        try:
            source_id_request_body = SourceIdRequestBody(
                source_id=source_id,
            )
            api_response = self.source_api_instance.check_connection_to_source(source_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling SourceApi->check_connection_to_source: %s\n" % e)

    def create_source(self, source_definition_id, workspace_id, name, connection_configuration):
        try:
            source_create = SourceCreate(
                source_definition_id=source_definition_id,
                connection_configuration=connection_configuration,
                workspace_id=workspace_id,
                name=name,
            )
            api_response = self.source_api_instance.create_source(source_create)
            return api_response
        except ApiException as e:
            print("Exception when calling SourceApi->create_source: %s\n" % e)

    def delete_source(self, source_id):
        try:
            source_id_request_body = SourceIdRequestBody(
                source_id=source_id,
            )
            self.source_api_instance.delete_source(source_id_request_body)
        except ApiException as e:
            print("Exception when calling SourceApi->delete_source: %s\n" % e)

    def get_source(self, source_id):
        try:
            source_id_request_body = SourceIdRequestBody(
                source_id=source_id,
            )
            api_response = self.source_api_instance.get_source(source_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling SourceApi->get_source: %s\n" % e)

    def list_sources_for_workspace(self, workspace_id):
        try:
            workspace_id_request_body = WorkspaceIdRequestBody(
                workspace_id=workspace_id,
            )
            api_response = self.source_api_instance.list_sources_for_workspace(workspace_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling SourceApi->list_sources_for_workspace: %s\n" % e)
