
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




class GoogleComputeInstanceGroupNamedPort(ResourceObject):
    """    
    Args:
        group (str): The name of the instance group.
        name (str): The name for this named port. The name must be 1-63 characters
                    long, and comply with RFC1035.
        port (float): The port number, which can be a value between 1 and 65535.
    """
    _type = 'google_compute_instance_group_named_port'
    
    def __init__(self,
        tf_id: str,
        group:str,
        name:str,
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
            if group is not None:
                kwargs['group'] = group
            if name is not None:
                kwargs['name'] = name
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
            
        
        
