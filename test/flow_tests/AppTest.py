import json
import time

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import workspace_api, destination_api, source_definition_api, \
    source_definition_specification_api, source_api, destination_definition_specification_api, \
    destination_definition_api, connection_api, jobs_api
from com.arkondata.airbyte.client.api.destination_api import DestinationApi
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody
from com.arkondata.airbyte.client.model.workspace_read_list import WorkspaceReadList
from pprint import pprint

### inputs params
from com.arkondata.airbyte.client.util.ConnectionActions import Connection
from com.arkondata.airbyte.client.util.DestinationActions import Destination
from com.arkondata.airbyte.client.util.DestinationDefinitionActions import DestinationDefinition
from com.arkondata.airbyte.client.util.DestinationDefinitionSpecificationActions import \
    DestinationDefinitionSpecification
from com.arkondata.airbyte.client.util.JobActions import Job
from com.arkondata.airbyte.client.util.SourceActions import Source
from com.arkondata.airbyte.client.util.SourceDefinitionActions import SourceDefinition
from com.arkondata.airbyte.client.util.SourceDefinitionSpecificationActions import SourceDefinitionSpecification
from com.arkondata.airbyte.client.util.WorkspaceActions import Workspace

workspace_name = '02bde510-f5b1-4aeb-b390-086b8d764e1d'  ###"javstest"
source_ds = "postgres"
destination_ds = "postgres"

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = com.arkondata.airbyte.client.Configuration(
    host="",
    username="",
    password=""
)


def clean_json(obj):
    json_obj = obj.__dict__["_data_store"]
    del json_obj["icon"]
    return json_obj


with com.arkondata.airbyte.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    print("workspace")
    workspace_api_instance = workspace_api.WorkspaceApi(api_client)
    workspaces = Workspace(workspace_api_instance).list_workspaces()
    get_workspaces = list(map(lambda x: x.__dict__.get('_data_store', {}), workspaces["workspaces"]))

    get_workspace = list(filter(lambda x: x["name"] == workspace_name, get_workspaces))
    if len(get_workspace) > 0:
        print("existe")
        workspace_id = get_workspace[0].get("workspace_id", "")
        print(workspace_id)
    else:
        print("no existe")
        ### add create workspace

    ### source vevents
    print("source def events--------------------------------------------------------------------------")
    source_definition_api_instance = source_definition_api.SourceDefinitionApi(api_client)
    sources_def = SourceDefinition(source_definition_api_instance).list_source_definitions()
    source_definitions_lst = sources_def.__dict__.get("_data_store").get("source_definitions")
    sources_json_lst = list(map(lambda x: clean_json(x), source_definitions_lst))

    ## get source id
    find_source = list(filter(lambda x: str(x.get("name", "")).lower() == source_ds, sources_json_lst))
    print(find_source)

    if find_source != []:
        source_def_id = find_source[0]["source_definition_id"]
        print(source_def_id)

        source_definition_specification_api_instance = source_definition_specification_api.SourceDefinitionSpecificationApi(api_client)
        source_def_spec = SourceDefinitionSpecification(source_definition_specification_api_instance).get_source_definition_specification(source_def_id)
        print("source_def_spec")

        print(source_def_spec)
        ###### create source
        print("create_source_res>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        source_api_instance = source_api.SourceApi(api_client)
        connection_configuration ={
            "database":"postgres",
            "host":"35.196.111.83",
            "username":"postgres",
            "password":"bm9tZXZlYXM=",
            "port":5432,
            "schemas":["public"]
        }

        source_inst = Source(source_api_instance)
        create_source_res = Source(source_api_instance).create_source(source_definition_id=source_def_id,workspace_id=workspace_id, name="testconn",connection_configuration=connection_configuration)
        print(create_source_res)
        time.sleep(10)


        ########## check source connection
        g_source_id = 'd0134a9c-d895-43e9-bc61-cc1f2ac05289'
        print("check source connection")
        check_source = source_inst.check_connection_to_source(g_source_id)
        connection_status = check_source.__dict__["_data_store"].get("status", None)
        print(connection_status)


        ################### destino
        time.sleep(10)
        destination_definition_api_instance = destination_definition_api.DestinationDefinitionApi(api_client)
        destination_definition_res = DestinationDefinition(destination_definition_api_instance).list_destination_definitions()
        print("destination_definition_res >>>>>><<>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        des_def_dict_res = destination_definition_res.__dict__["_data_store"]
        des = des_def_dict_res["destination_definitions"]
        des2 = list(map(lambda x: clean_json(x), des))
        find_destination = list(filter(lambda x: str(x.get("name", "")).lower() == destination_ds.lower(), des2))
        if len(find_destination) > 0:
            destination_definition_id = find_destination[0]["destination_definition_id"]
            print(destination_definition_id)
        else:
            print(" destino no existe, se procede a crear ...")




        ## get destin defini spec
        destination_definition_specification_api_instance = destination_definition_specification_api.DestinationDefinitionSpecificationApi(api_client)
        destination_definition_specification_res = DestinationDefinitionSpecification(destination_definition_specification_api_instance).get_destination_definition_specification(destination_definition_id)
        print("destination_definition_specification_res<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        ttd =destination_definition_specification_res.__dict__

        print(ttd["_data_store"]["connection_specification"]["properties"])

        destination_api_instance = destination_api.DestinationApi(api_client)
        destination = Destination(destination_api_instance)

        destination_configuration = {
            "database": "postgres",
            "host": "35.196.111.83",
            "username": "postgres",
            "password": "bm9tZXZlYXM=",
            "port": 5432,
            "schema": "public"
        }
        print("create destino zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        create_desti = destination.create_destination(workspace_id=workspace_id, name="outdest", destination_definition_id=destination_definition_id, connection_configuration=destination_configuration )
        print(create_desti)
        time.sleep(10)

        g_destination_id = '760f0492-00b7-4e72-812a-8b0f5a77febb'
        check_destination = destination.check_connection_to_destination(g_destination_id)
        destination_check_status = check_destination.__dict__["_data_store"]["status"]
        print("destination_check_status")
        print(destination_check_status)

        ### a las pruebas de connection agregarles recursividad de retry

        connection_api_instance = connection_api.ConnectionApi(api_client)
        connection_inst = Connection(connection_api_instance)

        connection_name = 'name_example'

        connections_lst = connection_inst.list_connections_for_workspace(workspace_id)
        print("connections_lst xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        get_connections_lst = connections_lst.__dict__["_data_store"]["connections"]
        print(get_connections_lst)

        print("find_connection------------------------------------------------------------")
        find_connection = list( filter( lambda x: x["name"] == connection_name, get_connections_lst) )
        print(find_connection)
        if len(find_connection) > 0:
            connection_id = find_connection[0]["connection_id"]
            print("existe")
            print(connection_id)
        else:
            res_create = connection_inst.create_connection()
            print("create conn >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(res_create)
            connection_id = 'b2188460-ce5e-4f7f-a201-9f61023719aa'
            print("creado")

        print("run_trigger<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        res_trigger = connection_inst.trigger_manual_sync(connection_id)
        tr = res_trigger.__dict__["_data_store"]["job"]
        job_id = tr["id"]
        print(tr)
        print(job_id)

        print("monitor job <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        jobs_api_instance = jobs_api.JobsApi(api_client)
        job_inst = Job(jobs_api_instance)
        while True:
            time.sleep(10)
            print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
            mon_job = job_inst.get_job_debug_info(job_id)
            print(mon_job)







