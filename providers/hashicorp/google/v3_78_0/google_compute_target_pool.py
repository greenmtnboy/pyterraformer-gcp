
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




class GoogleComputeTargetPool(ResourceObject):
    """    
    Args:
        name (str): A unique name for the resource, required by GCE. Changing this forces a new resource to be created.
    """
    _type = 'google_compute_target_pool'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        backup_pool: Optional[str] = None,
        description: Optional[str] = None,
        failover_ratio: Optional[float] = None,
        health_checks: Optional[List[str]] = None,
        id: Optional[str] = None,
        instances: Optional[Set[str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        session_affinity: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if backup_pool is not None:
                kwargs['backup_pool'] = backup_pool
            if description is not None:
                kwargs['description'] = description
            if failover_ratio is not None:
                kwargs['failover_ratio'] = failover_ratio
            if health_checks is not None:
                kwargs['health_checks'] = health_checks
            if id is not None:
                kwargs['id'] = id
            if instances is not None:
                kwargs['instances'] = instances
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if session_affinity is not None:
                kwargs['session_affinity'] = session_affinity
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
