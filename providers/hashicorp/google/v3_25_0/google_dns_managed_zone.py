
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworksItem():
        network_url:str
        # non-optional-blocks
        
# wrapper list class
class Networks(BlockSet):
        items: Set[NetworksItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class TargetNetworkItem():
        network_url:str
        # non-optional-blocks
        
# wrapper list class
class TargetNetwork(BlockList):
        items: List[TargetNetworkItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class TargetNameServersItem():
        ipv4_address:str
        # non-optional-blocks
        forwarding_path: Optional[str] = None
        
# wrapper list class
class TargetNameServers(BlockSet):
        items: Set[TargetNameServersItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class DefaultKeySpecsItem():
        # non-optional-blocks
        algorithm: Optional[str] = None
        key_length: Optional[float] = None
        key_type: Optional[str] = None
        kind: Optional[str] = None
        
# wrapper list class
class DefaultKeySpecs(BlockList):
        items: List[DefaultKeySpecsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DnssecConfigItem():
        # non-optional-blocks
        kind: Optional[str] = None
        non_existence: Optional[str] = None
        state: Optional[str] = None
        default_key_specs: Optional[DefaultKeySpecs]=None,
        
# wrapper list class
class DnssecConfig(BlockList):
        items: List[DnssecConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ForwardingConfigItem():
        # non-optional-blocks
        target_name_servers: Optional[TargetNameServers]=None,
        
# wrapper list class
class ForwardingConfig(BlockList):
        items: List[ForwardingConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PeeringConfigItem():
        # non-optional-blocks
        target_network: Optional[TargetNetwork]=None,
        
# wrapper list class
class PeeringConfig(BlockList):
        items: List[PeeringConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrivateVisibilityConfigItem():
        # non-optional-blocks
        networks: Optional[Networks]=None,
        
# wrapper list class
class PrivateVisibilityConfig(BlockList):
        items: List[PrivateVisibilityConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDnsManagedZone(ResourceObject):
    """    
    Args:
        dns_name (str): The DNS name of this managed zone, for instance "example.com.".
        name (str): User assigned name for this resource.
                    Must be unique within the project.
    """
    _type = 'google_dns_managed_zone'
    
    def __init__(self,
        tf_id: str,
        dns_name:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        visibility: Optional[str] = None,
        networks: Optional[Networks]=None,
        target_network: Optional[TargetNetwork]=None,
        target_name_servers: Optional[TargetNameServers]=None,
        default_key_specs: Optional[DefaultKeySpecs]=None,
        dnssec_config: Optional[DnssecConfig]=None,
        forwarding_config: Optional[ForwardingConfig]=None,
        peering_config: Optional[PeeringConfig]=None,
        private_visibility_config: Optional[PrivateVisibilityConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dns_name is not None:
                kwargs['dns_name'] = dns_name
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if visibility is not None:
                kwargs['visibility'] = visibility
            if networks is not None:
                kwargs['networks'] = networks
            if target_network is not None:
                kwargs['target_network'] = target_network
            if target_name_servers is not None:
                kwargs['target_name_servers'] = target_name_servers
            if default_key_specs is not None:
                kwargs['default_key_specs'] = default_key_specs
            if dnssec_config is not None:
                kwargs['dnssec_config'] = dnssec_config
            if forwarding_config is not None:
                kwargs['forwarding_config'] = forwarding_config
            if peering_config is not None:
                kwargs['peering_config'] = peering_config
            if private_visibility_config is not None:
                kwargs['private_visibility_config'] = private_visibility_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
