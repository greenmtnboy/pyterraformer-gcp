
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class KmsSettingsItem():
        next_rotation_time:str
        rotation_period:str
        # non-optional-blocks
        
# wrapper list class
class KmsSettings(BlockList):
        items: List[KmsSettingsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourceSettingsItem():
        # non-optional-blocks
        resource_id: Optional[str] = None
        resource_type: Optional[str] = None
        
# wrapper list class
class ResourceSettings(BlockList):
        items: List[ResourceSettingsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAssuredWorkloadsWorkload(ResourceObject):
    """    
    Args:
        billing_account (str): Required. Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, 'billingAccounts/012345-567890-ABCDEF`.
        compliance_regime (str): Required. Immutable. Compliance Regime associated with this workload. Possible values: COMPLIANCE_REGIME_UNSPECIFIED, IL4, CJIS, FEDRAMP_HIGH, FEDRAMP_MODERATE, US_REGIONAL_ACCESS
        display_name (str): Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        location (str): The location for the resource
        organization (str): The organization for the resource
    """
    _type = 'google_assured_workloads_workload'
    
    def __init__(self,
        tf_id: str,
        billing_account:str,
        compliance_regime:str,
        display_name:str,
        location:str,
        organization:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        provisioned_resources_parent: Optional[str] = None,
        kms_settings: Optional[KmsSettings]=None,
        resource_settings: Optional[ResourceSettings]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if billing_account is not None:
                kwargs['billing_account'] = billing_account
            if compliance_regime is not None:
                kwargs['compliance_regime'] = compliance_regime
            if display_name is not None:
                kwargs['display_name'] = display_name
            if location is not None:
                kwargs['location'] = location
            if organization is not None:
                kwargs['organization'] = organization
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if provisioned_resources_parent is not None:
                kwargs['provisioned_resources_parent'] = provisioned_resources_parent
            if kms_settings is not None:
                kwargs['kms_settings'] = kms_settings
            if resource_settings is not None:
                kwargs['resource_settings'] = resource_settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
