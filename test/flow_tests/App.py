import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import workspace_api, destination_api
from com.arkondata.airbyte.client.api.destination_api import DestinationApi
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody
from com.arkondata.airbyte.client.model.workspace_read_list import WorkspaceReadList
from pprint import pprint

### inputs params
workspace_name = "javstest"


# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host="",
    username="",
    password=""
)


def get_workspaces(workspace_api_instance):
    try:
        api_response = workspace_api_instance.list_workspaces()
        return api_response
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling WorkspaceApi->list_workspaces: %s\n" % e)


def list_destinations_by_workspaces(destination_api_instance:DestinationApi, workspace_id_request_body):
    try:
        api_response = destination_api_instance.list_destinations_for_workspace(workspace_id_request_body)
        pprint(api_response)
    except com.arkondata.airbyte.client.ApiException as e:
        print("Exception when calling DestinationApi->list_destinations_for_workspace: %s\n" % e)


with com.arkondata.airbyte.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    workspace_api_instance = workspace_api.WorkspaceApi(api_client)
    workspaces = get_workspaces(workspace_api_instance)
    print("workspaces")
    print(workspaces)
    id = workspaces["workspaces"][0]["workspace_id"]
    print(id)

    print("---------------------------------------------------------------------------------------------")
    destination_api_instance = destination_api.DestinationApi(api_client)
    workspace_id_request_body = WorkspaceIdRequestBody(
        workspace_id=id,
    )

    list_destinations_by_workspaces(destination_api_instance, workspace_id_request_body)

    # example, this endpoint has no required or optional parameters

