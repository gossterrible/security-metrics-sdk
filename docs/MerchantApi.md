# swagger_client.MerchantApi

All URIs are relative to *https://www.securitymetrics.com/smapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_merchant**](MerchantApi.md#create_merchant) | **POST** /partners/{partner_uuid}/merchants | Create a Merchant
[**delete_merchant**](MerchantApi.md#delete_merchant) | **DELETE** /merchants/{merchant_uuid} | Delete a Merchant by UUID
[**get_merchant**](MerchantApi.md#get_merchant) | **GET** /merchants/{merchant_uuid} | Find a single Merchant using their UUID
[**get_merchant_compliance**](MerchantApi.md#get_merchant_compliance) | **GET** /merchants/{merchant_uuid}/compliance | Find the compliance information for a single Merchant using their UUID
[**get_merchants**](MerchantApi.md#get_merchants) | **GET** /merchants | Get all Merchants
[**get_merchants_by_partner_id**](MerchantApi.md#get_merchants_by_partner_id) | **GET** /partners/{partner_uuid}/merchants | Get Merchants by Partner
[**update_merchant**](MerchantApi.md#update_merchant) | **PUT** /merchants/{merchant_uuid} | Update the information of a single Merchant

# **create_merchant**
> MerchantWithLinks create_merchant(body, partner_uuid)

Create a Merchant

Create a Merchant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
body = swagger_client.MerchantPost() # MerchantPost | Merchant to be added to the system
partner_uuid = 'partner_uuid_example' # str | UUID of Partner to add Merchant to

try:
    # Create a Merchant
    api_response = api_instance.create_merchant(body, partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantApi->create_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantPost**](MerchantPost.md)| Merchant to be added to the system | 
 **partner_uuid** | **str**| UUID of Partner to add Merchant to | 

### Return type

[**MerchantWithLinks**](MerchantWithLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.sm-api-v1+json
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_merchant**
> delete_merchant(merchant_uuid)

Delete a Merchant by UUID

Delete a Merchant by UUID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
merchant_uuid = 'merchant_uuid_example' # str | UUID of Merchant to delete

try:
    # Delete a Merchant by UUID
    api_instance.delete_merchant(merchant_uuid)
except ApiException as e:
    print("Exception when calling MerchantApi->delete_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_uuid** | **str**| UUID of Merchant to delete | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant**
> MerchantWithLinks get_merchant(merchant_uuid)

Find a single Merchant using their UUID

Returns a Merchant and related metadata by UUID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
merchant_uuid = 'merchant_uuid_example' # str | UUID of Merchant to query

try:
    # Find a single Merchant using their UUID
    api_response = api_instance.get_merchant(merchant_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantApi->get_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_uuid** | **str**| UUID of Merchant to query | 

### Return type

[**MerchantWithLinks**](MerchantWithLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_compliance**
> ComplianceGet get_merchant_compliance(merchant_uuid)

Find the compliance information for a single Merchant using their UUID

Returns the compliance information of a single Merchant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
merchant_uuid = 'merchant_uuid_example' # str | UUID of Merchant to query

try:
    # Find the compliance information for a single Merchant using their UUID
    api_response = api_instance.get_merchant_compliance(merchant_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantApi->get_merchant_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_uuid** | **str**| UUID of Merchant to query | 

### Return type

[**ComplianceGet**](ComplianceGet.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants**
> LinkedMerchantEntries get_merchants(sfdc_network_member_id=sfdc_network_member_id, last_modified_date=last_modified_date, last_synced_date=last_synced_date, unsynced=unsynced, mid=mid)

Get all Merchants

Returns all Merchants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
sfdc_network_member_id = 'sfdc_network_member_id_example' # str | (Internal Use) Salesforce network member id. 'null' returns all records with a null sfdc_network_member_id. (optional)
last_modified_date = 'last_modified_date_example' # str | (Internal Use) date merchant was last modified (optional)
last_synced_date = 'last_synced_date_example' # str | (Internal Use) date merchant was last synced (optional)
unsynced = true # bool | (Internal Use) check if merchant.last_changed > merchant.last_synced_date (optional)
mid = 'mid_example' # str | Merchant ID (optional)

try:
    # Get all Merchants
    api_response = api_instance.get_merchants(sfdc_network_member_id=sfdc_network_member_id, last_modified_date=last_modified_date, last_synced_date=last_synced_date, unsynced=unsynced, mid=mid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantApi->get_merchants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sfdc_network_member_id** | **str**| (Internal Use) Salesforce network member id. &#x27;null&#x27; returns all records with a null sfdc_network_member_id. | [optional] 
 **last_modified_date** | **str**| (Internal Use) date merchant was last modified | [optional] 
 **last_synced_date** | **str**| (Internal Use) date merchant was last synced | [optional] 
 **unsynced** | **bool**| (Internal Use) check if merchant.last_changed &gt; merchant.last_synced_date | [optional] 
 **mid** | **str**| Merchant ID | [optional] 

### Return type

[**LinkedMerchantEntries**](LinkedMerchantEntries.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants_by_partner_id**
> LinkedMerchantEntries get_merchants_by_partner_id(partner_uuid)

Get Merchants by Partner

Returns all Merchants for Partner by UUID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
partner_uuid = 'partner_uuid_example' # str | UUID of Partner to query for Merchants

try:
    # Get Merchants by Partner
    api_response = api_instance.get_merchants_by_partner_id(partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantApi->get_merchants_by_partner_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_uuid** | **str**| UUID of Partner to query for Merchants | 

### Return type

[**LinkedMerchantEntries**](LinkedMerchantEntries.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_merchant**
> MerchantWithLinks update_merchant(body, merchant_uuid)

Update the information of a single Merchant

Update Merchant info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MerchantApi(swagger_client.ApiClient(configuration))
body = swagger_client.MerchantPut() # MerchantPut | Fields to be updated on the Merchant
merchant_uuid = 'merchant_uuid_example' # str | UUID of a Merchant to update

try:
    # Update the information of a single Merchant
    api_response = api_instance.update_merchant(body, merchant_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantApi->update_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantPut**](MerchantPut.md)| Fields to be updated on the Merchant | 
 **merchant_uuid** | **str**| UUID of a Merchant to update | 

### Return type

[**MerchantWithLinks**](MerchantWithLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.sm-api-v1+json
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

