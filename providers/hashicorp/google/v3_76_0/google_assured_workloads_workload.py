
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
        billing_account (str): 
        compliance_regime (str): 
        display_name (str): 
        location (str): 
        organization (str): 
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
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
