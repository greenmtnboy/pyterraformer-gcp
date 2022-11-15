
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleFolder(ResourceObject):
    """    
    Args:
        display_name (str): 
        parent (str): 
    """
    _type = 'google_folder'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if parent is not None:
                kwargs['parent'] = parent
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
