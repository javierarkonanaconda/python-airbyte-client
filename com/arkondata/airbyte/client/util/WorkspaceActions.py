from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.workspace_api import WorkspaceApi
from com.arkondata.airbyte.client.model.workspace_create import WorkspaceCreate
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody


class Workspace:

    def __init__(self, workspace_api_instance: WorkspaceApi):
        if workspace_api_instance is not None:
            self.workspace_api_instance = workspace_api_instance
        else:
            raise Exception("error on source_api_instance ")

    def create_workspace(self, email, name):
        ## notifications agregar ??
        try:
            # Creates a workspace
            workspace_create = WorkspaceCreate(
                email=email,
                anonymous_data_collection=True,
                name=name,
                news=True,
                security_updates=True,
                display_setup_wizard=True,
            )

            api_response = self.workspace_api_instance.create_workspace(workspace_create)
            print(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling WorkspaceApi->create_workspace: %s\n" % e)

    def get_workspace_by_id(self, workspace_id):
        try:
            workspace_id_request_body = WorkspaceIdRequestBody(
                workspace_id=workspace_id,
            )

            api_response = self.workspace_api_instance.get_workspace(workspace_id_request_body)
            print(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling WorkspaceApi->get_workspace: %s\n" % e)

    def delete_workspace(self, workspace_id):
        try:
            workspace_id_request_body = WorkspaceIdRequestBody(
                workspace_id=workspace_id,
            )
            self.workspace_api_instance.delete_workspace(workspace_id_request_body)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)

    def list_workspaces(self):
        try:
            # List all workspaces registered in the current Airbyte deployment
            api_response = self.workspace_api_instance.list_workspaces()
            print(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling WorkspaceApi->list_workspaces: %s\n" % e)
