# ComplianceGet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**milestone_1** | **float** | Percent complete of Prioritized Approach Milestone 1 | [optional] 
**milestone_2** | **float** | Percent complete of Prioritized Approach Milestone 2 | [optional] 
**milestone_3** | **float** | Percent complete of Prioritized Approach Milestone 3 | [optional] 
**milestone_4** | **float** | Percent complete of Prioritized Approach Milestone 4 | [optional] 
**milestone_5** | **float** | Percent complete of Prioritized Approach Milestone 5 | [optional] 
**milestone_6** | **float** | Percent complete of Prioritized Approach Milestone 6 | [optional] 
**milestone_planned_compliance_date** | **datetime** | Date when the merchant plans to become compliant with the Prioritized Approach Milestone | [optional] 
**next_scan_date_utc** | **datetime** | The date in UTC of the next scan that is going to run on any of the merchant&#x27;s targets | [optional] 
**next_scan_target** | **str** | The target of the next scan that will run for this merchant. | [optional] 
**overall_compliance** | **str** | The Overall PCI Compliance of the merchant | [optional] 
**overall_compliant_date** | **datetime** | The date of the last time the merchant went from Noncompliant to Compliant | [optional] 
**overall_noncompliant_date** | **datetime** | The date of the last time the merchant became Non-Compliant | [optional] 
**saq_expiration** | **datetime** | The expiration date of the SAQ compliance. Will be null if the SAQ is not compliant. | [optional] 
**saq_type** | **str** | The SAQ type | [optional] 
**scan_expiration_date_utc** | **datetime** | The date in UTC of the either the scan that makes the merchant fail compliance or the most soon to expire. | [optional] 
**scan_result** | **str** | Whether the scan passed or failed | [optional] 
**scan_target** | **str** | The scan target of the scan used for the expiration date and result. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

