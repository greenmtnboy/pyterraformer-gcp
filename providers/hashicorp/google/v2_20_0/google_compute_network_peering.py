
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeNetworkPeering(ResourceObject):
    """    
    Args:
        name (str): 
        network (str): 
        peer_network (str): 
    """
    _type = 'google_compute_network_peering'
    
    def __init__(self,
        tf_id: str,
        name:str,
        network:str,
        peer_network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        auto_create_routes: Optional[bool] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if peer_network is not None:
                kwargs['peer_network'] = peer_network
            if auto_create_routes is not None:
                kwargs['auto_create_routes'] = auto_create_routes
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
