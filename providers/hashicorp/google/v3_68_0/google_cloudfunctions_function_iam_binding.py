
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




class GoogleCloudfunctionsFunctionIamBinding(ResourceObject):
    """    
    Args:
        cloud_function (str): 
        members (Set[str]): 
        role (str): 
    """
    _type = 'google_cloudfunctions_function_iam_binding'
    
    def __init__(self,
        tf_id: str,
        cloud_function:str,
        members:Set[str],
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if cloud_function is not None:
                kwargs['cloud_function'] = cloud_function
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        