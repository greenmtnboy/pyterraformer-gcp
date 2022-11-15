
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




class GoogleComputeTargetInstance(ResourceObject):
    """    
    Args:
        instance (str): The Compute instance VM handling traffic for this target instance.
                    Accepts the instance self-link, relative path
                    (e.g. 'projects/project/zones/zone/instances/instance') or name. If
                    name is given, the zone will default to the given zone or
                    the provider-default zone and the project will default to the
                    provider-level project.
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
    """
    _type = 'google_compute_target_instance'
    
    def __init__(self,
        tf_id: str,
        instance:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        nat_policy: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if instance is not None:
                kwargs['instance'] = instance
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if nat_policy is not None:
                kwargs['nat_policy'] = nat_policy
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
