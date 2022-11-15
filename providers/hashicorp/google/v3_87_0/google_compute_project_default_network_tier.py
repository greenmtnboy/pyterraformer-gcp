
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




class GoogleComputeProjectDefaultNetworkTier(ResourceObject):
    """    
    Args:
        network_tier (str): The default network tier to be configured for the project. This field can take the following values: PREMIUM or STANDARD.
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
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if network_tier is not None:
                kwargs['network_tier'] = network_tier
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
