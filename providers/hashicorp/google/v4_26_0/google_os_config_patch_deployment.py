
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DisruptionBudgetItem():
        # non-optional-blocks
        fixed: Optional[float] = None
        percentage: Optional[float] = None
        
# wrapper list class
class DisruptionBudget(BlockList):
        items: List[DisruptionBudgetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WeekDayOfMonthItem():
        day_of_week:str
        week_ordinal:float
        # non-optional-blocks
        
# wrapper list class
class WeekDayOfMonth(BlockList):
        items: List[WeekDayOfMonthItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MonthlyItem():
        # non-optional-blocks
        month_day: Optional[float] = None
        week_day_of_month: Optional[WeekDayOfMonth]=None,
        
# wrapper list class
class Monthly(BlockList):
        items: List[MonthlyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimeOfDayItem():
        # non-optional-blocks
        hours: Optional[float] = None
        minutes: Optional[float] = None
        nanos: Optional[float] = None
        seconds: Optional[float] = None
        
# wrapper list class
class TimeOfDay(BlockList):
        items: List[TimeOfDayItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimeZoneItem():
        id:str
        # non-optional-blocks
        version: Optional[str] = None
        
# wrapper list class
class TimeZone(BlockList):
        items: List[TimeZoneItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WeeklyItem():
        day_of_week:str
        # non-optional-blocks
        
# wrapper list class
class Weekly(BlockList):
        items: List[WeeklyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GcsObjectItem():
        bucket:str
        generation_number:str
        object:str
        # non-optional-blocks
        
# wrapper list class
class GcsObject(BlockList):
        items: List[GcsObjectItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LinuxExecStepConfigItem():
        # non-optional-blocks
        allowed_success_codes: Optional[List[float]] = None
        interpreter: Optional[str] = None
        local_path: Optional[str] = None
        gcs_object: Optional[GcsObject]=None,
        
# wrapper list class
class LinuxExecStepConfig(BlockList):
        items: List[LinuxExecStepConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WindowsExecStepConfigItem():
        # non-optional-blocks
        allowed_success_codes: Optional[List[float]] = None
        interpreter: Optional[str] = None
        local_path: Optional[str] = None
        gcs_object: Optional[GcsObject]=None,
        
# wrapper list class
class WindowsExecStepConfig(BlockList):
        items: List[WindowsExecStepConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AptItem():
        # non-optional-blocks
        excludes: Optional[List[str]] = None
        exclusive_packages: Optional[List[str]] = None
        type: Optional[str] = None
        
# wrapper list class
class Apt(BlockList):
        items: List[AptItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GooItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class Goo(BlockList):
        items: List[GooItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PostStepItem():
        # non-optional-blocks
        gcs_object: Optional[GcsObject]=None,
        linux_exec_step_config: Optional[LinuxExecStepConfig]=None,
        windows_exec_step_config: Optional[WindowsExecStepConfig]=None,
        
# wrapper list class
class PostStep(BlockList):
        items: List[PostStepItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PreStepItem():
        # non-optional-blocks
        gcs_object: Optional[GcsObject]=None,
        linux_exec_step_config: Optional[LinuxExecStepConfig]=None,
        windows_exec_step_config: Optional[WindowsExecStepConfig]=None,
        
# wrapper list class
class PreStep(BlockList):
        items: List[PreStepItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WindowsUpdateItem():
        # non-optional-blocks
        classifications: Optional[List[str]] = None
        excludes: Optional[List[str]] = None
        exclusive_patches: Optional[List[str]] = None
        
# wrapper list class
class WindowsUpdate(BlockList):
        items: List[WindowsUpdateItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class YumItem():
        # non-optional-blocks
        excludes: Optional[List[str]] = None
        exclusive_packages: Optional[List[str]] = None
        minimal: Optional[bool] = None
        security: Optional[bool] = None
        
# wrapper list class
class Yum(BlockList):
        items: List[YumItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ZypperItem():
        # non-optional-blocks
        categories: Optional[List[str]] = None
        excludes: Optional[List[str]] = None
        exclusive_patches: Optional[List[str]] = None
        severities: Optional[List[str]] = None
        with_optional: Optional[bool] = None
        with_update: Optional[bool] = None
        
# wrapper list class
class Zypper(BlockList):
        items: List[ZypperItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GroupLabelsItem():
        labels:Dict[str, str]
        # non-optional-blocks
        
# wrapper list class
class GroupLabels(BlockList):
        items: List[GroupLabelsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InstanceFilterItem():
        # non-optional-blocks
        all: Optional[bool] = None
        instance_name_prefixes: Optional[List[str]] = None
        instances: Optional[List[str]] = None
        zones: Optional[List[str]] = None
        group_labels: Optional[GroupLabels]=None,
        
# wrapper list class
class InstanceFilter(BlockList):
        items: List[InstanceFilterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OneTimeScheduleItem():
        execute_time:str
        # non-optional-blocks
        
# wrapper list class
class OneTimeSchedule(BlockList):
        items: List[OneTimeScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PatchConfigItem():
        # non-optional-blocks
        mig_instances_allowed: Optional[bool] = None
        reboot_config: Optional[str] = None
        gcs_object: Optional[GcsObject]=None,
        linux_exec_step_config: Optional[LinuxExecStepConfig]=None,
        windows_exec_step_config: Optional[WindowsExecStepConfig]=None,
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        post_step: Optional[PostStep]=None,
        pre_step: Optional[PreStep]=None,
        windows_update: Optional[WindowsUpdate]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        
# wrapper list class
class PatchConfig(BlockList):
        items: List[PatchConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RecurringScheduleItem():
        # non-optional-blocks
        end_time: Optional[str] = None
        start_time: Optional[str] = None
        week_day_of_month: Optional[WeekDayOfMonth]=None,
        monthly: Optional[Monthly]=None,
        time_of_day: Optional[TimeOfDay]=None,
        time_zone: Optional[TimeZone]=None,
        weekly: Optional[Weekly]=None,
        
# wrapper list class
class RecurringSchedule(BlockList):
        items: List[RecurringScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RolloutItem():
        mode:str
        # non-optional-blocks
        disruption_budget: Optional[DisruptionBudget]=None,
        
# wrapper list class
class Rollout(BlockList):
        items: List[RolloutItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleOsConfigPatchDeployment(ResourceObject):
    """    
    Args:
        patch_deployment_id (str): A name for the patch deployment in the project. When creating a name the following rules apply:
                    * Must contain only lowercase letters, numbers, and hyphens.
                    * Must start with a letter.
                    * Must be between 1-63 characters.
                    * Must end with a number or a letter.
                    * Must be unique within the project.
    """
    _type = 'google_os_config_patch_deployment'
    
    def __init__(self,
        tf_id: str,
        patch_deployment_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        duration: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        disruption_budget: Optional[DisruptionBudget]=None,
        week_day_of_month: Optional[WeekDayOfMonth]=None,
        monthly: Optional[Monthly]=None,
        time_of_day: Optional[TimeOfDay]=None,
        time_zone: Optional[TimeZone]=None,
        weekly: Optional[Weekly]=None,
        gcs_object: Optional[GcsObject]=None,
        linux_exec_step_config: Optional[LinuxExecStepConfig]=None,
        windows_exec_step_config: Optional[WindowsExecStepConfig]=None,
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        post_step: Optional[PostStep]=None,
        pre_step: Optional[PreStep]=None,
        windows_update: Optional[WindowsUpdate]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        group_labels: Optional[GroupLabels]=None,
        instance_filter: Optional[InstanceFilter]=None,
        one_time_schedule: Optional[OneTimeSchedule]=None,
        patch_config: Optional[PatchConfig]=None,
        recurring_schedule: Optional[RecurringSchedule]=None,
        rollout: Optional[Rollout]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if patch_deployment_id is not None:
                kwargs['patch_deployment_id'] = patch_deployment_id
            if description is not None:
                kwargs['description'] = description
            if duration is not None:
                kwargs['duration'] = duration
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if disruption_budget is not None:
                kwargs['disruption_budget'] = disruption_budget
            if week_day_of_month is not None:
                kwargs['week_day_of_month'] = week_day_of_month
            if monthly is not None:
                kwargs['monthly'] = monthly
            if time_of_day is not None:
                kwargs['time_of_day'] = time_of_day
            if time_zone is not None:
                kwargs['time_zone'] = time_zone
            if weekly is not None:
                kwargs['weekly'] = weekly
            if gcs_object is not None:
                kwargs['gcs_object'] = gcs_object
            if linux_exec_step_config is not None:
                kwargs['linux_exec_step_config'] = linux_exec_step_config
            if windows_exec_step_config is not None:
                kwargs['windows_exec_step_config'] = windows_exec_step_config
            if apt is not None:
                kwargs['apt'] = apt
            if goo is not None:
                kwargs['goo'] = goo
            if post_step is not None:
                kwargs['post_step'] = post_step
            if pre_step is not None:
                kwargs['pre_step'] = pre_step
            if windows_update is not None:
                kwargs['windows_update'] = windows_update
            if yum is not None:
                kwargs['yum'] = yum
            if zypper is not None:
                kwargs['zypper'] = zypper
            if group_labels is not None:
                kwargs['group_labels'] = group_labels
            if instance_filter is not None:
                kwargs['instance_filter'] = instance_filter
            if one_time_schedule is not None:
                kwargs['one_time_schedule'] = one_time_schedule
            if patch_config is not None:
                kwargs['patch_config'] = patch_config
            if recurring_schedule is not None:
                kwargs['recurring_schedule'] = recurring_schedule
            if rollout is not None:
                kwargs['rollout'] = rollout
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
