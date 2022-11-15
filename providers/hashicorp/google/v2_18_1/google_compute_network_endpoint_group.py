
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




class GoogleComputeNetworkEndpointGroup(ResourceObject):
    """    
    Args:
        name (str): 
        network (str): 
    """
    _type = 'google_compute_network_endpoint_group'
    
    def __init__(self,
        tf_id: str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        default_port: Optional[float] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        network_endpoint_type: Optional[str] = None,
        project: Optional[str] = None,
        subnetwork: Optional[str] = None,
        zone: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if default_port is not None:
                kwargs['default_port'] = default_port
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if network_endpoint_type is not None:
                kwargs['network_endpoint_type'] = network_endpoint_type
            if project is not None:
                kwargs['project'] = project
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if zone is not None:
                kwargs['zone'] = zone
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
