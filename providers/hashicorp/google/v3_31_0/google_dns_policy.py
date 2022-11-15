
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class TargetNameServersItem():
        ipv4_address:str
        # non-optional-blocks
        
# wrapper list class
class TargetNameServers(BlockSet):
        items: Set[TargetNameServersItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class AlternativeNameServerConfigItem():
        # non-optional-blocks
        target_name_servers: Optional[TargetNameServers]=None,
        
# wrapper list class
class AlternativeNameServerConfig(BlockList):
        items: List[AlternativeNameServerConfigItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class NetworksItem():
        network_url:str
        # non-optional-blocks
        
# wrapper list class
class Networks(BlockSet):
        items: Set[NetworksItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDnsPolicy(ResourceObject):
    """    
    Args:
        name (str): User assigned name for this policy.
    """
    _type = 'google_dns_policy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        enable_inbound_forwarding: Optional[bool] = None,
        enable_logging: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        target_name_servers: Optional[TargetNameServers]=None,
        alternative_name_server_config: Optional[AlternativeNameServerConfig]=None,
        networks: Optional[Networks]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if enable_inbound_forwarding is not None:
                kwargs['enable_inbound_forwarding'] = enable_inbound_forwarding
            if enable_logging is not None:
                kwargs['enable_logging'] = enable_logging
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if target_name_servers is not None:
                kwargs['target_name_servers'] = target_name_servers
            if alternative_name_server_config is not None:
                kwargs['alternative_name_server_config'] = alternative_name_server_config
            if networks is not None:
                kwargs['networks'] = networks
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
