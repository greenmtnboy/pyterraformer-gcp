
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CacheKeyPolicyItem():
        # non-optional-blocks
        include_host: Optional[bool] = None
        include_protocol: Optional[bool] = None
        include_query_string: Optional[bool] = None
        query_string_blacklist: Optional[Set[str]] = None
        query_string_whitelist: Optional[Set[str]] = None
        
# wrapper list class
class CacheKeyPolicy(BlockList):
        items: List[CacheKeyPolicyItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class BackendItem():
        # non-optional-blocks
        balancing_mode: Optional[str] = None
        capacity_scaler: Optional[float] = None
        description: Optional[str] = None
        group: Optional[str] = None
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



# this block can contain multiple items, items in a list are required
@dataclass 
class CdnPolicyItem():
        # non-optional-blocks
        signed_url_cache_max_age_sec: Optional[float] = None
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        
# wrapper list class
class CdnPolicy(BlockList):
        items: List[CdnPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IapItem():
        oauth2_client_id:str
        oauth2_client_secret:str
        # non-optional-blocks
        
# wrapper list class
class Iap(BlockList):
        items: List[IapItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeBackendService(ResourceObject):
    """    
    Args:
        health_checks (Set[str]): The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
                    for health checking this BackendService. Currently at most one health
                    check can be specified, and a health check is required.

                    For internal load balancing, a URL to a HealthCheck resource must be specified instead.
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
    """
    _type = 'google_compute_backend_service'
    
    def __init__(self,
        tf_id: str,
        health_checks:Set[str],
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        affinity_cookie_ttl_sec: Optional[float] = None,
        connection_draining_timeout_sec: Optional[float] = None,
        description: Optional[str] = None,
        enable_cdn: Optional[bool] = None,
        id: Optional[str] = None,
        load_balancing_scheme: Optional[str] = None,
        port_name: Optional[str] = None,
        project: Optional[str] = None,
        protocol: Optional[str] = None,
        security_policy: Optional[str] = None,
        session_affinity: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        backend: Optional[Backend]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        iap: Optional[Iap]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if health_checks is not None:
                kwargs['health_checks'] = health_checks
            if name is not None:
                kwargs['name'] = name
            if affinity_cookie_ttl_sec is not None:
                kwargs['affinity_cookie_ttl_sec'] = affinity_cookie_ttl_sec
            if connection_draining_timeout_sec is not None:
                kwargs['connection_draining_timeout_sec'] = connection_draining_timeout_sec
            if description is not None:
                kwargs['description'] = description
            if enable_cdn is not None:
                kwargs['enable_cdn'] = enable_cdn
            if id is not None:
                kwargs['id'] = id
            if load_balancing_scheme is not None:
                kwargs['load_balancing_scheme'] = load_balancing_scheme
            if port_name is not None:
                kwargs['port_name'] = port_name
            if project is not None:
                kwargs['project'] = project
            if protocol is not None:
                kwargs['protocol'] = protocol
            if security_policy is not None:
                kwargs['security_policy'] = security_policy
            if session_affinity is not None:
                kwargs['session_affinity'] = session_affinity
            if timeout_sec is not None:
                kwargs['timeout_sec'] = timeout_sec
            if cache_key_policy is not None:
                kwargs['cache_key_policy'] = cache_key_policy
            if backend is not None:
                kwargs['backend'] = backend
            if cdn_policy is not None:
                kwargs['cdn_policy'] = cdn_policy
            if iap is not None:
                kwargs['iap'] = iap
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
