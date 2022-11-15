
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class Layer4ConfigsItem():
        ip_protocol:str
        # non-optional-blocks
        ports: Optional[List[str]] = None
        
# wrapper list class
class Layer4Configs(BlockList):
        items: List[Layer4ConfigsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MatchItem():
        # non-optional-blocks
        dest_ip_ranges: Optional[List[str]] = None
        src_ip_ranges: Optional[List[str]] = None
        layer4_configs: Optional[Layer4Configs]=None,
        
# wrapper list class
class Match(BlockList):
        items: List[MatchItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeFirewallPolicyRule(ResourceObject):
    """    
    Args:
        action (str): 
        direction (str): 
        firewall_policy (str): 
        priority (float): 
    """
    _type = 'google_compute_firewall_policy_rule'
    
    def __init__(self,
        tf_id: str,
        action:str,
        direction:str,
        firewall_policy:str,
        priority:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        enable_logging: Optional[bool] = None,
        id: Optional[str] = None,
        target_resources: Optional[List[str]] = None,
        target_service_accounts: Optional[List[str]] = None,
        layer4_configs: Optional[Layer4Configs]=None,
        match: Optional[Match]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if action is not None:
                kwargs['action'] = action
            if direction is not None:
                kwargs['direction'] = direction
            if firewall_policy is not None:
                kwargs['firewall_policy'] = firewall_policy
            if priority is not None:
                kwargs['priority'] = priority
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if enable_logging is not None:
                kwargs['enable_logging'] = enable_logging
            if id is not None:
                kwargs['id'] = id
            if target_resources is not None:
                kwargs['target_resources'] = target_resources
            if target_service_accounts is not None:
                kwargs['target_service_accounts'] = target_service_accounts
            if layer4_configs is not None:
                kwargs['layer4_configs'] = layer4_configs
            if match is not None:
                kwargs['match'] = match
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
