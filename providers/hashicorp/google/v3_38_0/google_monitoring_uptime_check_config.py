
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AuthInfoItem():
        password:str
        username:str
        # non-optional-blocks
        
# wrapper list class
class AuthInfo(BlockList):
        items: List[AuthInfoItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ContentMatchersItem():
        content:str
        # non-optional-blocks
        matcher: Optional[str] = None
        
# wrapper list class
class ContentMatchers(BlockList):
        items: List[ContentMatchersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpCheckItem():
        # non-optional-blocks
        body: Optional[str] = None
        content_type: Optional[str] = None
        headers: Optional[Dict[str, str]] = None
        mask_headers: Optional[bool] = None
        path: Optional[str] = None
        port: Optional[float] = None
        request_method: Optional[str] = None
        use_ssl: Optional[bool] = None
        validate_ssl: Optional[bool] = None
        auth_info: Optional[AuthInfo]=None,
        
# wrapper list class
class HttpCheck(BlockList):
        items: List[HttpCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InternalCheckersItem():
        # non-optional-blocks
        display_name: Optional[str] = None
        gcp_zone: Optional[str] = None
        name: Optional[str] = None
        network: Optional[str] = None
        peer_project_id: Optional[str] = None
        
# wrapper list class
class InternalCheckers(BlockList):
        items: List[InternalCheckersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MonitoredResourceItem():
        labels:Dict[str, str]
        type:str
        # non-optional-blocks
        
# wrapper list class
class MonitoredResource(BlockList):
        items: List[MonitoredResourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourceGroupItem():
        # non-optional-blocks
        group_id: Optional[str] = None
        resource_type: Optional[str] = None
        
# wrapper list class
class ResourceGroup(BlockList):
        items: List[ResourceGroupItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TcpCheckItem():
        port:float
        # non-optional-blocks
        
# wrapper list class
class TcpCheck(BlockList):
        items: List[TcpCheckItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleMonitoringUptimeCheckConfig(ResourceObject):
    """    
    Args:
        display_name (str): A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced.
        timeout (str): The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
    """
    _type = 'google_monitoring_uptime_check_config'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        timeout:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        is_internal: Optional[bool] = None,
        period: Optional[str] = None,
        project: Optional[str] = None,
        selected_regions: Optional[List[str]] = None,
        auth_info: Optional[AuthInfo]=None,
        content_matchers: Optional[ContentMatchers]=None,
        http_check: Optional[HttpCheck]=None,
        internal_checkers: Optional[InternalCheckers]=None,
        monitored_resource: Optional[MonitoredResource]=None,
        resource_group: Optional[ResourceGroup]=None,
        tcp_check: Optional[TcpCheck]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if timeout is not None:
                kwargs['timeout'] = timeout
            if id is not None:
                kwargs['id'] = id
            if is_internal is not None:
                kwargs['is_internal'] = is_internal
            if period is not None:
                kwargs['period'] = period
            if project is not None:
                kwargs['project'] = project
            if selected_regions is not None:
                kwargs['selected_regions'] = selected_regions
            if auth_info is not None:
                kwargs['auth_info'] = auth_info
            if content_matchers is not None:
                kwargs['content_matchers'] = content_matchers
            if http_check is not None:
                kwargs['http_check'] = http_check
            if internal_checkers is not None:
                kwargs['internal_checkers'] = internal_checkers
            if monitored_resource is not None:
                kwargs['monitored_resource'] = monitored_resource
            if resource_group is not None:
                kwargs['resource_group'] = resource_group
            if tcp_check is not None:
                kwargs['tcp_check'] = tcp_check
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
