import json
import time

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api import workspace_api, destination_api, source_definition_api, \
    source_definition_specification_api, source_api, destination_definition_specification_api, \
    destination_definition_api, connection_api, jobs_api, operation_api
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
from com.arkondata.airbyte.client.util.OperationActions import Operation
from com.arkondata.airbyte.client.util.SourceActions import Source
from com.arkondata.airbyte.client.util.SourceDefinitionActions import SourceDefinition
from com.arkondata.airbyte.client.util.SourceDefinitionSpecificationActions import SourceDefinitionSpecification
from com.arkondata.airbyte.client.util.WorkspaceActions import Workspace

workspace_name = '02bde510-f5b1-4aeb-b390-086b8d764e1d'  ###"javstest"
source_ds = "postgres"
destination_ds = "snowflake"
table_name = "prueba"

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


def get_json_schema(obj):
    if obj != None:
        obj_dict = obj.__dict__
        stream = obj_dict["_data_store"]["stream"]
        res = {
            "name":stream["name"],
            "json_schema":stream["json_schema"]
        }
        return res
    else:
        return {}

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
        g_source_id = create_source_res.__dict__["_data_store"]["source_id"]
        print(f"source id ---> {g_source_id}")
        print("check source connection wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        check_source = source_inst.check_connection_to_source(g_source_id)
        if check_source != None:
            connection_status = check_source.__dict__["_data_store"].get("status", None)
            print(connection_status)
        else:
            raise Exception("error al checar el source")


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

        destination_api_instance = destination_api.DestinationApi(api_client)
        destination = Destination(destination_api_instance)

        destination_configuration = {
            "host":"ee52075.us-east-2.aws.snowflakecomputing.com",
            "role":"ACCOUNTADMIN",
            "schema":"PUBLIC",
            "database":"pg",
            "username":"javierorta",
            "warehouse":"COMPUTE_WH",
            "credentials":{
                'password': "**18DeMayoDe1995##"
            }

        }
        print("create destino zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        create_desti = destination.create_destination(workspace_id=workspace_id, name="outdest", destination_definition_id=destination_definition_id, connection_configuration=destination_configuration )
        print(create_desti.__dict__)
        time.sleep(10)

        g_destination_id = create_desti.__dict__["_data_store"]["destination_id"]
        print(f"dest id ---> {g_destination_id}")
        check_destination = destination.check_connection_to_destination(g_destination_id)
        destination_check_status = check_destination.__dict__["_data_store"]["status"]
        print("destination_check_status wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
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

            get_source_schemas = source_inst.discover_schema_for_source(g_source_id)
            print("get_source_schemas XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(get_source_schemas.__dict__)
            print("ñññññññ")
            stream_source_catalog = get_source_schemas.__dict__["_data_store"]["catalog"].__dict__["_data_store"]["streams"]

            map1 = list( map( lambda x: get_json_schema(x) , stream_source_catalog) )
            print("map1")
            print(map1)
            print(type(map1))
            #33filter_by_table = list( map( lambda x: x.keys() , map1) )
            filter_by_table = list( filter(lambda x: dict(x).get("name", "") == table_name, map1))
            print(filter_by_table)

            if len(filter_by_table) > 0:
                get_json_schema = filter_by_table[0]["json_schema"]
                print("get_json_schema ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
                print(get_json_schema)
                print(type(get_json_schema))

            ### create basic operation
            operation_api_instance = operation_api.OperationApi(api_client)
            operation_inst = Operation(operation_api_instance)
            res_create_op = operation_inst.create_operation(workspace_id,"Normalization","normalization","basic", False).__dict__
            print("res_create_op <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print(res_create_op)
            print(type(res_create_op))

            get_operation_id = res_create_op["_data_store"]["operation_id"]
            print("get_operation_id kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            print(get_operation_id)

            ### create connection
            ## nota: el nombre de la tabla del destino debe ser el mismo que el del source, eso automaticamente lo mapea y asi es como lo maneja airbyte, lel nombre de las tablas es el mismo en ambos source y destino, tomando como base el source
            name = "testconnection"
            namespace_definition = "source"  ## Allowed: source┃destination┃customformat
            namespace_format = '${SOURCE_NAMESPACE}'  ##"public" ## db schema connection sink ## Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
            source_id = g_source_id  ## source_id
            destination_id = g_destination_id  ## destination_id
            stream_name = table_name  ## is the raw table name from your source.
            stream_sync_mode = "full_refresh"  ## existen varios tipos de sync
            stream_namespace = "public"  ## db schema connection source
            destination_sync_mode = "overwrite"  ## must be one of ['append', 'overwrite', 'append_dedup']
            stream_alias_name = table_name
            stream_source_defined_cursor = None  ## es true o false
            status = "active"
            stream_selected = True
            json_schema = get_json_schema##{'properties': {'description': {'type': 'string'}, 'id': {'type': 'number'}},'type': 'object'}
            operation_ids = [get_operation_id] ## basic normalization

            res_create = connection_inst.create_connection( name, namespace_definition, namespace_format, source_id, destination_id, stream_name, stream_sync_mode, stream_namespace, destination_sync_mode, stream_alias_name, stream_source_defined_cursor, status, stream_selected, json_schema, operation_ids)
            print("create conn >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(res_create)
            print("creado")

        connection_id = res_create.__dict__["_data_store"]["connection_id"]
        print(f"connection_id -> {connection_id}")

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







