
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class LogConfigItem():
        # non-optional-blocks
        aggregation_interval: Optional[str] = None
        flow_sampling: Optional[float] = None
        metadata: Optional[str] = None
        
# wrapper list class
class LogConfig(BlockList):
        items: List[LogConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeSubnetwork(ResourceObject):
    """    
    Args:
        ip_cidr_range (str): 
        name (str): 
        network (str): 
    """
    _type = 'google_compute_subnetwork'
    
    def __init__(self,
        tf_id: str,
        ip_cidr_range:str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        enable_flow_logs: Optional[bool] = None,
        id: Optional[str] = None,
        private_ip_google_access: Optional[bool] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        secondary_ip_range: Optional[List[Dict[str,Any]]] = None,
        log_config: Optional[LogConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if ip_cidr_range is not None:
                kwargs['ip_cidr_range'] = ip_cidr_range
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if description is not None:
                kwargs['description'] = description
            if enable_flow_logs is not None:
                kwargs['enable_flow_logs'] = enable_flow_logs
            if id is not None:
                kwargs['id'] = id
            if private_ip_google_access is not None:
                kwargs['private_ip_google_access'] = private_ip_google_access
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if secondary_ip_range is not None:
                kwargs['secondary_ip_range'] = secondary_ip_range
            if log_config is not None:
                kwargs['log_config'] = log_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
