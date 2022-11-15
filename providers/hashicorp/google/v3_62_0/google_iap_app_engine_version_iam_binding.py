
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




class GoogleIapAppEngineVersionIamBinding(ResourceObject):
    """    
    Args:
        app_id (str): 
        members (Set[str]): 
        role (str): 
        service (str): 
        version_id (str): 
    """
    _type = 'google_iap_app_engine_version_iam_binding'
    
    def __init__(self,
        tf_id: str,
        app_id:str,
        members:Set[str],
        role:str,
        service:str,
        version_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if app_id is not None:
                kwargs['app_id'] = app_id
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if service is not None:
                kwargs['service'] = service
            if version_id is not None:
                kwargs['version_id'] = version_id
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
