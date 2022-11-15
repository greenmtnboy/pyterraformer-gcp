
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
        name (str): The name of the resource (Max 25 characters).
    """
    _type = 'google_vpc_access_connector'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ip_cidr_range: Optional[str] = None,
        max_throughput: Optional[float] = None,
        min_throughput: Optional[float] = None,
        network: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if ip_cidr_range is not None:
                kwargs['ip_cidr_range'] = ip_cidr_range
            if max_throughput is not None:
                kwargs['max_throughput'] = max_throughput
            if min_throughput is not None:
                kwargs['min_throughput'] = min_throughput
            if network is not None:
                kwargs['network'] = network
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
