
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class LogConfigItem():
        enable:bool
        filter:str
        # non-optional-blocks
        
# wrapper list class
class LogConfig(BlockList):
        items: List[LogConfigItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class SubnetworkItem():
        name:str
        source_ip_ranges_to_nat:Set[str]
        # non-optional-blocks
        secondary_ip_range_names: Optional[Set[str]] = None
        
# wrapper list class
class Subnetwork(BlockSet):
        items: Set[SubnetworkItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleComputeRouterNat(ResourceObject):
    """    
    Args:
        name (str): 
        nat_ip_allocate_option (str): 
        router (str): 
        source_subnetwork_ip_ranges_to_nat (str): 
    """
    _type = 'google_compute_router_nat'
    
    def __init__(self,
        tf_id: str,
        name:str,
        nat_ip_allocate_option:str,
        router:str,
        source_subnetwork_ip_ranges_to_nat:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        icmp_idle_timeout_sec: Optional[float] = None,
        id: Optional[str] = None,
        min_ports_per_vm: Optional[float] = None,
        nat_ips: Optional[Set[str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        tcp_established_idle_timeout_sec: Optional[float] = None,
        tcp_transitory_idle_timeout_sec: Optional[float] = None,
        udp_idle_timeout_sec: Optional[float] = None,
        log_config: Optional[LogConfig]=None,
        subnetwork: Optional[Subnetwork]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if nat_ip_allocate_option is not None:
                kwargs['nat_ip_allocate_option'] = nat_ip_allocate_option
            if router is not None:
                kwargs['router'] = router
            if source_subnetwork_ip_ranges_to_nat is not None:
                kwargs['source_subnetwork_ip_ranges_to_nat'] = source_subnetwork_ip_ranges_to_nat
            if icmp_idle_timeout_sec is not None:
                kwargs['icmp_idle_timeout_sec'] = icmp_idle_timeout_sec
            if id is not None:
                kwargs['id'] = id
            if min_ports_per_vm is not None:
                kwargs['min_ports_per_vm'] = min_ports_per_vm
            if nat_ips is not None:
                kwargs['nat_ips'] = nat_ips
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if tcp_established_idle_timeout_sec is not None:
                kwargs['tcp_established_idle_timeout_sec'] = tcp_established_idle_timeout_sec
            if tcp_transitory_idle_timeout_sec is not None:
                kwargs['tcp_transitory_idle_timeout_sec'] = tcp_transitory_idle_timeout_sec
            if udp_idle_timeout_sec is not None:
                kwargs['udp_idle_timeout_sec'] = udp_idle_timeout_sec
            if log_config is not None:
                kwargs['log_config'] = log_config
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
