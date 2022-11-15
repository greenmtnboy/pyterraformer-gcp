
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




class GoogleTagsTagKeyIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        role (str): 
        tag_key (str): 
    """
    _type = 'google_tags_tag_key_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        role:str,
        tag_key:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if tag_key is not None:
                kwargs['tag_key'] = tag_key
            if id is not None:
                kwargs['id'] = id
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
