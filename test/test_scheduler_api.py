"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints. * All `web_backend` APIs are not considered public APIs and are not guaranteeing backwards compatibility.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.api.scheduler_api import SchedulerApi  # noqa: E501


class TestSchedulerApi(unittest.TestCase):
    """SchedulerApi unit test stubs"""

    def setUp(self):
        self.api = SchedulerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_execute_destination_check_connection(self):
        """Test case for execute_destination_check_connection

        Run check connection for a given destination configuration  # noqa: E501
        """
        pass

    def test_execute_source_check_connection(self):
        """Test case for execute_source_check_connection

        Run check connection for a given source configuration  # noqa: E501
        """
        pass

    def test_execute_source_discover_schema(self):
        """Test case for execute_source_discover_schema

        Run discover schema for a given source a source configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
