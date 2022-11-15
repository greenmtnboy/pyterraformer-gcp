
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeRouterInterface(ResourceObject):
    """    
    Args:
        name (str): 
        router (str): 
        vpn_tunnel (str): 
    """
    _type = 'google_compute_router_interface'
    
    def __init__(self,
        tf_id: str,
        name:str,
        router:str,
        vpn_tunnel:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ip_range: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if router is not None:
                kwargs['router'] = router
            if vpn_tunnel is not None:
                kwargs['vpn_tunnel'] = vpn_tunnel
            if id is not None:
                kwargs['id'] = id
            if ip_range is not None:
                kwargs['ip_range'] = ip_range
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
