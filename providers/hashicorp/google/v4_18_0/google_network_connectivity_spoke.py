
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class InstancesItem():
        # non-optional-blocks
        ip_address: Optional[str] = None
        virtual_machine: Optional[str] = None
        
# wrapper list class
class Instances(BlockList):
        items: List[InstancesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LinkedInterconnectAttachmentsItem():
        site_to_site_data_transfer:bool
        uris:List[str]
        # non-optional-blocks
        
# wrapper list class
class LinkedInterconnectAttachments(BlockList):
        items: List[LinkedInterconnectAttachmentsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LinkedRouterApplianceInstancesItem():
        site_to_site_data_transfer:bool
        # non-optional-blocks
        instances: Optional[Instances]=None,
        
# wrapper list class
class LinkedRouterApplianceInstances(BlockList):
        items: List[LinkedRouterApplianceInstancesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LinkedVpnTunnelsItem():
        site_to_site_data_transfer:bool
        uris:List[str]
        # non-optional-blocks
        
# wrapper list class
class LinkedVpnTunnels(BlockList):
        items: List[LinkedVpnTunnelsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleNetworkConnectivitySpoke(ResourceObject):
    """    
    Args:
        hub (str): Immutable. The URI of the hub that this spoke is attached to.
        location (str): The location for the resource
        name (str): Immutable. The name of the spoke. Spoke names must be unique.
    """
    _type = 'google_network_connectivity_spoke'
    
    def __init__(self,
        tf_id: str,
        hub:str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        instances: Optional[Instances]=None,
        linked_interconnect_attachments: Optional[LinkedInterconnectAttachments]=None,
        linked_router_appliance_instances: Optional[LinkedRouterApplianceInstances]=None,
        linked_vpn_tunnels: Optional[LinkedVpnTunnels]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if hub is not None:
                kwargs['hub'] = hub
            if location is not None:
                kwargs['location'] = location
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
            if instances is not None:
                kwargs['instances'] = instances
            if linked_interconnect_attachments is not None:
                kwargs['linked_interconnect_attachments'] = linked_interconnect_attachments
            if linked_router_appliance_instances is not None:
                kwargs['linked_router_appliance_instances'] = linked_router_appliance_instances
            if linked_vpn_tunnels is not None:
                kwargs['linked_vpn_tunnels'] = linked_vpn_tunnels
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
