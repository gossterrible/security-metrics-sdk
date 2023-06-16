# PartnerWithLinks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**auto_emails** | **bool** | If True, we will send automated emails to merchants of this Partner | [optional] 
**date_created** | **date** | The date this Partner was created | [optional] 
**disable_mcc_export** | **bool** | If True, then the Partner cannot export merchants in Partner+ | [optional] 
**do_not_call** | **bool** | If True, then we should not call this Partner&#x27;s merchants | [optional] 
**do_not_change_customer_info** | **bool** | Do not allow certain customer info to be changed | [optional] 
**enable_qir** | **bool** | The QIR program is applicable for the Partner and merchants | [optional] 
**enable_shopping_cart** | **bool** | Ability to enable the online shopping cart for users | [optional] 
**id_and_verify_items** | **str** | The items that the Partner wants identified and verified when merchants call in | [optional] 
**instructions** | **str** | Instructions for SecurityMetrics Agents when working with Merchants of this Partner | [optional] 
**landing_merchant_creation** | **bool** | Whether this Partner has allowed merchant records to be created from their custom landing page | [optional] 
**masquerade** | **bool** | The Partner has Masquerade abilities | [optional] 
**max_emails_per_day** | **int** | The max number of emals we send to the Merchants of this Partner per day. 0 means no limit | [optional] 
**mid_match_required** | **bool** | Whether this Partner requires MID matching as a part of the online setup and purchase process | [optional] 
**misc1_field_name** | **str** | The Partner-chosen name of the Merchant misc1 field | [optional] 
**misc2_field_name** | **str** | The Partner-chosen name of the Merchant misc2 field | [optional] 
**misc3_field_name** | **str** | The Partner-chosen name of the Merchant misc3 field | [optional] 
**misc4_field_name** | **str** | The Partner-chosen name of the Merchant misc4 field | [optional] 
**name** | **str** | The name of the Partner | [optional] 
**preferred_name** | **str** | An optional customer-facing name of the Partner | [optional] 
**reports_discover** | **bool** | This Partner has access to the Discover report | [optional] 
**reports_fastpass** | **bool** | This Partner has access to the Fastpass Responses report | [optional] 
**reports_first_data_l4** | **bool** | This Partner has access to the First Data Opt Out report | [optional] 
**reports_mastercard** | **bool** | This Partner has access to the MasterCard report | [optional] 
**reports_visa_asia_pacific** | **bool** | This Partner has access to the Visa Asia Pacific report | [optional] 
**reports_visa_europe** | **bool** | This Partner has access to the Visa Europe report | [optional] 
**reports_visa_north_america** | **bool** | This Partner has access to the Visa North America report | [optional] 
**reports_weekly_stats** | **bool** | This Partner has access to the Weekly Stats report | [optional] 
**require_id_and_verify** | **bool** | The Partner requires SecurityMetrics to identify and verify certain information of merchants when they call in | [optional] 
**saq3_confirm_all** | **bool** | Allow customers the option to answer \&quot;yes\&quot; to all questions in each section of the SAQ | [optional] 
**saq_d_support** | **bool** | Whether the Merchants of this Partner are required to purchase support for SAQ D | [optional] 
**saq_response_options** | **str** | The type of response options available to a Partner&#x27;s merchants on SAQs | [optional] 
**show_goals** | **bool** | Show goals | [optional] 
**uuid** | **str** | The Universal Unique IDentifier for this Partner | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

