# on_sdk.NeedsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_need_api_needs_post**](NeedsApi.md#create_need_api_needs_post) | **POST** /api/needs/ | Create Need
[**read_items_api_needs_get**](NeedsApi.md#read_items_api_needs_get) | **GET** /api/needs/ | Read Items


# **create_need_api_needs_post**
> Need create_need_api_needs_post(need_create)

Create Need

### Example


```python
import time
import on_sdk
from on_sdk.api import needs_api
from on_sdk.model.need_create import NeedCreate
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.need import Need
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = needs_api.NeedsApi(api_client)
    need_create = NeedCreate(
        title="title_example",
        description="description_example",
        project_id=1,
        meta={
            "key": None,
        },
    ) # NeedCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Need
        api_response = api_instance.create_need_api_needs_post(need_create)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling NeedsApi->create_need_api_needs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **need_create** | [**NeedCreate**](NeedCreate.md)|  |

### Return type

[**Need**](Need.md)

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

# **read_items_api_needs_get**
> [Need] read_items_api_needs_get()

Read Items

### Example


```python
import time
import on_sdk
from on_sdk.api import needs_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.need import Need
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = needs_api.NeedsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Items
        api_response = api_instance.read_items_api_needs_get(skip=skip, limit=limit)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling NeedsApi->read_items_api_needs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**[Need]**](Need.md)

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

