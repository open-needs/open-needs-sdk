"""
    Open-Needs Server

    REST API Server of Open-Needs  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import on_sdk
from on_sdk.api.projects_api import ProjectsApi  # noqa: E501


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_api_projects_post(self):
        """Test case for create_project_api_projects_post

        Create Project  # noqa: E501
        """
        pass

    def test_read_project_api_projects_project_id_get(self):
        """Test case for read_project_api_projects_project_id_get

        Read Project  # noqa: E501
        """
        pass

    def test_read_projects_api_projects_get(self):
        """Test case for read_projects_api_projects_get

        Read Projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
