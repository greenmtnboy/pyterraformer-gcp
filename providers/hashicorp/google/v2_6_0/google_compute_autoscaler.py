
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CpuUtilizationItem():
        target:float
        # non-optional-blocks
        
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
class AutoscalingPolicyItem():
        max_replicas:float
        min_replicas:float
        # non-optional-blocks
        cooldown_period: Optional[float] = None
        cpu_utilization: Optional[CpuUtilization]=None,
        load_balancing_utilization: Optional[LoadBalancingUtilization]=None,
        metric: Optional[Metric]=None,
        
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




class GoogleComputeAutoscaler(ResourceObject):
    """    
    Args:
        name (str): 
        target (str): 
    """
    _type = 'google_compute_autoscaler'
    
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
        zone: Optional[str] = None,
        cpu_utilization: Optional[CpuUtilization]=None,
        load_balancing_utilization: Optional[LoadBalancingUtilization]=None,
        metric: Optional[Metric]=None,
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
            if zone is not None:
                kwargs['zone'] = zone
            if cpu_utilization is not None:
                kwargs['cpu_utilization'] = cpu_utilization
            if load_balancing_utilization is not None:
                kwargs['load_balancing_utilization'] = load_balancing_utilization
            if metric is not None:
                kwargs['metric'] = metric
            if autoscaling_policy is not None:
                kwargs['autoscaling_policy'] = autoscaling_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
