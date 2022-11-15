
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleServiceNetworkingConnection(ResourceObject):
    """    
    Args:
        network (str): 
        reserved_peering_ranges (List[str]): 
        service (str): 
    """
    _type = 'google_service_networking_connection'
    
    def __init__(self,
        tf_id: str,
        network:str,
        reserved_peering_ranges:List[str],
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if network is not None:
                kwargs['network'] = network
            if reserved_peering_ranges is not None:
                kwargs['reserved_peering_ranges'] = reserved_peering_ranges
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
