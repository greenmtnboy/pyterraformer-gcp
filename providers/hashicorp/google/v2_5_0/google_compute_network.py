
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
        update: Optional[str] = None




class GoogleComputeNetwork(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_compute_network'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        auto_create_subnetworks: Optional[bool] = None,
        delete_default_routes_on_create: Optional[bool] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ipv4_range: Optional[str] = None,
        project: Optional[str] = None,
        routing_mode: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if auto_create_subnetworks is not None:
                kwargs['auto_create_subnetworks'] = auto_create_subnetworks
            if delete_default_routes_on_create is not None:
                kwargs['delete_default_routes_on_create'] = delete_default_routes_on_create
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ipv4_range is not None:
                kwargs['ipv4_range'] = ipv4_range
            if project is not None:
                kwargs['project'] = project
            if routing_mode is not None:
                kwargs['routing_mode'] = routing_mode
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
