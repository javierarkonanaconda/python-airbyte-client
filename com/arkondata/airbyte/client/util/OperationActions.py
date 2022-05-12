from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.operation_api import OperationApi
from com.arkondata.airbyte.client.model.connection_id_request_body import ConnectionIdRequestBody
from com.arkondata.airbyte.client.model.operation_create import OperationCreate
from com.arkondata.airbyte.client.model.operator_configuration import OperatorConfiguration
from com.arkondata.airbyte.client.model.operator_dbt import OperatorDbt
from com.arkondata.airbyte.client.model.operator_normalization import OperatorNormalization
from com.arkondata.airbyte.client.model.operator_type import OperatorType


class Operation:

    def __init__(self, operation_api_instance: OperationApi):
        if operation_api_instance is not None:
            self.operation_api_instance = operation_api_instance
        else:
            raise Exception("error on destination_definition_api")

    def list_operations_for_connection(self, connection_id):
        try:
            connection_id_request_body = ConnectionIdRequestBody(
                connection_id=connection_id,
            )

            api_response = self.operation_api_instance.list_operations_for_connection(connection_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling OperationApi->list_operations_for_connection: %s\n" % e)

    def create_operation(self, workspace_id, name, operator_type, operator_normalization, dbt_custom:bool=False, git_repo_url:str = "", git_repo_branch:str="", docker_image:str="", dbt_arguments:str=""):

        dbt_op = None if dbt_custom is False else OperatorDbt(
                        git_repo_url=git_repo_url,
                        git_repo_branch=git_repo_branch,
                        docker_image=docker_image,
                        dbt_arguments=dbt_arguments,
                    )
        try:
            operation_create = OperationCreate(
                workspace_id=workspace_id,
                name=name,
                operator_configuration=OperatorConfiguration(
                    operator_type=OperatorType(operator_type),
                    normalization=OperatorNormalization(
                        option=operator_normalization,
                    ),
                    dbt=dbt_op,
                ),
            )
            api_response = self.operation_api_instance.create_operation(operation_create)
            return api_response
        except ApiException as e:
            print("Exception when calling OperationApi->create_operation: %s\n" % e)