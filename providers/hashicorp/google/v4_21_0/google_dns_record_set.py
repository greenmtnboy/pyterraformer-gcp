
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GeoItem():
        location:str
        rrdatas:List[str]
        # non-optional-blocks
        
# wrapper list class
class Geo(BlockList):
        items: List[GeoItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WrrItem():
        rrdatas:List[str]
        weight:float
        # non-optional-blocks
        
# wrapper list class
class Wrr(BlockList):
        items: List[WrrItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RoutingPolicyItem():
        # non-optional-blocks
        geo: Optional[Geo]=None,
        wrr: Optional[Wrr]=None,
        
# wrapper list class
class RoutingPolicy(BlockList):
        items: List[RoutingPolicyItem]




class GoogleDnsRecordSet(ResourceObject):
    """    
    Args:
        managed_zone (str): The name of the zone in which this record set will reside.
        name (str): The DNS name this record set will apply to.
        type (str): The DNS record set type.
    """
    _type = 'google_dns_record_set'
    
    def __init__(self,
        tf_id: str,
        managed_zone:str,
        name:str,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        rrdatas: Optional[List[str]] = None,
        ttl: Optional[float] = None,
        geo: Optional[Geo]=None,
        wrr: Optional[Wrr]=None,
        routing_policy: Optional[RoutingPolicy]=None,
        ):
            kwargs = {}
            if managed_zone is not None:
                kwargs['managed_zone'] = managed_zone
            if name is not None:
                kwargs['name'] = name
            if type is not None:
                kwargs['type'] = type
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if rrdatas is not None:
                kwargs['rrdatas'] = rrdatas
            if ttl is not None:
                kwargs['ttl'] = ttl
            if geo is not None:
                kwargs['geo'] = geo
            if wrr is not None:
                kwargs['wrr'] = wrr
            if routing_policy is not None:
                kwargs['routing_policy'] = routing_policy
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
