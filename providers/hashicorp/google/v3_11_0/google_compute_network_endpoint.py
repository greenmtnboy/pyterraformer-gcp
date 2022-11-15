
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




class GoogleComputeNetworkEndpoint(ResourceObject):
    """    
    Args:
        instance (str): The name for a specific VM instance that the IP address belongs to.
                    This is required for network endpoints of type GCE_VM_IP_PORT.
                    The instance must be in the same zone of network endpoint group.
        ip_address (str): IPv4 address of network endpoint. The IP address must belong
                    to a VM in GCE (either the primary IP or as part of an aliased IP
                    range).
        network_endpoint_group (str): The network endpoint group this endpoint is part of.
        port (float): Port number of network endpoint.
    """
    _type = 'google_compute_network_endpoint'
    
    def __init__(self,
        tf_id: str,
        instance:str,
        ip_address:str,
        network_endpoint_group:str,
        port:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if instance is not None:
                kwargs['instance'] = instance
            if ip_address is not None:
                kwargs['ip_address'] = ip_address
            if network_endpoint_group is not None:
                kwargs['network_endpoint_group'] = network_endpoint_group
            if port is not None:
                kwargs['port'] = port
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
