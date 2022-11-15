
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAccessContextManagerAccessPolicy(ResourceObject):
    """    
    Args:
        parent (str): The parent of this AccessPolicy in the Cloud Resource Hierarchy.
                    Format: organizations/{organization_id}
        title (str): Human readable title. Does not affect behavior.
    """
    _type = 'google_access_context_manager_access_policy'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        title:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if title is not None:
                kwargs['title'] = title
            if id is not None:
                kwargs['id'] = id
            if scopes is not None:
                kwargs['scopes'] = scopes
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
