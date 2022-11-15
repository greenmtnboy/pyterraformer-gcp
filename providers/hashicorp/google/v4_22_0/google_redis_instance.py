
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
class MaintenanceScheduleItem():
        # non-optional-blocks
        
# wrapper list class
class MaintenanceSchedule(BlockList):
        items: List[MaintenanceScheduleItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleRedisInstance(ResourceObject):
    """    
    Args:
        memory_size_gb (float): Redis memory size in GiB.
        name (str): The ID of the instance or a fully qualified identifier for the instance.
    """
    _type = 'google_redis_instance'
    
    def __init__(self,
        tf_id: str,
        memory_size_gb:float,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        alternative_location_id: Optional[str] = None,
        auth_enabled: Optional[bool] = None,
        authorized_network: Optional[str] = None,
        connect_mode: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location_id: Optional[str] = None,
        project: Optional[str] = None,
        read_replicas_mode: Optional[str] = None,
        redis_configs: Optional[Dict[str, str]] = None,
        redis_version: Optional[str] = None,
        region: Optional[str] = None,
        replica_count: Optional[float] = None,
        reserved_ip_range: Optional[str] = None,
        secondary_ip_range: Optional[str] = None,
        tier: Optional[str] = None,
        transit_encryption_mode: Optional[str] = None,
        start_time: Optional[StartTime]=None,
        weekly_maintenance_window: Optional[WeeklyMaintenanceWindow]=None,
        maintenance_policy: Optional[MaintenancePolicy]=None,
        maintenance_schedule: Optional[MaintenanceSchedule]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if memory_size_gb is not None:
                kwargs['memory_size_gb'] = memory_size_gb
            if name is not None:
                kwargs['name'] = name
            if alternative_location_id is not None:
                kwargs['alternative_location_id'] = alternative_location_id
            if auth_enabled is not None:
                kwargs['auth_enabled'] = auth_enabled
            if authorized_network is not None:
                kwargs['authorized_network'] = authorized_network
            if connect_mode is not None:
                kwargs['connect_mode'] = connect_mode
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if location_id is not None:
                kwargs['location_id'] = location_id
            if project is not None:
                kwargs['project'] = project
            if read_replicas_mode is not None:
                kwargs['read_replicas_mode'] = read_replicas_mode
            if redis_configs is not None:
                kwargs['redis_configs'] = redis_configs
            if redis_version is not None:
                kwargs['redis_version'] = redis_version
            if region is not None:
                kwargs['region'] = region
            if replica_count is not None:
                kwargs['replica_count'] = replica_count
            if reserved_ip_range is not None:
                kwargs['reserved_ip_range'] = reserved_ip_range
            if secondary_ip_range is not None:
                kwargs['secondary_ip_range'] = secondary_ip_range
            if tier is not None:
                kwargs['tier'] = tier
            if transit_encryption_mode is not None:
                kwargs['transit_encryption_mode'] = transit_encryption_mode
            if start_time is not None:
                kwargs['start_time'] = start_time
            if weekly_maintenance_window is not None:
                kwargs['weekly_maintenance_window'] = weekly_maintenance_window
            if maintenance_policy is not None:
                kwargs['maintenance_policy'] = maintenance_policy
            if maintenance_schedule is not None:
                kwargs['maintenance_schedule'] = maintenance_schedule
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
