
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




class GoogleAppEngineFirewallRule(ResourceObject):
    """    
    Args:
        action (str): The action to take if this rule matches. Possible values: ["UNSPECIFIED_ACTION", "ALLOW", "DENY"]
        source_range (str): IP address or range, defined using CIDR notation, of requests that this rule applies to.
    """
    _type = 'google_app_engine_firewall_rule'
    
    def __init__(self,
        tf_id: str,
        action:str,
        source_range:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        priority: Optional[float] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if action is not None:
                kwargs['action'] = action
            if source_range is not None:
                kwargs['source_range'] = source_range
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if priority is not None:
                kwargs['priority'] = priority
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
