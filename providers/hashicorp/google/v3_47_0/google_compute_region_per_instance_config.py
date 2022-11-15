
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class DiskItem():
        device_name:str
        source:str
        # non-optional-blocks
        delete_rule: Optional[str] = None
        mode: Optional[str] = None
        
# wrapper list class
class Disk(BlockSet):
        items: Set[DiskItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class PreservedStateItem():
        # non-optional-blocks
        metadata: Optional[Dict[str, str]] = None
        disk: Optional[Disk]=None,
        
# wrapper list class
class PreservedState(BlockList):
        items: List[PreservedStateItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRegionPerInstanceConfig(ResourceObject):
    """    
    Args:
        name (str): The name for this per-instance config and its corresponding instance.
        region (str): Region where the containing instance group manager is located
        region_instance_group_manager (str): The region instance group manager this instance config is part of.
    """
    _type = 'google_compute_region_per_instance_config'
    
    def __init__(self,
        tf_id: str,
        name:str,
        region:str,
        region_instance_group_manager:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        minimal_action: Optional[str] = None,
        most_disruptive_allowed_action: Optional[str] = None,
        project: Optional[str] = None,
        remove_instance_state_on_destroy: Optional[bool] = None,
        disk: Optional[Disk]=None,
        preserved_state: Optional[PreservedState]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if region is not None:
                kwargs['region'] = region
            if region_instance_group_manager is not None:
                kwargs['region_instance_group_manager'] = region_instance_group_manager
            if id is not None:
                kwargs['id'] = id
            if minimal_action is not None:
                kwargs['minimal_action'] = minimal_action
            if most_disruptive_allowed_action is not None:
                kwargs['most_disruptive_allowed_action'] = most_disruptive_allowed_action
            if project is not None:
                kwargs['project'] = project
            if remove_instance_state_on_destroy is not None:
                kwargs['remove_instance_state_on_destroy'] = remove_instance_state_on_destroy
            if disk is not None:
                kwargs['disk'] = disk
            if preserved_state is not None:
                kwargs['preserved_state'] = preserved_state
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
