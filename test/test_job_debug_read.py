"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints. * All `web_backend` APIs are not considered public APIs and are not guaranteeing backwards compatibility.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import com.arkondata.airbyte.client
from com.arkondata.airbyte.client.model.destination_definition_read import DestinationDefinitionRead
from com.arkondata.airbyte.client.model.job_config_type import JobConfigType
from com.arkondata.airbyte.client.model.job_status import JobStatus
from com.arkondata.airbyte.client.model.source_definition_read import SourceDefinitionRead
globals()['DestinationDefinitionRead'] = DestinationDefinitionRead
globals()['JobConfigType'] = JobConfigType
globals()['JobStatus'] = JobStatus
globals()['SourceDefinitionRead'] = SourceDefinitionRead
from com.arkondata.airbyte.client.model.job_debug_read import JobDebugRead


class TestJobDebugRead(unittest.TestCase):
    """JobDebugRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobDebugRead(self):
        """Test JobDebugRead"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobDebugRead()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
