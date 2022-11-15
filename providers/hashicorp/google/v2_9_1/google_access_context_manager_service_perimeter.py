
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class StatusItem():
        # non-optional-blocks
        access_levels: Optional[List[str]] = None
        resources: Optional[List[str]] = None
        restricted_services: Optional[List[str]] = None
        
# wrapper list class
class Status(BlockList):
        items: List[StatusItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAccessContextManagerServicePerimeter(ResourceObject):
    """    
    Args:
        name (str): 
        parent (str): 
        title (str): 
    """
    _type = 'google_access_context_manager_service_perimeter'
    
    def __init__(self,
        tf_id: str,
        name:str,
        parent:str,
        title:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        perimeter_type: Optional[str] = None,
        status: Optional[Status]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if parent is not None:
                kwargs['parent'] = parent
            if title is not None:
                kwargs['title'] = title
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if perimeter_type is not None:
                kwargs['perimeter_type'] = perimeter_type
            if status is not None:
                kwargs['status'] = status
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
