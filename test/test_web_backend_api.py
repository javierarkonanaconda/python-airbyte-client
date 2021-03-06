"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints. * All `web_backend` APIs are not considered public APIs and are not guaranteeing backwards compatibility.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api.web_backend_api import WebBackendApi  # noqa: E501


class TestWebBackendApi(unittest.TestCase):
    """WebBackendApi unit test stubs"""

    def setUp(self):
        self.api = WebBackendApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_web_backend_create_connection(self):
        """Test case for web_backend_create_connection

        Create a connection  # noqa: E501
        """
        pass

    def test_web_backend_get_connection(self):
        """Test case for web_backend_get_connection

        Get a connection  # noqa: E501
        """
        pass

    def test_web_backend_get_workspace_state(self):
        """Test case for web_backend_get_workspace_state

        Returns the current state of a workspace  # noqa: E501
        """
        pass

    def test_web_backend_list_all_connections_for_workspace(self):
        """Test case for web_backend_list_all_connections_for_workspace

        Returns all connections for a workspace.  # noqa: E501
        """
        pass

    def test_web_backend_list_connections_for_workspace(self):
        """Test case for web_backend_list_connections_for_workspace

        Returns all non-deleted connections for a workspace.  # noqa: E501
        """
        pass

    def test_web_backend_search_connections(self):
        """Test case for web_backend_search_connections

        Search connections  # noqa: E501
        """
        pass

    def test_web_backend_update_connection(self):
        """Test case for web_backend_update_connection

        Update a connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
