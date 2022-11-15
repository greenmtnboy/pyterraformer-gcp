
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AdvertisedIpRangesItem():
        range:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class AdvertisedIpRanges(BlockList):
        items: List[AdvertisedIpRangesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BfdItem():
        session_initialization_mode:str
        # non-optional-blocks
        min_receive_interval: Optional[float] = None
        min_transmit_interval: Optional[float] = None
        multiplier: Optional[float] = None
        
# wrapper list class
class Bfd(BlockList):
        items: List[BfdItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRouterPeer(ResourceObject):
    """    
    Args:
        interface (str): Name of the interface the BGP peer is associated with.
        name (str): Name of this BGP peer. The name must be 1-63 characters long,
                    and comply with RFC1035. Specifically, the name must be 1-63 characters
                    long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which
                    means the first character must be a lowercase letter, and all
                    following characters must be a dash, lowercase letter, or digit,
                    except the last character, which cannot be a dash.
        peer_asn (float): Peer BGP Autonomous System Number (ASN).
                    Each BGP interface may use a different value.
        peer_ip_address (str): IP address of the BGP interface outside Google Cloud Platform.
                    Only IPv4 is supported.
        router (str): The name of the Cloud Router in which this BgpPeer will be configured.
    """
    _type = 'google_compute_router_peer'
    
    def __init__(self,
        tf_id: str,
        interface:str,
        name:str,
        peer_asn:float,
        peer_ip_address:str,
        router:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        advertise_mode: Optional[str] = None,
        advertised_groups: Optional[List[str]] = None,
        advertised_route_priority: Optional[float] = None,
        enable: Optional[bool] = None,
        id: Optional[str] = None,
        ip_address: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        advertised_ip_ranges: Optional[AdvertisedIpRanges]=None,
        bfd: Optional[Bfd]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if interface is not None:
                kwargs['interface'] = interface
            if name is not None:
                kwargs['name'] = name
            if peer_asn is not None:
                kwargs['peer_asn'] = peer_asn
            if peer_ip_address is not None:
                kwargs['peer_ip_address'] = peer_ip_address
            if router is not None:
                kwargs['router'] = router
            if advertise_mode is not None:
                kwargs['advertise_mode'] = advertise_mode
            if advertised_groups is not None:
                kwargs['advertised_groups'] = advertised_groups
            if advertised_route_priority is not None:
                kwargs['advertised_route_priority'] = advertised_route_priority
            if enable is not None:
                kwargs['enable'] = enable
            if id is not None:
                kwargs['id'] = id
            if ip_address is not None:
                kwargs['ip_address'] = ip_address
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if advertised_ip_ranges is not None:
                kwargs['advertised_ip_ranges'] = advertised_ip_ranges
            if bfd is not None:
                kwargs['bfd'] = bfd
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
