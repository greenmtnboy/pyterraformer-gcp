
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeProjectMetadata(ResourceObject):
    """    
    Args:
        metadata (Dict[str, str]): 
    """
    _type = 'google_compute_project_metadata'
    
    def __init__(self,
        tf_id: str,
        metadata:Dict[str, str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if metadata is not None:
                kwargs['metadata'] = metadata
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
