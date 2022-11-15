
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AppEngineRoutingOverrideItem():
        # non-optional-blocks
        instance: Optional[str] = None
        service: Optional[str] = None
        version: Optional[str] = None
        
# wrapper list class
class AppEngineRoutingOverride(BlockList):
        items: List[AppEngineRoutingOverrideItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RateLimitsItem():
        # non-optional-blocks
        max_concurrent_dispatches: Optional[float] = None
        max_dispatches_per_second: Optional[float] = None
        
# wrapper list class
class RateLimits(BlockList):
        items: List[RateLimitsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RetryConfigItem():
        # non-optional-blocks
        max_attempts: Optional[float] = None
        max_backoff: Optional[str] = None
        max_doublings: Optional[float] = None
        max_retry_duration: Optional[str] = None
        min_backoff: Optional[str] = None
        
# wrapper list class
class RetryConfig(BlockList):
        items: List[RetryConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudTasksQueue(ResourceObject):
    """    
    Args:
        location (str): The location of the queue
    """
    _type = 'google_cloud_tasks_queue'
    
    def __init__(self,
        tf_id: str,
        location:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        app_engine_routing_override: Optional[AppEngineRoutingOverride]=None,
        rate_limits: Optional[RateLimits]=None,
        retry_config: Optional[RetryConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if id is not None:
                kwargs['id'] = id
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if app_engine_routing_override is not None:
                kwargs['app_engine_routing_override'] = app_engine_routing_override
            if rate_limits is not None:
                kwargs['rate_limits'] = rate_limits
            if retry_config is not None:
                kwargs['retry_config'] = retry_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
