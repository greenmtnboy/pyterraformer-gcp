
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ExprItem():
        expression:str
        # non-optional-blocks
        description: Optional[str] = None
        location: Optional[str] = None
        title: Optional[str] = None
        
# wrapper list class
class Expr(BlockList):
        items: List[ExprItem]




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




# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionsItem():
        # non-optional-blocks
        ip_subnetworks: Optional[List[str]] = None
        members: Optional[List[str]] = None
        negate: Optional[bool] = None
        regions: Optional[List[str]] = None
        required_access_levels: Optional[List[str]] = None
        os_constraints: Optional[OsConstraints]=None,
        device_policy: Optional[DevicePolicy]=None,
        
# wrapper list class
class Conditions(BlockList):
        items: List[ConditionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BasicItem():
        # non-optional-blocks
        combining_function: Optional[str] = None
        os_constraints: Optional[OsConstraints]=None,
        device_policy: Optional[DevicePolicy]=None,
        conditions: Optional[Conditions]=None,
        
# wrapper list class
class Basic(BlockList):
        items: List[BasicItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CustomItem():
        # non-optional-blocks
        expr: Optional[Expr]=None,
        
# wrapper list class
class Custom(BlockList):
        items: List[CustomItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class AccessLevelsItem():
        name:str
        title:str
        # non-optional-blocks
        description: Optional[str] = None
        expr: Optional[Expr]=None,
        os_constraints: Optional[OsConstraints]=None,
        device_policy: Optional[DevicePolicy]=None,
        conditions: Optional[Conditions]=None,
        basic: Optional[Basic]=None,
        custom: Optional[Custom]=None,
        
# wrapper list class
class AccessLevels(BlockSet):
        items: Set[AccessLevelsItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAccessContextManagerAccessLevels(ResourceObject):
    """    
    Args:
        parent (str): The AccessPolicy this AccessLevel lives in.
                    Format: accessPolicies/{policy_id}
    """
    _type = 'google_access_context_manager_access_levels'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        expr: Optional[Expr]=None,
        os_constraints: Optional[OsConstraints]=None,
        device_policy: Optional[DevicePolicy]=None,
        conditions: Optional[Conditions]=None,
        basic: Optional[Basic]=None,
        custom: Optional[Custom]=None,
        access_levels: Optional[AccessLevels]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if id is not None:
                kwargs['id'] = id
            if expr is not None:
                kwargs['expr'] = expr
            if os_constraints is not None:
                kwargs['os_constraints'] = os_constraints
            if device_policy is not None:
                kwargs['device_policy'] = device_policy
            if conditions is not None:
                kwargs['conditions'] = conditions
            if basic is not None:
                kwargs['basic'] = basic
            if custom is not None:
                kwargs['custom'] = custom
            if access_levels is not None:
                kwargs['access_levels'] = access_levels
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
