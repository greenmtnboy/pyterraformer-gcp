
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class OsConstraintsItem():
        os_type:str
        # non-optional-blocks
        minimum_version: Optional[str] = None
        
# wrapper list class
class OsConstraints(BlockList):
        items: List[OsConstraintsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DevicePolicyItem():
        # non-optional-blocks
        allowed_device_management_levels: Optional[List[str]] = None
        allowed_encryption_statuses: Optional[List[str]] = None
        require_admin_approval: Optional[bool] = None
        require_corp_owned: Optional[bool] = None
        require_screen_lock: Optional[bool] = None
        os_constraints: Optional[OsConstraints]=None,
        
# wrapper list class
class DevicePolicy(BlockList):
        items: List[DevicePolicyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleAccessContextManagerAccessLevelCondition(ResourceObject):
    """    
    Args:
        access_level (str): The name of the Access Level to add this condition to.
    """
    _type = 'google_access_context_manager_access_level_condition'
    
    def __init__(self,
        tf_id: str,
        access_level:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ip_subnetworks: Optional[List[str]] = None,
        members: Optional[List[str]] = None,
        negate: Optional[bool] = None,
        regions: Optional[List[str]] = None,
        required_access_levels: Optional[List[str]] = None,
        os_constraints: Optional[OsConstraints]=None,
        device_policy: Optional[DevicePolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if access_level is not None:
                kwargs['access_level'] = access_level
            if id is not None:
                kwargs['id'] = id
            if ip_subnetworks is not None:
                kwargs['ip_subnetworks'] = ip_subnetworks
            if members is not None:
                kwargs['members'] = members
            if negate is not None:
                kwargs['negate'] = negate
            if regions is not None:
                kwargs['regions'] = regions
            if required_access_levels is not None:
                kwargs['required_access_levels'] = required_access_levels
            if os_constraints is not None:
                kwargs['os_constraints'] = os_constraints
            if device_policy is not None:
                kwargs['device_policy'] = device_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
