"""
    Open-Needs Server

    REST API Server of Open-Needs  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import on_sdk
from on_sdk.api.filter_api import FilterApi  # noqa: E501


class TestFilterApi(unittest.TestCase):
    """FilterApi unit test stubs"""

    def setUp(self):
        self.api = FilterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_filter_needs_api_filter_needs_post(self):
        """Test case for filter_needs_api_filter_needs_post

        Filter Needs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()