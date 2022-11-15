
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
        export_custom_routes: Optional[bool] = None,
        id: Optional[str] = None,
        import_custom_routes: Optional[bool] = None,
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
            if export_custom_routes is not None:
                kwargs['export_custom_routes'] = export_custom_routes
            if id is not None:
                kwargs['id'] = id
            if import_custom_routes is not None:
                kwargs['import_custom_routes'] = import_custom_routes
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
