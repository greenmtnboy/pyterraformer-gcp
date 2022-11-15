
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




class GoogleComputeNetworkPeering(ResourceObject):
    """    
    Args:
        name (str): Name of the peering.
        network (str): The primary network of the peering.
        peer_network (str): The peer network in the peering. The peer network may belong to a different project.
    """
    _type = 'google_compute_network_peering'
    
    def __init__(self,
        tf_id: str,
        name:str,
        network:str,
        peer_network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        auto_create_routes: Optional[bool] = None,
        export_custom_routes: Optional[bool] = None,
        export_subnet_routes_with_public_ip: Optional[bool] = None,
        id: Optional[str] = None,
        import_custom_routes: Optional[bool] = None,
        import_subnet_routes_with_public_ip: Optional[bool] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if peer_network is not None:
                kwargs['peer_network'] = peer_network
            if auto_create_routes is not None:
                kwargs['auto_create_routes'] = auto_create_routes
            if export_custom_routes is not None:
                kwargs['export_custom_routes'] = export_custom_routes
            if export_subnet_routes_with_public_ip is not None:
                kwargs['export_subnet_routes_with_public_ip'] = export_subnet_routes_with_public_ip
            if id is not None:
                kwargs['id'] = id
            if import_custom_routes is not None:
                kwargs['import_custom_routes'] = import_custom_routes
            if import_subnet_routes_with_public_ip is not None:
                kwargs['import_subnet_routes_with_public_ip'] = import_subnet_routes_with_public_ip
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
