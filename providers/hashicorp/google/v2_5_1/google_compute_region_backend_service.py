
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class BackendItem():
        # non-optional-blocks
        description: Optional[str] = None
        group: Optional[str] = None
        
# wrapper list class
class Backend(BlockSet):
        items: Set[BackendItem]



class GoogleComputeRegionBackendService(ResourceObject):
    """    
    Args:
        health_checks (Set[str]): 
        name (str): 
    """
    _type = 'google_compute_region_backend_service'
    
    def __init__(self,
        tf_id: str,
        health_checks:Set[str],
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        connection_draining_timeout_sec: Optional[float] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        protocol: Optional[str] = None,
        region: Optional[str] = None,
        session_affinity: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        backend: Optional[Backend]=None,
        ):
            kwargs = {}
            if health_checks is not None:
                kwargs['health_checks'] = health_checks
            if name is not None:
                kwargs['name'] = name
            if connection_draining_timeout_sec is not None:
                kwargs['connection_draining_timeout_sec'] = connection_draining_timeout_sec
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if protocol is not None:
                kwargs['protocol'] = protocol
            if region is not None:
                kwargs['region'] = region
            if session_affinity is not None:
                kwargs['session_affinity'] = session_affinity
            if timeout_sec is not None:
                kwargs['timeout_sec'] = timeout_sec
            if backend is not None:
                kwargs['backend'] = backend
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
