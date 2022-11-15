
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




class GoogleVpcAccessConnector(ResourceObject):
    """    
    Args:
        ip_cidr_range (str): The range of internal addresses that follows RFC 4632 notation. Example: '10.132.0.0/28'.
        name (str): The name of the resource (Max 25 characters).
        network (str): Name of a VPC network.
        region (str): Region where the VPC Access connector resides
    """
    _type = 'google_vpc_access_connector'
    
    def __init__(self,
        tf_id: str,
        ip_cidr_range:str,
        name:str,
        network:str,
        region:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        max_throughput: Optional[float] = None,
        min_throughput: Optional[float] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if ip_cidr_range is not None:
                kwargs['ip_cidr_range'] = ip_cidr_range
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if region is not None:
                kwargs['region'] = region
            if id is not None:
                kwargs['id'] = id
            if max_throughput is not None:
                kwargs['max_throughput'] = max_throughput
            if min_throughput is not None:
                kwargs['min_throughput'] = min_throughput
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
