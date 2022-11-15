
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkSettingsItem():
        # non-optional-blocks
        ingress_traffic_allowed: Optional[str] = None
        
# wrapper list class
class NetworkSettings(BlockList):
        items: List[NetworkSettingsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAppEngineServiceNetworkSettings(ResourceObject):
    """    
    Args:
        service (str): The name of the service these settings apply to.
    """
    _type = 'google_app_engine_service_network_settings'
    
    def __init__(self,
        tf_id: str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        network_settings: Optional[NetworkSettings]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if network_settings is not None:
                kwargs['network_settings'] = network_settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
