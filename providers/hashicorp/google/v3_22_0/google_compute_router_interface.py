
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




class GoogleComputeRouterInterface(ResourceObject):
    """    
    Args:
        name (str): 
        router (str): 
    """
    _type = 'google_compute_router_interface'
    
    def __init__(self,
        tf_id: str,
        name:str,
        router:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        interconnect_attachment: Optional[str] = None,
        ip_range: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        vpn_tunnel: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if router is not None:
                kwargs['router'] = router
            if id is not None:
                kwargs['id'] = id
            if interconnect_attachment is not None:
                kwargs['interconnect_attachment'] = interconnect_attachment
            if ip_range is not None:
                kwargs['ip_range'] = ip_range
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if vpn_tunnel is not None:
                kwargs['vpn_tunnel'] = vpn_tunnel
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
