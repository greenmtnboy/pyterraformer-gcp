
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




class GoogleComputeGlobalNetworkEndpoint(ResourceObject):
    """    
    Args:
        global_network_endpoint_group (str): The global network endpoint group this endpoint is part of.
        port (float): Port number of the external endpoint.
    """
    _type = 'google_compute_global_network_endpoint'
    
    def __init__(self,
        tf_id: str,
        global_network_endpoint_group:str,
        port:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        fqdn: Optional[str] = None,
        id: Optional[str] = None,
        ip_address: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if global_network_endpoint_group is not None:
                kwargs['global_network_endpoint_group'] = global_network_endpoint_group
            if port is not None:
                kwargs['port'] = port
            if fqdn is not None:
                kwargs['fqdn'] = fqdn
            if id is not None:
                kwargs['id'] = id
            if ip_address is not None:
                kwargs['ip_address'] = ip_address
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
