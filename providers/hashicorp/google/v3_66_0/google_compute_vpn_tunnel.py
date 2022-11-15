
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




class GoogleComputeVpnTunnel(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. The name must be 1-63 characters long, and
                    comply with RFC1035. Specifically, the name must be 1-63
                    characters long and match the regular expression
                    '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character
                    must be a lowercase letter, and all following characters must
                    be a dash, lowercase letter, or digit,
                    except the last character, which cannot be a dash.
        shared_secret (str): Shared secret used to set the secure session between the Cloud VPN
                    gateway and the peer VPN gateway.
    """
    _type = 'google_compute_vpn_tunnel'
    
    def __init__(self,
        tf_id: str,
        name:str,
        shared_secret:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ike_version: Optional[float] = None,
        local_traffic_selector: Optional[Set[str]] = None,
        peer_external_gateway: Optional[str] = None,
        peer_external_gateway_interface: Optional[float] = None,
        peer_gcp_gateway: Optional[str] = None,
        peer_ip: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        remote_traffic_selector: Optional[Set[str]] = None,
        router: Optional[str] = None,
        target_vpn_gateway: Optional[str] = None,
        vpn_gateway: Optional[str] = None,
        vpn_gateway_interface: Optional[float] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if shared_secret is not None:
                kwargs['shared_secret'] = shared_secret
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ike_version is not None:
                kwargs['ike_version'] = ike_version
            if local_traffic_selector is not None:
                kwargs['local_traffic_selector'] = local_traffic_selector
            if peer_external_gateway is not None:
                kwargs['peer_external_gateway'] = peer_external_gateway
            if peer_external_gateway_interface is not None:
                kwargs['peer_external_gateway_interface'] = peer_external_gateway_interface
            if peer_gcp_gateway is not None:
                kwargs['peer_gcp_gateway'] = peer_gcp_gateway
            if peer_ip is not None:
                kwargs['peer_ip'] = peer_ip
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if remote_traffic_selector is not None:
                kwargs['remote_traffic_selector'] = remote_traffic_selector
            if router is not None:
                kwargs['router'] = router
            if target_vpn_gateway is not None:
                kwargs['target_vpn_gateway'] = target_vpn_gateway
            if vpn_gateway is not None:
                kwargs['vpn_gateway'] = vpn_gateway
            if vpn_gateway_interface is not None:
                kwargs['vpn_gateway_interface'] = vpn_gateway_interface
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
