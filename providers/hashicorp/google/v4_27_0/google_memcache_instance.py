
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class StartTimeItem():
        # non-optional-blocks
        hours: Optional[float] = None
        minutes: Optional[float] = None
        nanos: Optional[float] = None
        seconds: Optional[float] = None
        
# wrapper list class
class StartTime(BlockList):
        items: List[StartTimeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WeeklyMaintenanceWindowItem():
        day:str
        duration:str
        # non-optional-blocks
        start_time: Optional[StartTime]=None,
        
# wrapper list class
class WeeklyMaintenanceWindow(BlockList):
        items: List[WeeklyMaintenanceWindowItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaintenancePolicyItem():
        # non-optional-blocks
        description: Optional[str] = None
        start_time: Optional[StartTime]=None,
        weekly_maintenance_window: Optional[WeeklyMaintenanceWindow]=None,
        
# wrapper list class
class MaintenancePolicy(BlockList):
        items: List[MaintenancePolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MemcacheParametersItem():
        # non-optional-blocks
        params: Optional[Dict[str, str]] = None
        
# wrapper list class
class MemcacheParameters(BlockList):
        items: List[MemcacheParametersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NodeConfigItem():
        cpu_count:float
        memory_size_mb:float
        # non-optional-blocks
        
# wrapper list class
class NodeConfig(BlockList):
        items: List[NodeConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleMemcacheInstance(ResourceObject):
    """    
    Args:
        name (str): The resource name of the instance.
        node_count (float): Number of nodes in the memcache instance.
    """
    _type = 'google_memcache_instance'
    
    def __init__(self,
        tf_id: str,
        name:str,
        node_count:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        authorized_network: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        memcache_version: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        zones: Optional[Set[str]] = None,
        start_time: Optional[StartTime]=None,
        weekly_maintenance_window: Optional[WeeklyMaintenanceWindow]=None,
        maintenance_policy: Optional[MaintenancePolicy]=None,
        memcache_parameters: Optional[MemcacheParameters]=None,
        node_config: Optional[NodeConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if node_count is not None:
                kwargs['node_count'] = node_count
            if authorized_network is not None:
                kwargs['authorized_network'] = authorized_network
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if memcache_version is not None:
                kwargs['memcache_version'] = memcache_version
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if zones is not None:
                kwargs['zones'] = zones
            if start_time is not None:
                kwargs['start_time'] = start_time
            if weekly_maintenance_window is not None:
                kwargs['weekly_maintenance_window'] = weekly_maintenance_window
            if maintenance_policy is not None:
                kwargs['maintenance_policy'] = maintenance_policy
            if memcache_parameters is not None:
                kwargs['memcache_parameters'] = memcache_parameters
            if node_config is not None:
                kwargs['node_config'] = node_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
