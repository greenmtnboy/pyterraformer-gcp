
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




class GoogleSecretManagerSecretIamMember(ResourceObject):
    """    
    Args:
        member (str): 
        role (str): 
        secret_id (str): 
    """
    _type = 'google_secret_manager_secret_iam_member'
    
    def __init__(self,
        tf_id: str,
        member:str,
        role:str,
        secret_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if secret_id is not None:
                kwargs['secret_id'] = secret_id
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
