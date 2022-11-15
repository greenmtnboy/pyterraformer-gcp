
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AutoscalingPolicyItem():
        # non-optional-blocks
        max_nodes: Optional[float] = None
        min_nodes: Optional[float] = None
        mode: Optional[str] = None
        
# wrapper list class
class AutoscalingPolicy(BlockList):
        items: List[AutoscalingPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaintenanceWindowItem():
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class MaintenanceWindow(BlockList):
        items: List[MaintenanceWindowItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeNodeGroup(ResourceObject):
    """    
    Args:
        node_template (str): The URL of the node template to which this node group belongs.
    """
    _type = 'google_compute_node_group'
    
    def __init__(self,
        tf_id: str,
        node_template:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        initial_size: Optional[float] = None,
        maintenance_policy: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        size: Optional[float] = None,
        zone: Optional[str] = None,
        autoscaling_policy: Optional[AutoscalingPolicy]=None,
        maintenance_window: Optional[MaintenanceWindow]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if node_template is not None:
                kwargs['node_template'] = node_template
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if initial_size is not None:
                kwargs['initial_size'] = initial_size
            if maintenance_policy is not None:
                kwargs['maintenance_policy'] = maintenance_policy
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if size is not None:
                kwargs['size'] = size
            if zone is not None:
                kwargs['zone'] = zone
            if autoscaling_policy is not None:
                kwargs['autoscaling_policy'] = autoscaling_policy
            if maintenance_window is not None:
                kwargs['maintenance_window'] = maintenance_window
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
