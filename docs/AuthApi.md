# on_sdk.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_jwt_login_auth_jwt_login_post**](AuthApi.md#auth_jwt_login_auth_jwt_login_post) | **POST** /auth/jwt/login | Auth:Jwt.Login
[**auth_jwt_logout_auth_jwt_logout_post**](AuthApi.md#auth_jwt_logout_auth_jwt_logout_post) | **POST** /auth/jwt/logout | Auth:Jwt.Logout
[**register_register_auth_register_post**](AuthApi.md#register_register_auth_register_post) | **POST** /auth/register | Register:Register
[**reset_forgot_password_auth_forgot_password_post**](AuthApi.md#reset_forgot_password_auth_forgot_password_post) | **POST** /auth/forgot-password | Reset:Forgot Password
[**reset_reset_password_auth_reset_password_post**](AuthApi.md#reset_reset_password_auth_reset_password_post) | **POST** /auth/reset-password | Reset:Reset Password
[**verify_request_token_auth_request_verify_token_post**](AuthApi.md#verify_request_token_auth_request_verify_token_post) | **POST** /auth/request-verify-token | Verify:Request-Token
[**verify_verify_auth_verify_post**](AuthApi.md#verify_verify_auth_verify_post) | **POST** /auth/verify | Verify:Verify


# **auth_jwt_login_auth_jwt_login_post**
> BearerResponse auth_jwt_login_auth_jwt_login_post(username, password)

Auth:Jwt.Login

### Example


```python
import time
import on_sdk
from on_sdk.api import auth_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.bearer_response import BearerResponse
from on_sdk.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    username = "username_example" # str | 
    password = "password_example" # str | 
    grant_type = "passwor" # str |  (optional)
    scope = "" # str |  (optional) if omitted the server will use the default value of ""
    client_id = "client_id_example" # str |  (optional)
    client_secret = "client_secret_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Auth:Jwt.Login
        api_response = api_instance.auth_jwt_login_auth_jwt_login_post(username, password)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_login_auth_jwt_login_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Auth:Jwt.Login
        api_response = api_instance.auth_jwt_login_auth_jwt_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_login_auth_jwt_login_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **password** | **str**|  |
 **grant_type** | **str**|  | [optional]
 **scope** | **str**|  | [optional] if omitted the server will use the default value of ""
 **client_id** | **str**|  | [optional]
 **client_secret** | **str**|  | [optional]

### Return type

[**BearerResponse**](BearerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_jwt_logout_auth_jwt_logout_post**
> bool, date, datetime, dict, float, int, list, str, none_type auth_jwt_logout_auth_jwt_logout_post()

Auth:Jwt.Logout

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import on_sdk
from on_sdk.api import auth_api
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Auth:Jwt.Logout
        api_response = api_instance.auth_jwt_logout_auth_jwt_logout_post()
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_logout_auth_jwt_logout_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **register_register_auth_register_post**
> User register_register_auth_register_post(user_create)

Register:Register

### Example


```python
import time
import on_sdk
from on_sdk.api import auth_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.user_create import UserCreate
from on_sdk.model.error_model import ErrorModel
from on_sdk.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    user_create = UserCreate(
        email="email_example",
        password="password_example",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    ) # UserCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Register:Register
        api_response = api_instance.register_register_auth_register_post(user_create)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->register_register_auth_register_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_forgot_password_auth_forgot_password_post**
> bool, date, datetime, dict, float, int, list, str, none_type reset_forgot_password_auth_forgot_password_post(body_reset_forgot_password_auth_forgot_password_post)

Reset:Forgot Password

### Example


```python
import time
import on_sdk
from on_sdk.api import auth_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.body_reset_forgot_password_auth_forgot_password_post import BodyResetForgotPasswordAuthForgotPasswordPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_reset_forgot_password_auth_forgot_password_post = BodyResetForgotPasswordAuthForgotPasswordPost(
        email="email_example",
    ) # BodyResetForgotPasswordAuthForgotPasswordPost | 

    # example passing only required values which don't have defaults set
    try:
        # Reset:Forgot Password
        api_response = api_instance.reset_forgot_password_auth_forgot_password_post(body_reset_forgot_password_auth_forgot_password_post)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->reset_forgot_password_auth_forgot_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_reset_forgot_password_auth_forgot_password_post** | [**BodyResetForgotPasswordAuthForgotPasswordPost**](BodyResetForgotPasswordAuthForgotPasswordPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_reset_password_auth_reset_password_post**
> bool, date, datetime, dict, float, int, list, str, none_type reset_reset_password_auth_reset_password_post(body_reset_reset_password_auth_reset_password_post)

Reset:Reset Password

### Example


```python
import time
import on_sdk
from on_sdk.api import auth_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.body_reset_reset_password_auth_reset_password_post import BodyResetResetPasswordAuthResetPasswordPost
from on_sdk.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_reset_reset_password_auth_reset_password_post = BodyResetResetPasswordAuthResetPasswordPost(
        token="token_example",
        password="password_example",
    ) # BodyResetResetPasswordAuthResetPasswordPost | 

    # example passing only required values which don't have defaults set
    try:
        # Reset:Reset Password
        api_response = api_instance.reset_reset_password_auth_reset_password_post(body_reset_reset_password_auth_reset_password_post)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->reset_reset_password_auth_reset_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_reset_reset_password_auth_reset_password_post** | [**BodyResetResetPasswordAuthResetPasswordPost**](BodyResetResetPasswordAuthResetPasswordPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_request_token_auth_request_verify_token_post**
> bool, date, datetime, dict, float, int, list, str, none_type verify_request_token_auth_request_verify_token_post(body_verify_request_token_auth_request_verify_token_post)

Verify:Request-Token

### Example


```python
import time
import on_sdk
from on_sdk.api import auth_api
from on_sdk.model.body_verify_request_token_auth_request_verify_token_post import BodyVerifyRequestTokenAuthRequestVerifyTokenPost
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
    api_instance = auth_api.AuthApi(api_client)
    body_verify_request_token_auth_request_verify_token_post = BodyVerifyRequestTokenAuthRequestVerifyTokenPost(
        email="email_example",
    ) # BodyVerifyRequestTokenAuthRequestVerifyTokenPost | 

    # example passing only required values which don't have defaults set
    try:
        # Verify:Request-Token
        api_response = api_instance.verify_request_token_auth_request_verify_token_post(body_verify_request_token_auth_request_verify_token_post)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->verify_request_token_auth_request_verify_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_request_token_auth_request_verify_token_post** | [**BodyVerifyRequestTokenAuthRequestVerifyTokenPost**](BodyVerifyRequestTokenAuthRequestVerifyTokenPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verify_auth_verify_post**
> User verify_verify_auth_verify_post(body_verify_verify_auth_verify_post)

Verify:Verify

### Example


```python
import time
import on_sdk
from on_sdk.api import auth_api
from on_sdk.model.http_validation_error import HTTPValidationError
from on_sdk.model.error_model import ErrorModel
from on_sdk.model.user import User
from on_sdk.model.body_verify_verify_auth_verify_post import BodyVerifyVerifyAuthVerifyPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = on_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with on_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_verify_verify_auth_verify_post = BodyVerifyVerifyAuthVerifyPost(
        token="token_example",
    ) # BodyVerifyVerifyAuthVerifyPost | 

    # example passing only required values which don't have defaults set
    try:
        # Verify:Verify
        api_response = api_instance.verify_verify_auth_verify_post(body_verify_verify_auth_verify_post)
        pprint(api_response)
    except on_sdk.ApiException as e:
        print("Exception when calling AuthApi->verify_verify_auth_verify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_verify_auth_verify_post** | [**BodyVerifyVerifyAuthVerifyPost**](BodyVerifyVerifyAuthVerifyPost.md)|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

