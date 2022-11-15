
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeProjectDefaultNetworkTier(ResourceObject):
    """    
    Args:
        network_tier (str): 
    """
    _type = 'google_compute_project_default_network_tier'
    
    def __init__(self,
        tf_id: str,
        network_tier:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if network_tier is not None:
                kwargs['network_tier'] = network_tier
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
