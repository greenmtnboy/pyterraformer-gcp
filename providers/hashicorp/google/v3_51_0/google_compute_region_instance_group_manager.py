
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class TargetSizeItem():
        # non-optional-blocks
        fixed: Optional[float] = None
        percent: Optional[float] = None
        
# wrapper list class
class TargetSize(BlockList):
        items: List[TargetSizeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AutoHealingPoliciesItem():
        health_check:str
        initial_delay_sec:float
        # non-optional-blocks
        
# wrapper list class
class AutoHealingPolicies(BlockList):
        items: List[AutoHealingPoliciesItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class NamedPortItem():
        name:str
        port:float
        # non-optional-blocks
        
# wrapper list class
class NamedPort(BlockSet):
        items: Set[NamedPortItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StatefulDiskItem():
        device_name:str
        # non-optional-blocks
        delete_rule: Optional[str] = None
        
# wrapper list class
class StatefulDisk(BlockSet):
        items: Set[StatefulDiskItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class UpdatePolicyItem():
        minimal_action:str
        type:str
        # non-optional-blocks
        instance_redistribution_type: Optional[str] = None
        max_surge_fixed: Optional[float] = None
        max_surge_percent: Optional[float] = None
        max_unavailable_fixed: Optional[float] = None
        max_unavailable_percent: Optional[float] = None
        min_ready_sec: Optional[float] = None
        replacement_method: Optional[str] = None
        
# wrapper list class
class UpdatePolicy(BlockList):
        items: List[UpdatePolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class VersionItem():
        instance_template:str
        # non-optional-blocks
        name: Optional[str] = None
        target_size: Optional[TargetSize]=None,
        
# wrapper list class
class Version(BlockList):
        items: List[VersionItem]




class GoogleComputeRegionInstanceGroupManager(ResourceObject):
    """    
    Args:
        base_instance_name (str): The base instance name to use for instances in this group. The value must be a valid RFC1035 name. Supported characters are lowercase letters, numbers, and hyphens (-). Instances are named by appending a hyphen and a random four-character string to the base instance name.
        name (str): The name of the instance group manager. Must be 1-63 characters long and comply with RFC1035. Supported characters include lowercase letters, numbers, and hyphens.
        region (str): The region where the managed instance group resides.
    """
    _type = 'google_compute_region_instance_group_manager'
    
    def __init__(self,
        tf_id: str,
        base_instance_name:str,
        name:str,
        region:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        distribution_policy_zones: Optional[Set[str]] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        target_pools: Optional[Set[str]] = None,
        target_size: Optional[float] = None,
        wait_for_instances: Optional[bool] = None,
        target_size: Optional[TargetSize]=None,
        auto_healing_policies: Optional[AutoHealingPolicies]=None,
        named_port: Optional[NamedPort]=None,
        stateful_disk: Optional[StatefulDisk]=None,
        timeouts: Optional[Timeouts]=None,
        update_policy: Optional[UpdatePolicy]=None,
        version: Optional[Version]=None,
        ):
            kwargs = {}
            if base_instance_name is not None:
                kwargs['base_instance_name'] = base_instance_name
            if name is not None:
                kwargs['name'] = name
            if region is not None:
                kwargs['region'] = region
            if description is not None:
                kwargs['description'] = description
            if distribution_policy_zones is not None:
                kwargs['distribution_policy_zones'] = distribution_policy_zones
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if target_pools is not None:
                kwargs['target_pools'] = target_pools
            if target_size is not None:
                kwargs['target_size'] = target_size
            if wait_for_instances is not None:
                kwargs['wait_for_instances'] = wait_for_instances
            if target_size is not None:
                kwargs['target_size'] = target_size
            if auto_healing_policies is not None:
                kwargs['auto_healing_policies'] = auto_healing_policies
            if named_port is not None:
                kwargs['named_port'] = named_port
            if stateful_disk is not None:
                kwargs['stateful_disk'] = stateful_disk
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if update_policy is not None:
                kwargs['update_policy'] = update_policy
            if version is not None:
                kwargs['version'] = version
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
