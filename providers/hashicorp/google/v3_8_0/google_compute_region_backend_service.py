
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class BackendItem():
        group:str
        # non-optional-blocks
        balancing_mode: Optional[str] = None
        capacity_scaler: Optional[float] = None
        description: Optional[str] = None
        max_connections: Optional[float] = None
        max_connections_per_endpoint: Optional[float] = None
        max_connections_per_instance: Optional[float] = None
        max_rate: Optional[float] = None
        max_rate_per_endpoint: Optional[float] = None
        max_rate_per_instance: Optional[float] = None
        max_utilization: Optional[float] = None
        
# wrapper list class
class Backend(BlockSet):
        items: Set[BackendItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRegionBackendService(ResourceObject):
    """    
    Args:
        health_checks (Set[str]): The set of URLs to HealthCheck resources for health checking
                    this RegionBackendService. Currently at most one health
                    check can be specified, and a health check is required.
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
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
        load_balancing_scheme: Optional[str] = None,
        project: Optional[str] = None,
        protocol: Optional[str] = None,
        region: Optional[str] = None,
        session_affinity: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        backend: Optional[Backend]=None,
        timeouts: Optional[Timeouts]=None,
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
            if load_balancing_scheme is not None:
                kwargs['load_balancing_scheme'] = load_balancing_scheme
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
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
