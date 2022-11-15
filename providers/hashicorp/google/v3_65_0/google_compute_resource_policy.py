
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class DayOfWeeksItem():
        day:str
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class DayOfWeeks(BlockSet):
        items: Set[DayOfWeeksItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class DailyScheduleItem():
        days_in_cycle:float
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class DailySchedule(BlockList):
        items: List[DailyScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HourlyScheduleItem():
        hours_in_cycle:float
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class HourlySchedule(BlockList):
        items: List[HourlyScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WeeklyScheduleItem():
        # non-optional-blocks
        day_of_weeks: Optional[DayOfWeeks]=None,
        
# wrapper list class
class WeeklySchedule(BlockList):
        items: List[WeeklyScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RetentionPolicyItem():
        max_retention_days:float
        # non-optional-blocks
        on_source_disk_delete: Optional[str] = None
        
# wrapper list class
class RetentionPolicy(BlockList):
        items: List[RetentionPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScheduleItem():
        # non-optional-blocks
        day_of_weeks: Optional[DayOfWeeks]=None,
        daily_schedule: Optional[DailySchedule]=None,
        hourly_schedule: Optional[HourlySchedule]=None,
        weekly_schedule: Optional[WeeklySchedule]=None,
        
# wrapper list class
class Schedule(BlockList):
        items: List[ScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SnapshotPropertiesItem():
        # non-optional-blocks
        guest_flush: Optional[bool] = None
        labels: Optional[Dict[str, str]] = None
        storage_locations: Optional[Set[str]] = None
        
# wrapper list class
class SnapshotProperties(BlockList):
        items: List[SnapshotPropertiesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GroupPlacementPolicyItem():
        # non-optional-blocks
        availability_domain_count: Optional[float] = None
        collocation: Optional[str] = None
        vm_count: Optional[float] = None
        
# wrapper list class
class GroupPlacementPolicy(BlockList):
        items: List[GroupPlacementPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SnapshotSchedulePolicyItem():
        # non-optional-blocks
        day_of_weeks: Optional[DayOfWeeks]=None,
        daily_schedule: Optional[DailySchedule]=None,
        hourly_schedule: Optional[HourlySchedule]=None,
        weekly_schedule: Optional[WeeklySchedule]=None,
        retention_policy: Optional[RetentionPolicy]=None,
        schedule: Optional[Schedule]=None,
        snapshot_properties: Optional[SnapshotProperties]=None,
        
# wrapper list class
class SnapshotSchedulePolicy(BlockList):
        items: List[SnapshotSchedulePolicyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleComputeResourcePolicy(ResourceObject):
    """    
    Args:
        name (str): The name of the resource, provided by the client when initially creating
                    the resource. The resource name must be 1-63 characters long, and comply
                    with RFC1035. Specifically, the name must be 1-63 characters long and
                    match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])'? which means the
                    first character must be a lowercase letter, and all following characters
                    must be a dash, lowercase letter, or digit, except the last character,
                    which cannot be a dash.
    """
    _type = 'google_compute_resource_policy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        day_of_weeks: Optional[DayOfWeeks]=None,
        daily_schedule: Optional[DailySchedule]=None,
        hourly_schedule: Optional[HourlySchedule]=None,
        weekly_schedule: Optional[WeeklySchedule]=None,
        retention_policy: Optional[RetentionPolicy]=None,
        schedule: Optional[Schedule]=None,
        snapshot_properties: Optional[SnapshotProperties]=None,
        group_placement_policy: Optional[GroupPlacementPolicy]=None,
        snapshot_schedule_policy: Optional[SnapshotSchedulePolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if day_of_weeks is not None:
                kwargs['day_of_weeks'] = day_of_weeks
            if daily_schedule is not None:
                kwargs['daily_schedule'] = daily_schedule
            if hourly_schedule is not None:
                kwargs['hourly_schedule'] = hourly_schedule
            if weekly_schedule is not None:
                kwargs['weekly_schedule'] = weekly_schedule
            if retention_policy is not None:
                kwargs['retention_policy'] = retention_policy
            if schedule is not None:
                kwargs['schedule'] = schedule
            if snapshot_properties is not None:
                kwargs['snapshot_properties'] = snapshot_properties
            if group_placement_policy is not None:
                kwargs['group_placement_policy'] = group_placement_policy
            if snapshot_schedule_policy is not None:
                kwargs['snapshot_schedule_policy'] = snapshot_schedule_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
