
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworksItem():
        # non-optional-blocks
        network_url: Optional[str] = None
        
# wrapper list class
class Networks(BlockSet):
        items: Set[NetworksItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class PrivateVisibilityConfigItem():
        # non-optional-blocks
        networks: Optional[Networks]=None,
        
# wrapper list class
class PrivateVisibilityConfig(BlockList):
        items: List[PrivateVisibilityConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDnsManagedZone(ResourceObject):
    """    
    Args:
        dns_name (str): 
        name (str): 
    """
    _type = 'google_dns_managed_zone'
    
    def __init__(self,
        tf_id: str,
        dns_name:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        visibility: Optional[str] = None,
        networks: Optional[Networks]=None,
        private_visibility_config: Optional[PrivateVisibilityConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dns_name is not None:
                kwargs['dns_name'] = dns_name
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if visibility is not None:
                kwargs['visibility'] = visibility
            if networks is not None:
                kwargs['networks'] = networks
            if private_visibility_config is not None:
                kwargs['private_visibility_config'] = private_visibility_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
