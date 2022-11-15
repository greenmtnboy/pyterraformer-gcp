
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AdvertisedIpRangesItem():
        # non-optional-blocks
        description: Optional[str] = None
        range: Optional[str] = None
        
# wrapper list class
class AdvertisedIpRanges(BlockList):
        items: List[AdvertisedIpRangesItem]




class GoogleComputeRouterPeer(ResourceObject):
    """    
    Args:
        interface (str): 
        name (str): 
        peer_asn (float): 
        router (str): 
    """
    _type = 'google_compute_router_peer'
    
    def __init__(self,
        tf_id: str,
        interface:str,
        name:str,
        peer_asn:float,
        router:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        advertise_mode: Optional[str] = None,
        advertised_groups: Optional[List[str]] = None,
        advertised_route_priority: Optional[float] = None,
        id: Optional[str] = None,
        peer_ip_address: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        advertised_ip_ranges: Optional[AdvertisedIpRanges]=None,
        ):
            kwargs = {}
            if interface is not None:
                kwargs['interface'] = interface
            if name is not None:
                kwargs['name'] = name
            if peer_asn is not None:
                kwargs['peer_asn'] = peer_asn
            if router is not None:
                kwargs['router'] = router
            if advertise_mode is not None:
                kwargs['advertise_mode'] = advertise_mode
            if advertised_groups is not None:
                kwargs['advertised_groups'] = advertised_groups
            if advertised_route_priority is not None:
                kwargs['advertised_route_priority'] = advertised_route_priority
            if id is not None:
                kwargs['id'] = id
            if peer_ip_address is not None:
                kwargs['peer_ip_address'] = peer_ip_address
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if advertised_ip_ranges is not None:
                kwargs['advertised_ip_ranges'] = advertised_ip_ranges
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
