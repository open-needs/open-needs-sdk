# on_sdk.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_api_organizations_post**](OrganizationsApi.md#create_organization_api_organizations_post) | **POST** /api/organizations/ | Create Organization
[**read_organization_api_organizations_organization_id_get**](OrganizationsApi.md#read_organization_api_organizations_organization_id_get) | **GET** /api/organizations/{organization_id} | Read Organization
[**read_organizations_api_organizations_get**](OrganizationsApi.md#read_organizations_api_organizations_get) | **GET** /api/organizations/ | Read Organizations


# **create_organization_api_organizations_post**
> Organization create_organization_api_organizations_post(organization_create)

Create Organization

### Example


```python
import time
import on_sdk
from on_sdk.api import organizations_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.organization import Organization
from on_sdk.model.organization_create import OrganizationCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    organization_create = OrganizationCreate(
        title="title_example",
    ) # OrganizationCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Organization
        api_response = api_instance.create_organization_api_organizations_post(organization_create)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->create_organization_api_organizations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_create** | [**OrganizationCreate**](OrganizationCreate.md)|  |

### Return type

[**Organization**](Organization.md)

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

# **read_organization_api_organizations_organization_id_get**
> Organization read_organization_api_organizations_organization_id_get(organization_id)

Read Organization

### Example


```python
import time
import on_sdk
from on_sdk.api import organizations_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    organization_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Read Organization
        api_response = api_instance.read_organization_api_organizations_organization_id_get(organization_id)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->read_organization_api_organizations_organization_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  |

### Return type

[**Organization**](Organization.md)

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

# **read_organizations_api_organizations_get**
> [Organization] read_organizations_api_organizations_get()

Read Organizations

### Example


```python
import time
import on_sdk
from on_sdk.api import organizations_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Organizations
        api_response = api_instance.read_organizations_api_organizations_get(skip=skip, limit=limit)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling OrganizationsApi->read_organizations_api_organizations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**[Organization]**](Organization.md)

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

