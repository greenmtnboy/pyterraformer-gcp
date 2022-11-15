
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




# this block can contain multiple items, items in a list are required
@dataclass 
class BgpItem():
        asn:float
        # non-optional-blocks
        advertise_mode: Optional[str] = None
        advertised_groups: Optional[List[str]] = None
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
        name (str): 
        network (str): 
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
            
        
        
