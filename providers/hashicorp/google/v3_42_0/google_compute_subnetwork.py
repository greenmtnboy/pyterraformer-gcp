
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
        filter_expr: Optional[str] = None
        flow_sampling: Optional[float] = None
        metadata: Optional[str] = None
        metadata_fields: Optional[Set[str]] = None
        
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
        ip_cidr_range (str): The range of internal addresses that are owned by this subnetwork.
                    Provide this property when you create the subnetwork. For example,
                    10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and
                    non-overlapping within a network. Only IPv4 is supported.
        name (str): The name of the resource, provided by the client when initially
                    creating the resource. The name must be 1-63 characters long, and
                    comply with RFC1035. Specifically, the name must be 1-63 characters
                    long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which
                    means the first character must be a lowercase letter, and all
                    following characters must be a dash, lowercase letter, or digit,
                    except the last character, which cannot be a dash.
        network (str): The network this subnet belongs to.
                    Only networks that are in the distributed mode can have subnetworks.
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
            
        
        
