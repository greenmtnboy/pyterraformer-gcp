
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




class GoogleComputeRoute(ResourceObject):
    """    
    Args:
        dest_range (str): 
        name (str): 
        network (str): 
    """
    _type = 'google_compute_route'
    
    def __init__(self,
        tf_id: str,
        dest_range:str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        next_hop_gateway: Optional[str] = None,
        next_hop_instance: Optional[str] = None,
        next_hop_instance_zone: Optional[str] = None,
        next_hop_ip: Optional[str] = None,
        next_hop_vpn_tunnel: Optional[str] = None,
        priority: Optional[float] = None,
        project: Optional[str] = None,
        tags: Optional[Set[str]] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dest_range is not None:
                kwargs['dest_range'] = dest_range
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if next_hop_gateway is not None:
                kwargs['next_hop_gateway'] = next_hop_gateway
            if next_hop_instance is not None:
                kwargs['next_hop_instance'] = next_hop_instance
            if next_hop_instance_zone is not None:
                kwargs['next_hop_instance_zone'] = next_hop_instance_zone
            if next_hop_ip is not None:
                kwargs['next_hop_ip'] = next_hop_ip
            if next_hop_vpn_tunnel is not None:
                kwargs['next_hop_vpn_tunnel'] = next_hop_vpn_tunnel
            if priority is not None:
                kwargs['priority'] = priority
            if project is not None:
                kwargs['project'] = project
            if tags is not None:
                kwargs['tags'] = tags
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
