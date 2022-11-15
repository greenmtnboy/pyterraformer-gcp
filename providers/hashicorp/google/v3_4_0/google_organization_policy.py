
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AllowItem():
        # non-optional-blocks
        all: Optional[bool] = None
        values: Optional[Set[str]] = None
        
# wrapper list class
class Allow(BlockList):
        items: List[AllowItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DenyItem():
        # non-optional-blocks
        all: Optional[bool] = None
        values: Optional[Set[str]] = None
        
# wrapper list class
class Deny(BlockList):
        items: List[DenyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BooleanPolicyItem():
        enforced:bool
        # non-optional-blocks
        
# wrapper list class
class BooleanPolicy(BlockList):
        items: List[BooleanPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ListPolicyItem():
        # non-optional-blocks
        inherit_from_parent: Optional[bool] = None
        suggested_value: Optional[str] = None
        allow: Optional[Allow]=None,
        deny: Optional[Deny]=None,
        
# wrapper list class
class ListPolicy(BlockList):
        items: List[ListPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RestorePolicyItem():
        default:bool
        # non-optional-blocks
        
# wrapper list class
class RestorePolicy(BlockList):
        items: List[RestorePolicyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        read: Optional[str] = None
        update: Optional[str] = None




class GoogleOrganizationPolicy(ResourceObject):
    """    
    Args:
        constraint (str): 
        org_id (str): 
    """
    _type = 'google_organization_policy'
    
    def __init__(self,
        tf_id: str,
        constraint:str,
        org_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        version: Optional[float] = None,
        allow: Optional[Allow]=None,
        deny: Optional[Deny]=None,
        boolean_policy: Optional[BooleanPolicy]=None,
        list_policy: Optional[ListPolicy]=None,
        restore_policy: Optional[RestorePolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if constraint is not None:
                kwargs['constraint'] = constraint
            if org_id is not None:
                kwargs['org_id'] = org_id
            if id is not None:
                kwargs['id'] = id
            if version is not None:
                kwargs['version'] = version
            if allow is not None:
                kwargs['allow'] = allow
            if deny is not None:
                kwargs['deny'] = deny
            if boolean_policy is not None:
                kwargs['boolean_policy'] = boolean_policy
            if list_policy is not None:
                kwargs['list_policy'] = list_policy
            if restore_policy is not None:
                kwargs['restore_policy'] = restore_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
