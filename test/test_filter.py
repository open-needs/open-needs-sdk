"""
    Open-Needs Server

    REST API Server of Open-Needs  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import on_sdk
from on_sdk.model.need_filter import NeedFilter
globals()['NeedFilter'] = NeedFilter
from on_sdk.model.filter import Filter


class TestFilter(unittest.TestCase):
    """Filter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFilter(self):
        """Test Filter"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Filter()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()