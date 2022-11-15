
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




class GoogleNotebooksInstanceIamBinding(ResourceObject):
    """    
    Args:
        instance_name (str): 
        members (Set[str]): 
        role (str): 
    """
    _type = 'google_notebooks_instance_iam_binding'
    
    def __init__(self,
        tf_id: str,
        instance_name:str,
        members:Set[str],
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if instance_name is not None:
                kwargs['instance_name'] = instance_name
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
