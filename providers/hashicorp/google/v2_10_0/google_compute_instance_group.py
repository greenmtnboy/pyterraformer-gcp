
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NamedPortItem():
        name:str
        port:float
        # non-optional-blocks
        
# wrapper list class
class NamedPort(BlockList):
        items: List[NamedPortItem]




class GoogleComputeInstanceGroup(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_compute_instance_group'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        instances: Optional[Set[str]] = None,
        network: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        named_port: Optional[NamedPort]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if instances is not None:
                kwargs['instances'] = instances
            if network is not None:
                kwargs['network'] = network
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            if named_port is not None:
                kwargs['named_port'] = named_port
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
