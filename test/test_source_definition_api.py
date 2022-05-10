"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints. * All `web_backend` APIs are not considered public APIs and are not guaranteeing backwards compatibility.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api.source_definition_api import SourceDefinitionApi  # noqa: E501


class TestSourceDefinitionApi(unittest.TestCase):
    """SourceDefinitionApi unit test stubs"""

    def setUp(self):
        self.api = SourceDefinitionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_custom_source_definition(self):
        """Test case for create_custom_source_definition

        Creates a custom sourceDefinition for the given workspace  # noqa: E501
        """
        pass

    def test_create_source_definition(self):
        """Test case for create_source_definition

        Creates a sourceDefinition  # noqa: E501
        """
        pass

    def test_delete_custom_source_definition(self):
        """Test case for delete_custom_source_definition

        Delete a custom source definition for the given workspace  # noqa: E501
        """
        pass

    def test_delete_source_definition(self):
        """Test case for delete_source_definition

        Delete a source definition  # noqa: E501
        """
        pass

    def test_get_source_definition(self):
        """Test case for get_source_definition

        Get source  # noqa: E501
        """
        pass

    def test_get_source_definition_for_workspace(self):
        """Test case for get_source_definition_for_workspace

        Get a sourceDefinition that is configured for the given workspace  # noqa: E501
        """
        pass

    def test_grant_source_definition_to_workspace(self):
        """Test case for grant_source_definition_to_workspace

        grant a private, non-custom sourceDefinition to a given workspace  # noqa: E501
        """
        pass

    def test_list_latest_source_definitions(self):
        """Test case for list_latest_source_definitions

        List the latest sourceDefinitions Airbyte supports  # noqa: E501
        """
        pass

    def test_list_private_source_definitions(self):
        """Test case for list_private_source_definitions

        List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.  # noqa: E501
        """
        pass

    def test_list_source_definitions(self):
        """Test case for list_source_definitions

        List all the sourceDefinitions the current Airbyte deployment is configured to use  # noqa: E501
        """
        pass

    def test_list_source_definitions_for_workspace(self):
        """Test case for list_source_definitions_for_workspace

        List all the sourceDefinitions the given workspace is configured to use  # noqa: E501
        """
        pass

    def test_revoke_source_definition_from_workspace(self):
        """Test case for revoke_source_definition_from_workspace

        revoke a grant to a private, non-custom sourceDefinition from a given workspace  # noqa: E501
        """
        pass

    def test_update_custom_source_definition(self):
        """Test case for update_custom_source_definition

        Update a custom sourceDefinition for the given workspace  # noqa: E501
        """
        pass

    def test_update_source_definition(self):
        """Test case for update_source_definition

        Update a sourceDefinition  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()