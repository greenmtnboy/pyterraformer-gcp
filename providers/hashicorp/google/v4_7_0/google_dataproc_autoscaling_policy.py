
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class YarnConfigItem():
        graceful_decommission_timeout:str
        scale_down_factor:float
        scale_up_factor:float
        # non-optional-blocks
        scale_down_min_worker_fraction: Optional[float] = None
        scale_up_min_worker_fraction: Optional[float] = None
        
# wrapper list class
class YarnConfig(BlockList):
        items: List[YarnConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BasicAlgorithmItem():
        # non-optional-blocks
        cooldown_period: Optional[str] = None
        yarn_config: Optional[YarnConfig]=None,
        
# wrapper list class
class BasicAlgorithm(BlockList):
        items: List[BasicAlgorithmItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecondaryWorkerConfigItem():
        # non-optional-blocks
        max_instances: Optional[float] = None
        min_instances: Optional[float] = None
        weight: Optional[float] = None
        
# wrapper list class
class SecondaryWorkerConfig(BlockList):
        items: List[SecondaryWorkerConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkerConfigItem():
        max_instances:float
        # non-optional-blocks
        min_instances: Optional[float] = None
        weight: Optional[float] = None
        
# wrapper list class
class WorkerConfig(BlockList):
        items: List[WorkerConfigItem]




class GoogleDataprocAutoscalingPolicy(ResourceObject):
    """    
    Args:
        policy_id (str): The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
                    and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
                    3 and 50 characters.
    """
    _type = 'google_dataproc_autoscaling_policy'
    
    def __init__(self,
        tf_id: str,
        policy_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        yarn_config: Optional[YarnConfig]=None,
        basic_algorithm: Optional[BasicAlgorithm]=None,
        secondary_worker_config: Optional[SecondaryWorkerConfig]=None,
        timeouts: Optional[Timeouts]=None,
        worker_config: Optional[WorkerConfig]=None,
        ):
            kwargs = {}
            if policy_id is not None:
                kwargs['policy_id'] = policy_id
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if yarn_config is not None:
                kwargs['yarn_config'] = yarn_config
            if basic_algorithm is not None:
                kwargs['basic_algorithm'] = basic_algorithm
            if secondary_worker_config is not None:
                kwargs['secondary_worker_config'] = secondary_worker_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if worker_config is not None:
                kwargs['worker_config'] = worker_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
