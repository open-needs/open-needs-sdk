# on_sdk.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_api_projects_post**](ProjectsApi.md#create_project_api_projects_post) | **POST** /api/projects/ | Create Project
[**read_project_api_projects_project_id_get**](ProjectsApi.md#read_project_api_projects_project_id_get) | **GET** /api/projects/{project_id} | Read Project
[**read_projects_api_projects_get**](ProjectsApi.md#read_projects_api_projects_get) | **GET** /api/projects/ | Read Projects


# **create_project_api_projects_post**
> Project create_project_api_projects_post(project_create)

Create Project

### Example


```python
import time
import on_sdk
from on_sdk.api import projects_api
from on_sdk.model.project import Project
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.project_create import ProjectCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_create = ProjectCreate(
        title="title_example",
        organization_id=1,
    ) # ProjectCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.create_project_api_projects_post(project_create)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_api_projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_api_projects_project_id_get**
> Project read_project_api_projects_project_id_get(project_id)

Read Project

### Example


```python
import time
import on_sdk
from on_sdk.api import projects_api
from on_sdk.model.project import Project
from on_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Read Project
        api_response = api_instance.read_project_api_projects_project_id_get(project_id)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->read_project_api_projects_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_projects_api_projects_get**
> [Project] read_projects_api_projects_get()

Read Projects

### Example


```python
import time
import on_sdk
from on_sdk.api import projects_api
from on_sdk.model.project import Project
from on_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Projects
        api_response = api_instance.read_projects_api_projects_get(skip=skip, limit=limit)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->read_projects_api_projects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

