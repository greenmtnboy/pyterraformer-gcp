
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




class GoogleComputeNetworkPeeringRoutesConfig(ResourceObject):
    """    
    Args:
        export_custom_routes (bool): Whether to export the custom routes to the peer network.
        import_custom_routes (bool): Whether to import the custom routes to the peer network.
        network (str): The name of the primary network for the peering.
        peering (str): Name of the peering.
    """
    _type = 'google_compute_network_peering_routes_config'
    
    def __init__(self,
        tf_id: str,
        export_custom_routes:bool,
        import_custom_routes:bool,
        network:str,
        peering:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if export_custom_routes is not None:
                kwargs['export_custom_routes'] = export_custom_routes
            if import_custom_routes is not None:
                kwargs['import_custom_routes'] = import_custom_routes
            if network is not None:
                kwargs['network'] = network
            if peering is not None:
                kwargs['peering'] = peering
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
