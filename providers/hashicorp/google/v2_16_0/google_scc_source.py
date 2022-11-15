
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




class GoogleSccSource(ResourceObject):
    """    
    Args:
        display_name (str): 
        organization (str): 
    """
    _type = 'google_scc_source'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        organization:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if organization is not None:
                kwargs['organization'] = organization
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
