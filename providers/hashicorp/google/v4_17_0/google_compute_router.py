
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
class BgpItem():
        asn:float
        # non-optional-blocks
        advertise_mode: Optional[str] = None
        advertised_groups: Optional[List[str]] = None
        keepalive_interval: Optional[float] = None
        advertised_ip_ranges: Optional[AdvertisedIpRanges]=None,
        
# wrapper list class
class Bgp(BlockList):
        items: List[BgpItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRouter(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. The name must be 1-63 characters long, and
                    comply with RFC1035. Specifically, the name must be 1-63 characters
                    long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?'
                    which means the first character must be a lowercase letter, and all
                    following characters must be a dash, lowercase letter, or digit,
                    except the last character, which cannot be a dash.
        network (str): A reference to the network to which this router belongs.
    """
    _type = 'google_compute_router'
    
    def __init__(self,
        tf_id: str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        encrypted_interconnect_router: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        advertised_ip_ranges: Optional[AdvertisedIpRanges]=None,
        bgp: Optional[Bgp]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if description is not None:
                kwargs['description'] = description
            if encrypted_interconnect_router is not None:
                kwargs['encrypted_interconnect_router'] = encrypted_interconnect_router
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if advertised_ip_ranges is not None:
                kwargs['advertised_ip_ranges'] = advertised_ip_ranges
            if bgp is not None:
                kwargs['bgp'] = bgp
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
