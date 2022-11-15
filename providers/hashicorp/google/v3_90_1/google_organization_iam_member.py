
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




class GoogleOrganizationIamMember(ResourceObject):
    """    
    Args:
        member (str): 
        org_id (str): The numeric ID of the organization in which you want to manage the audit logging config.
        role (str): 
    """
    _type = 'google_organization_iam_member'
    
    def __init__(self,
        tf_id: str,
        member:str,
        org_id:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if member is not None:
                kwargs['member'] = member
            if org_id is not None:
                kwargs['org_id'] = org_id
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
