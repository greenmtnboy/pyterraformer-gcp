
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionItem():
        expression:str
        title:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class Condition(BlockList):
        items: List[ConditionItem]




class GoogleAccessContextManagerAccessPolicyIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        name (str): 
        role (str): 
    """
    _type = 'google_access_context_manager_access_policy_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        name:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if name is not None:
                kwargs['name'] = name
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
