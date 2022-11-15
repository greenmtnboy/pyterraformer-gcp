
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class VpnInterfacesItem():
        # non-optional-blocks
        id: Optional[float] = None
        interconnect_attachment: Optional[str] = None
        
# wrapper list class
class VpnInterfaces(BlockList):
        items: List[VpnInterfacesItem]




class GoogleComputeHaVpnGateway(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035.  Specifically, the name must be 1-63 characters long and
                    match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means
                    the first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
        network (str): The network this VPN gateway is accepting traffic for.
    """
    _type = 'google_compute_ha_vpn_gateway'
    
    def __init__(self,
        tf_id: str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        vpn_interfaces: Optional[VpnInterfaces]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if vpn_interfaces is not None:
                kwargs['vpn_interfaces'] = vpn_interfaces
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
