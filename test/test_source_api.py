"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints. * All `web_backend` APIs are not considered public APIs and are not guaranteeing backwards compatibility.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api.source_api import SourceApi  # noqa: E501


class TestSourceApi(unittest.TestCase):
    """SourceApi unit test stubs"""

    def setUp(self):
        self.api = SourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_connection_to_source(self):
        """Test case for check_connection_to_source

        Check connection to the source  # noqa: E501
        """
        pass

    def test_check_connection_to_source_for_update(self):
        """Test case for check_connection_to_source_for_update

        Check connection for a proposed update to a source  # noqa: E501
        """
        pass

    def test_clone_source(self):
        """Test case for clone_source

        Clone source  # noqa: E501
        """
        pass

    def test_create_source(self):
        """Test case for create_source

        Create a source  # noqa: E501
        """
        pass

    def test_delete_source(self):
        """Test case for delete_source

        Delete a source  # noqa: E501
        """
        pass

    def test_discover_schema_for_source(self):
        """Test case for discover_schema_for_source

        Discover the schema catalog of the source  # noqa: E501
        """
        pass

    def test_get_source(self):
        """Test case for get_source

        Get source  # noqa: E501
        """
        pass

    def test_list_sources_for_workspace(self):
        """Test case for list_sources_for_workspace

        List sources for workspace  # noqa: E501
        """
        pass

    def test_search_sources(self):
        """Test case for search_sources

        Search sources  # noqa: E501
        """
        pass

    def test_update_source(self):
        """Test case for update_source

        Update a source  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
