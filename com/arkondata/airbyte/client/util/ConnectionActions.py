from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.connection_api import ConnectionApi
from com.arkondata.airbyte.client.model.airbyte_catalog import AirbyteCatalog
from com.arkondata.airbyte.client.model.airbyte_stream import AirbyteStream
from com.arkondata.airbyte.client.model.airbyte_stream_and_configuration import AirbyteStreamAndConfiguration
from com.arkondata.airbyte.client.model.airbyte_stream_configuration import AirbyteStreamConfiguration
from com.arkondata.airbyte.client.model.connection_create import ConnectionCreate
from com.arkondata.airbyte.client.model.connection_id_request_body import ConnectionIdRequestBody
from com.arkondata.airbyte.client.model.connection_schedule import ConnectionSchedule
from com.arkondata.airbyte.client.model.connection_status import ConnectionStatus
from com.arkondata.airbyte.client.model.destination_sync_mode import DestinationSyncMode
from com.arkondata.airbyte.client.model.namespace_definition_type import NamespaceDefinitionType
from com.arkondata.airbyte.client.model.resource_requirements import ResourceRequirements
from com.arkondata.airbyte.client.model.sync_mode import SyncMode
from com.arkondata.airbyte.client.model.workspace_id_request_body import WorkspaceIdRequestBody


class Connection:
    def __init__(self, connection_api_instance: ConnectionApi):
        if connection_api_instance is not None:
            self.connection_api_instance = connection_api_instance
        else:
            raise Exception("error on destination_api_instance")

    def create_connection(self, name, namespace_definition, namespace_format, source_id, destination_id, stream_source_name, stream_sync_mode, stream_namespace, stream_destination_sync_mode, stream_destination_alias_name, stream_source_defined_cursor, status, stream_destination_selected, json_schema, operation_ids: list = [], stream_source_default_cursor_field: list = [], stream_source_defined_primary_key: list = [], stream_destination_cursor_field: list = [], stream_destination_primary_key: list = []):  ###pending , tambien los demas create
        try:
            connection_create = ConnectionCreate(
                name=name,
                namespace_definition=NamespaceDefinitionType(namespace_definition), ###Destination Namespace* ->  ["source", "destination", "customformat", ]
                namespace_format=namespace_format,###
                source_id=source_id,
                destination_id=destination_id,
                operation_ids=operation_ids,
                sync_catalog=AirbyteCatalog(
                    streams=[
                        AirbyteStreamAndConfiguration(
                            stream=AirbyteStream(
                                name=stream_source_name,
                                json_schema=json_schema,
                                supported_sync_modes=[
                                    SyncMode(stream_sync_mode),
                                ],
                                source_defined_cursor=stream_source_defined_cursor,
                                default_cursor_field=stream_source_default_cursor_field, ## Used in incremental sync mode only. It determines which records to sync.
                                source_defined_primary_key=stream_source_defined_primary_key,
                                namespace=stream_namespace,
                            ),
                            config=AirbyteStreamConfiguration(
                                sync_mode=SyncMode(stream_sync_mode),
                                cursor_field=stream_destination_cursor_field,
                                destination_sync_mode=DestinationSyncMode(stream_destination_sync_mode),
                                primary_key=stream_destination_primary_key,
                                alias_name=stream_destination_alias_name,
                                selected=stream_destination_selected,
                            ),
                        ),
                    ],
                ),
                status=ConnectionStatus(status),
            )
            api_response = self.connection_api_instance.create_connection(connection_create)
            return api_response
        except ApiException as e:
            print("Exception when calling ConnectionApi->create_connection: %s\n" % e)

    def delete_connection(self, connection_id):
        try:
            connection_id_request_body = ConnectionIdRequestBody(
                connection_id=connection_id,
            )
            self.connection_api_instance.delete_connection(connection_id_request_body)
        except ApiException as e:
            print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)

    def get_connection(self, connection_id):
        try:
            connection_id_request_body = ConnectionIdRequestBody(
                connection_id=connection_id,
            )
            api_response = self.connection_api_instance.get_connection(connection_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling ConnectionApi->get_connection: %s\n" % e)

    def get_state(self, connection_id):
        try:
            connection_id_request_body = ConnectionIdRequestBody(
                connection_id=connection_id,
            )
            api_response = self.connection_api_instance.get_state(connection_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling ConnectionApi->get_state: %s\n" % e)

    def list_all_connections_for_workspace(self, workspace_id):
        try:
            workspace_id_request_body = WorkspaceIdRequestBody(
                workspace_id=workspace_id,
            )
            api_response = self.connection_api_instance.list_all_connections_for_workspace(workspace_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling ConnectionApi->list_all_connections_for_workspace: %s\n" % e)

    def list_connections_for_workspace(self, workspace_id):
        try:
            workspace_id_request_body = WorkspaceIdRequestBody(
                workspace_id=workspace_id,
            )
            api_response = self.connection_api_instance.list_connections_for_workspace(workspace_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling ConnectionApi->list_connections_for_workspace: %s\n" % e)

    def trigger_manual_sync(self, connection_id):
        connection_id_request_body = ConnectionIdRequestBody(
            connection_id=connection_id,
        )
        try:
            api_response = self.connection_api_instance.sync_connection(connection_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling ConnectionApi->sync_connection: %s\n" % e)
