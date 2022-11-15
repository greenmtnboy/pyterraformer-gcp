
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class BaseEjectionTimeItem():
        seconds:float
        # non-optional-blocks
        nanos: Optional[float] = None
        
# wrapper list class
class BaseEjectionTime(BlockList):
        items: List[BaseEjectionTimeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IntervalItem():
        seconds:float
        # non-optional-blocks
        nanos: Optional[float] = None
        
# wrapper list class
class Interval(BlockList):
        items: List[IntervalItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TtlItem():
        seconds:float
        # non-optional-blocks
        nanos: Optional[float] = None
        
# wrapper list class
class Ttl(BlockList):
        items: List[TtlItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpCookieItem():
        # non-optional-blocks
        name: Optional[str] = None
        path: Optional[str] = None
        ttl: Optional[Ttl]=None,
        
# wrapper list class
class HttpCookie(BlockList):
        items: List[HttpCookieItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class BackendItem():
        group:str
        # non-optional-blocks
        balancing_mode: Optional[str] = None
        capacity_scaler: Optional[float] = None
        description: Optional[str] = None
        failover: Optional[bool] = None
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
class CircuitBreakersItem():
        # non-optional-blocks
        max_connections: Optional[float] = None
        max_pending_requests: Optional[float] = None
        max_requests: Optional[float] = None
        max_requests_per_connection: Optional[float] = None
        max_retries: Optional[float] = None
        
# wrapper list class
class CircuitBreakers(BlockList):
        items: List[CircuitBreakersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConsistentHashItem():
        # non-optional-blocks
        http_header_name: Optional[str] = None
        minimum_ring_size: Optional[float] = None
        ttl: Optional[Ttl]=None,
        http_cookie: Optional[HttpCookie]=None,
        
# wrapper list class
class ConsistentHash(BlockList):
        items: List[ConsistentHashItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FailoverPolicyItem():
        # non-optional-blocks
        disable_connection_drain_on_failover: Optional[bool] = None
        drop_traffic_if_unhealthy: Optional[bool] = None
        failover_ratio: Optional[float] = None
        
# wrapper list class
class FailoverPolicy(BlockList):
        items: List[FailoverPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LogConfigItem():
        # non-optional-blocks
        enable: Optional[bool] = None
        sample_rate: Optional[float] = None
        
# wrapper list class
class LogConfig(BlockList):
        items: List[LogConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OutlierDetectionItem():
        # non-optional-blocks
        consecutive_errors: Optional[float] = None
        consecutive_gateway_failure: Optional[float] = None
        enforcing_consecutive_errors: Optional[float] = None
        enforcing_consecutive_gateway_failure: Optional[float] = None
        enforcing_success_rate: Optional[float] = None
        max_ejection_percent: Optional[float] = None
        success_rate_minimum_hosts: Optional[float] = None
        success_rate_request_volume: Optional[float] = None
        success_rate_stdev_factor: Optional[float] = None
        base_ejection_time: Optional[BaseEjectionTime]=None,
        interval: Optional[Interval]=None,
        
# wrapper list class
class OutlierDetection(BlockList):
        items: List[OutlierDetectionItem]




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
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        affinity_cookie_ttl_sec: Optional[float] = None,
        connection_draining_timeout_sec: Optional[float] = None,
        description: Optional[str] = None,
        health_checks: Optional[Set[str]] = None,
        id: Optional[str] = None,
        load_balancing_scheme: Optional[str] = None,
        locality_lb_policy: Optional[str] = None,
        network: Optional[str] = None,
        port_name: Optional[str] = None,
        project: Optional[str] = None,
        protocol: Optional[str] = None,
        region: Optional[str] = None,
        session_affinity: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        base_ejection_time: Optional[BaseEjectionTime]=None,
        interval: Optional[Interval]=None,
        ttl: Optional[Ttl]=None,
        http_cookie: Optional[HttpCookie]=None,
        backend: Optional[Backend]=None,
        circuit_breakers: Optional[CircuitBreakers]=None,
        consistent_hash: Optional[ConsistentHash]=None,
        failover_policy: Optional[FailoverPolicy]=None,
        log_config: Optional[LogConfig]=None,
        outlier_detection: Optional[OutlierDetection]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if affinity_cookie_ttl_sec is not None:
                kwargs['affinity_cookie_ttl_sec'] = affinity_cookie_ttl_sec
            if connection_draining_timeout_sec is not None:
                kwargs['connection_draining_timeout_sec'] = connection_draining_timeout_sec
            if description is not None:
                kwargs['description'] = description
            if health_checks is not None:
                kwargs['health_checks'] = health_checks
            if id is not None:
                kwargs['id'] = id
            if load_balancing_scheme is not None:
                kwargs['load_balancing_scheme'] = load_balancing_scheme
            if locality_lb_policy is not None:
                kwargs['locality_lb_policy'] = locality_lb_policy
            if network is not None:
                kwargs['network'] = network
            if port_name is not None:
                kwargs['port_name'] = port_name
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
            if base_ejection_time is not None:
                kwargs['base_ejection_time'] = base_ejection_time
            if interval is not None:
                kwargs['interval'] = interval
            if ttl is not None:
                kwargs['ttl'] = ttl
            if http_cookie is not None:
                kwargs['http_cookie'] = http_cookie
            if backend is not None:
                kwargs['backend'] = backend
            if circuit_breakers is not None:
                kwargs['circuit_breakers'] = circuit_breakers
            if consistent_hash is not None:
                kwargs['consistent_hash'] = consistent_hash
            if failover_policy is not None:
                kwargs['failover_policy'] = failover_policy
            if log_config is not None:
                kwargs['log_config'] = log_config
            if outlier_detection is not None:
                kwargs['outlier_detection'] = outlier_detection
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
