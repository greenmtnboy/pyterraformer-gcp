
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
        update: Optional[str] = None




class GoogleComputeForwardingRule(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_compute_forwarding_rule'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        all_ports: Optional[bool] = None,
        backend_service: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ip_address: Optional[str] = None,
        ip_protocol: Optional[str] = None,
        ip_version: Optional[str] = None,
        load_balancing_scheme: Optional[str] = None,
        network: Optional[str] = None,
        network_tier: Optional[str] = None,
        port_range: Optional[str] = None,
        ports: Optional[Set[str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        service_label: Optional[str] = None,
        subnetwork: Optional[str] = None,
        target: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if all_ports is not None:
                kwargs['all_ports'] = all_ports
            if backend_service is not None:
                kwargs['backend_service'] = backend_service
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ip_address is not None:
                kwargs['ip_address'] = ip_address
            if ip_protocol is not None:
                kwargs['ip_protocol'] = ip_protocol
            if ip_version is not None:
                kwargs['ip_version'] = ip_version
            if load_balancing_scheme is not None:
                kwargs['load_balancing_scheme'] = load_balancing_scheme
            if network is not None:
                kwargs['network'] = network
            if network_tier is not None:
                kwargs['network_tier'] = network_tier
            if port_range is not None:
                kwargs['port_range'] = port_range
            if ports is not None:
                kwargs['ports'] = ports
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if service_label is not None:
                kwargs['service_label'] = service_label
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if target is not None:
                kwargs['target'] = target
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
