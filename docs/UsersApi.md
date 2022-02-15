# on_sdk.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_current_user_users_me_get**](UsersApi.md#users_current_user_users_me_get) | **GET** /users/me | Users:Current User
[**users_current_user_users_me_patch**](UsersApi.md#users_current_user_users_me_patch) | **PATCH** /users/me | Users:Current User
[**users_user_users_id_delete**](UsersApi.md#users_user_users_id_delete) | **DELETE** /users/{id} | Users:User
[**users_user_users_id_get**](UsersApi.md#users_user_users_id_get) | **GET** /users/{id} | Users:User
[**users_user_users_id_patch**](UsersApi.md#users_user_users_id_patch) | **PATCH** /users/{id} | Users:User


# **users_current_user_users_me_get**
> User users_current_user_users_me_get()

Users:Current User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import on_sdk
from on_sdk.api import users_api
from on_sdk.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = on_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with on_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Users:Current User
        api_response = api_instance.users_current_user_users_me_get()
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_current_user_users_me_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_current_user_users_me_patch**
> User users_current_user_users_me_patch(user_update)

Users:Current User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import on_sdk
from on_sdk.api import users_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.user_update import UserUpdate
from on_sdk.model.error_model import ErrorModel
from on_sdk.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = on_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with on_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_update = UserUpdate(
        password="password_example",
        email="email_example",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    ) # UserUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Users:Current User
        api_response = api_instance.users_current_user_users_me_patch(user_update)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_current_user_users_me_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**UserUpdate**](UserUpdate.md)|  |

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_users_id_delete**
> users_user_users_id_delete(id)

Users:User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import on_sdk
from on_sdk.api import users_api
from on_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = on_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with on_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Users:User
        api_instance.users_user_users_id_delete(id)
    except on_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_user_users_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_users_id_get**
> User users_user_users_id_get(id)

Users:User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import on_sdk
from on_sdk.api import users_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = on_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with on_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Users:User
        api_response = api_instance.users_user_users_id_get(id)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_user_users_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_users_id_patch**
> User users_user_users_id_patch(id, user_update)

Users:User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import on_sdk
from on_sdk.api import users_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.user_update import UserUpdate
from on_sdk.model.error_model import ErrorModel
from on_sdk.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = on_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with on_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | 
    user_update = UserUpdate(
        password="password_example",
        email="email_example",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    ) # UserUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Users:User
        api_response = api_instance.users_user_users_id_patch(id, user_update)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_user_users_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_update** | [**UserUpdate**](UserUpdate.md)|  |

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

