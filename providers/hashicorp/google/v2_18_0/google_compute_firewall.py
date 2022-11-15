
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class AllowItem():
        protocol:str
        # non-optional-blocks
        ports: Optional[List[str]] = None
        
# wrapper list class
class Allow(BlockSet):
        items: Set[AllowItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DenyItem():
        protocol:str
        # non-optional-blocks
        ports: Optional[List[str]] = None
        
# wrapper list class
class Deny(BlockSet):
        items: Set[DenyItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeFirewall(ResourceObject):
    """    
    Args:
        name (str): 
        network (str): 
    """
    _type = 'google_compute_firewall'
    
    def __init__(self,
        tf_id: str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        destination_ranges: Optional[Set[str]] = None,
        direction: Optional[str] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        priority: Optional[float] = None,
        project: Optional[str] = None,
        source_ranges: Optional[Set[str]] = None,
        source_service_accounts: Optional[Set[str]] = None,
        source_tags: Optional[Set[str]] = None,
        target_service_accounts: Optional[Set[str]] = None,
        target_tags: Optional[Set[str]] = None,
        allow: Optional[Allow]=None,
        deny: Optional[Deny]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if description is not None:
                kwargs['description'] = description
            if destination_ranges is not None:
                kwargs['destination_ranges'] = destination_ranges
            if direction is not None:
                kwargs['direction'] = direction
            if disabled is not None:
                kwargs['disabled'] = disabled
            if id is not None:
                kwargs['id'] = id
            if priority is not None:
                kwargs['priority'] = priority
            if project is not None:
                kwargs['project'] = project
            if source_ranges is not None:
                kwargs['source_ranges'] = source_ranges
            if source_service_accounts is not None:
                kwargs['source_service_accounts'] = source_service_accounts
            if source_tags is not None:
                kwargs['source_tags'] = source_tags
            if target_service_accounts is not None:
                kwargs['target_service_accounts'] = target_service_accounts
            if target_tags is not None:
                kwargs['target_tags'] = target_tags
            if allow is not None:
                kwargs['allow'] = allow
            if deny is not None:
                kwargs['deny'] = deny
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
