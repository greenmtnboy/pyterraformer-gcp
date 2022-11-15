
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class Http2HealthCheckItem():
        # non-optional-blocks
        host: Optional[str] = None
        port: Optional[float] = None
        port_name: Optional[str] = None
        port_specification: Optional[str] = None
        proxy_header: Optional[str] = None
        request_path: Optional[str] = None
        response: Optional[str] = None
        
# wrapper list class
class Http2HealthCheck(BlockList):
        items: List[Http2HealthCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpHealthCheckItem():
        # non-optional-blocks
        host: Optional[str] = None
        port: Optional[float] = None
        port_name: Optional[str] = None
        port_specification: Optional[str] = None
        proxy_header: Optional[str] = None
        request_path: Optional[str] = None
        response: Optional[str] = None
        
# wrapper list class
class HttpHealthCheck(BlockList):
        items: List[HttpHealthCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpsHealthCheckItem():
        # non-optional-blocks
        host: Optional[str] = None
        port: Optional[float] = None
        port_name: Optional[str] = None
        port_specification: Optional[str] = None
        proxy_header: Optional[str] = None
        request_path: Optional[str] = None
        response: Optional[str] = None
        
# wrapper list class
class HttpsHealthCheck(BlockList):
        items: List[HttpsHealthCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SslHealthCheckItem():
        # non-optional-blocks
        port: Optional[float] = None
        port_name: Optional[str] = None
        port_specification: Optional[str] = None
        proxy_header: Optional[str] = None
        request: Optional[str] = None
        response: Optional[str] = None
        
# wrapper list class
class SslHealthCheck(BlockList):
        items: List[SslHealthCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TcpHealthCheckItem():
        # non-optional-blocks
        port: Optional[float] = None
        port_name: Optional[str] = None
        port_specification: Optional[str] = None
        proxy_header: Optional[str] = None
        request: Optional[str] = None
        response: Optional[str] = None
        
# wrapper list class
class TcpHealthCheck(BlockList):
        items: List[TcpHealthCheckItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeHealthCheck(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_compute_health_check'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        check_interval_sec: Optional[float] = None,
        description: Optional[str] = None,
        healthy_threshold: Optional[float] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        unhealthy_threshold: Optional[float] = None,
        http2_health_check: Optional[Http2HealthCheck]=None,
        http_health_check: Optional[HttpHealthCheck]=None,
        https_health_check: Optional[HttpsHealthCheck]=None,
        ssl_health_check: Optional[SslHealthCheck]=None,
        tcp_health_check: Optional[TcpHealthCheck]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if check_interval_sec is not None:
                kwargs['check_interval_sec'] = check_interval_sec
            if description is not None:
                kwargs['description'] = description
            if healthy_threshold is not None:
                kwargs['healthy_threshold'] = healthy_threshold
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeout_sec is not None:
                kwargs['timeout_sec'] = timeout_sec
            if unhealthy_threshold is not None:
                kwargs['unhealthy_threshold'] = unhealthy_threshold
            if http2_health_check is not None:
                kwargs['http2_health_check'] = http2_health_check
            if http_health_check is not None:
                kwargs['http_health_check'] = http_health_check
            if https_health_check is not None:
                kwargs['https_health_check'] = https_health_check
            if ssl_health_check is not None:
                kwargs['ssl_health_check'] = ssl_health_check
            if tcp_health_check is not None:
                kwargs['tcp_health_check'] = tcp_health_check
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
