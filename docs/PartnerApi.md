# swagger_client.PartnerApi

All URIs are relative to *https://www.securitymetrics.com/smapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank**](PartnerApi.md#create_bank) | **POST** /partners | Create a Partner
[**create_merchant**](PartnerApi.md#create_merchant) | **POST** /partners/{partner_uuid}/merchants | Create a Merchant
[**get_active_campaign_list_for_bank_uuid**](PartnerApi.md#get_active_campaign_list_for_bank_uuid) | **GET** /partners/{partner_uuid}/active_campaign_emails | Find active_campaign_emails
[**get_merchants_by_partner_id**](PartnerApi.md#get_merchants_by_partner_id) | **GET** /partners/{partner_uuid}/merchants | Get Merchants by Partner
[**get_partners**](PartnerApi.md#get_partners) | **GET** /partners | Get all Partners
[**get_partners_by_id**](PartnerApi.md#get_partners_by_id) | **GET** /partners/{partner_uuid} | Find an Partner by their UUID
[**modify_active_campaign_for_bank_uuid**](PartnerApi.md#modify_active_campaign_for_bank_uuid) | **PUT** /partners/{partner_uuid}/active_campaign_emails/{campaign_email_uuid} | Start or stop a campaign
[**update_bank_by_uuid**](PartnerApi.md#update_bank_by_uuid) | **PUT** /partners/{partner_uuid} | Update the information of a single Partner

# **create_bank**
> PartnerWithLinks create_bank(body)

Create a Partner

Create a Partner

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PartnerPost() # PartnerPost | Partner to be added to the system

try:
    # Create a Partner
    api_response = api_instance.create_bank(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->create_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerPost**](PartnerPost.md)| Partner to be added to the system | 

### Return type

[**PartnerWithLinks**](PartnerWithLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.sm-api-v1+json
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
body = swagger_client.MerchantPost() # MerchantPost | Merchant to be added to the system
partner_uuid = 'partner_uuid_example' # str | UUID of Partner to add Merchant to

try:
    # Create a Merchant
    api_response = api_instance.create_merchant(body, partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->create_merchant: %s\n" % e)
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

# **get_active_campaign_list_for_bank_uuid**
> CampaignEmailWithoutLinks get_active_campaign_list_for_bank_uuid(partner_uuid)

Find active_campaign_emails

Returns a List of active_campaign_emails for this Partner

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
partner_uuid = 'partner_uuid_example' # str | UUID of Partner to query

try:
    # Find active_campaign_emails
    api_response = api_instance.get_active_campaign_list_for_bank_uuid(partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->get_active_campaign_list_for_bank_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_uuid** | **str**| UUID of Partner to query | 

### Return type

[**CampaignEmailWithoutLinks**](CampaignEmailWithoutLinks.md)

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
partner_uuid = 'partner_uuid_example' # str | UUID of Partner to query for Merchants

try:
    # Get Merchants by Partner
    api_response = api_instance.get_merchants_by_partner_id(partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->get_merchants_by_partner_id: %s\n" % e)
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

# **get_partners**
> LinkedPartnerEntries get_partners(last_modified_date=last_modified_date)

Get all Partners

Return all Partners and related metadata

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
last_modified_date = '2013-10-20' # date | Include partners with changes since this date (optional)

try:
    # Get all Partners
    api_response = api_instance.get_partners(last_modified_date=last_modified_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->get_partners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_modified_date** | **date**| Include partners with changes since this date | [optional] 

### Return type

[**LinkedPartnerEntries**](LinkedPartnerEntries.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partners_by_id**
> PartnerWithLinks get_partners_by_id(partner_uuid)

Find an Partner by their UUID

Returns an Partner and related metadata by UUID

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
partner_uuid = 'partner_uuid_example' # str | UUID of Partner to query

try:
    # Find an Partner by their UUID
    api_response = api_instance.get_partners_by_id(partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->get_partners_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_uuid** | **str**| UUID of Partner to query | 

### Return type

[**PartnerWithLinks**](PartnerWithLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_active_campaign_for_bank_uuid**
> CampaignEmailWithoutLinks modify_active_campaign_for_bank_uuid(body, partner_uuid, campaign_email_uuid)

Start or stop a campaign

Start/Stop Campaign emails

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CampaignEmailPut() # CampaignEmailPut | Fields to be updated on the Partner
partner_uuid = 'partner_uuid_example' # str | UUID of a Partner who owns the Campaign
campaign_email_uuid = 'campaign_email_uuid_example' # str | UUID of a CampaignEmail to update

try:
    # Start or stop a campaign
    api_response = api_instance.modify_active_campaign_for_bank_uuid(body, partner_uuid, campaign_email_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->modify_active_campaign_for_bank_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CampaignEmailPut**](CampaignEmailPut.md)| Fields to be updated on the Partner | 
 **partner_uuid** | **str**| UUID of a Partner who owns the Campaign | 
 **campaign_email_uuid** | **str**| UUID of a CampaignEmail to update | 

### Return type

[**CampaignEmailWithoutLinks**](CampaignEmailWithoutLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.sm-api-v1+json
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_by_uuid**
> PartnerWithLinks update_bank_by_uuid(body, partner_uuid)

Update the information of a single Partner

Update Partner info

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
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PartnerPut() # PartnerPut | Fields to be updated on the Partner
partner_uuid = 'partner_uuid_example' # str | UUID of a Partner to update

try:
    # Update the information of a single Partner
    api_response = api_instance.update_bank_by_uuid(body, partner_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->update_bank_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerPut**](PartnerPut.md)| Fields to be updated on the Partner | 
 **partner_uuid** | **str**| UUID of a Partner to update | 

### Return type

[**PartnerWithLinks**](PartnerWithLinks.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.sm-api-v1+json
 - **Accept**: application/json, application/vnd.sm-api-v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

