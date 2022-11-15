
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class MaxScaledInReplicasItem():
        # non-optional-blocks
        fixed: Optional[float] = None
        percent: Optional[float] = None
        
# wrapper list class
class MaxScaledInReplicas(BlockList):
        items: List[MaxScaledInReplicasItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CpuUtilizationItem():
        target:float
        # non-optional-blocks
        predictive_method: Optional[str] = None
        
# wrapper list class
class CpuUtilization(BlockList):
        items: List[CpuUtilizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LoadBalancingUtilizationItem():
        target:float
        # non-optional-blocks
        
# wrapper list class
class LoadBalancingUtilization(BlockList):
        items: List[LoadBalancingUtilizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MetricItem():
        name:str
        # non-optional-blocks
        target: Optional[float] = None
        type: Optional[str] = None
        
# wrapper list class
class Metric(BlockList):
        items: List[MetricItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScaleInControlItem():
        # non-optional-blocks
        time_window_sec: Optional[float] = None
        max_scaled_in_replicas: Optional[MaxScaledInReplicas]=None,
        
# wrapper list class
class ScaleInControl(BlockList):
        items: List[ScaleInControlItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class ScalingSchedulesItem():
        duration_sec:float
        min_required_replicas:float
        name:str
        schedule:str
        # non-optional-blocks
        description: Optional[str] = None
        disabled: Optional[bool] = None
        time_zone: Optional[str] = None
        
# wrapper list class
class ScalingSchedules(BlockSet):
        items: Set[ScalingSchedulesItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class AutoscalingPolicyItem():
        max_replicas:float
        min_replicas:float
        # non-optional-blocks
        cooldown_period: Optional[float] = None
        mode: Optional[str] = None
        max_scaled_in_replicas: Optional[MaxScaledInReplicas]=None,
        cpu_utilization: Optional[CpuUtilization]=None,
        load_balancing_utilization: Optional[LoadBalancingUtilization]=None,
        metric: Optional[Metric]=None,
        scale_in_control: Optional[ScaleInControl]=None,
        scaling_schedules: Optional[ScalingSchedules]=None,
        
# wrapper list class
class AutoscalingPolicy(BlockList):
        items: List[AutoscalingPolicyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRegionAutoscaler(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. The name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
        target (str): URL of the managed instance group that this autoscaler will scale.
    """
    _type = 'google_compute_region_autoscaler'
    
    def __init__(self,
        tf_id: str,
        name:str,
        target:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        max_scaled_in_replicas: Optional[MaxScaledInReplicas]=None,
        cpu_utilization: Optional[CpuUtilization]=None,
        load_balancing_utilization: Optional[LoadBalancingUtilization]=None,
        metric: Optional[Metric]=None,
        scale_in_control: Optional[ScaleInControl]=None,
        scaling_schedules: Optional[ScalingSchedules]=None,
        autoscaling_policy: Optional[AutoscalingPolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if target is not None:
                kwargs['target'] = target
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if max_scaled_in_replicas is not None:
                kwargs['max_scaled_in_replicas'] = max_scaled_in_replicas
            if cpu_utilization is not None:
                kwargs['cpu_utilization'] = cpu_utilization
            if load_balancing_utilization is not None:
                kwargs['load_balancing_utilization'] = load_balancing_utilization
            if metric is not None:
                kwargs['metric'] = metric
            if scale_in_control is not None:
                kwargs['scale_in_control'] = scale_in_control
            if scaling_schedules is not None:
                kwargs['scaling_schedules'] = scaling_schedules
            if autoscaling_policy is not None:
                kwargs['autoscaling_policy'] = autoscaling_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
