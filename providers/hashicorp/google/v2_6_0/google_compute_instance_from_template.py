
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class NodeAffinitiesItem():
        key:str
        operator:str
        values:Set[str]
        # non-optional-blocks
        
# wrapper list class
class NodeAffinities(BlockSet):
        items: Set[NodeAffinitiesItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class InitializeParamsItem():
        # non-optional-blocks
        image: Optional[str] = None
        size: Optional[float] = None
        type: Optional[str] = None
        
# wrapper list class
class InitializeParams(BlockList):
        items: List[InitializeParamsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BootDiskItem():
        # non-optional-blocks
        auto_delete: Optional[bool] = None
        device_name: Optional[str] = None
        disk_encryption_key_raw: Optional[str] = None
        source: Optional[str] = None
        initialize_params: Optional[InitializeParams]=None,
        
# wrapper list class
class BootDisk(BlockList):
        items: List[BootDiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkInterfaceItem():
        # non-optional-blocks
        access_config: Optional[List[Dict[str,Any]]] = None
        address: Optional[str] = None
        alias_ip_range: Optional[List[Dict[str,Any]]] = None
        network: Optional[str] = None
        network_ip: Optional[str] = None
        subnetwork: Optional[str] = None
        subnetwork_project: Optional[str] = None
        
# wrapper list class
class NetworkInterface(BlockList):
        items: List[NetworkInterfaceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SchedulingItem():
        # non-optional-blocks
        automatic_restart: Optional[bool] = None
        on_host_maintenance: Optional[str] = None
        preemptible: Optional[bool] = None
        node_affinities: Optional[NodeAffinities]=None,
        
# wrapper list class
class Scheduling(BlockList):
        items: List[SchedulingItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeInstanceFromTemplate(ResourceObject):
    """    
    Args:
        name (str): 
        source_instance_template (str): 
    """
    _type = 'google_compute_instance_from_template'
    
    def __init__(self,
        tf_id: str,
        name:str,
        source_instance_template:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        allow_stopping_for_update: Optional[bool] = None,
        attached_disk: Optional[List[Dict[str,Any]]] = None,
        can_ip_forward: Optional[bool] = None,
        deletion_protection: Optional[bool] = None,
        description: Optional[str] = None,
        guest_accelerator: Optional[List[Dict[str,Any]]] = None,
        hostname: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        machine_type: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        metadata_startup_script: Optional[str] = None,
        min_cpu_platform: Optional[str] = None,
        project: Optional[str] = None,
        scratch_disk: Optional[List[Dict[str,Any]]] = None,
        service_account: Optional[List[Dict[str,Any]]] = None,
        tags: Optional[Set[str]] = None,
        zone: Optional[str] = None,
        node_affinities: Optional[NodeAffinities]=None,
        initialize_params: Optional[InitializeParams]=None,
        boot_disk: Optional[BootDisk]=None,
        network_interface: Optional[NetworkInterface]=None,
        scheduling: Optional[Scheduling]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if source_instance_template is not None:
                kwargs['source_instance_template'] = source_instance_template
            if allow_stopping_for_update is not None:
                kwargs['allow_stopping_for_update'] = allow_stopping_for_update
            if attached_disk is not None:
                kwargs['attached_disk'] = attached_disk
            if can_ip_forward is not None:
                kwargs['can_ip_forward'] = can_ip_forward
            if deletion_protection is not None:
                kwargs['deletion_protection'] = deletion_protection
            if description is not None:
                kwargs['description'] = description
            if guest_accelerator is not None:
                kwargs['guest_accelerator'] = guest_accelerator
            if hostname is not None:
                kwargs['hostname'] = hostname
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if machine_type is not None:
                kwargs['machine_type'] = machine_type
            if metadata is not None:
                kwargs['metadata'] = metadata
            if metadata_startup_script is not None:
                kwargs['metadata_startup_script'] = metadata_startup_script
            if min_cpu_platform is not None:
                kwargs['min_cpu_platform'] = min_cpu_platform
            if project is not None:
                kwargs['project'] = project
            if scratch_disk is not None:
                kwargs['scratch_disk'] = scratch_disk
            if service_account is not None:
                kwargs['service_account'] = service_account
            if tags is not None:
                kwargs['tags'] = tags
            if zone is not None:
                kwargs['zone'] = zone
            if node_affinities is not None:
                kwargs['node_affinities'] = node_affinities
            if initialize_params is not None:
                kwargs['initialize_params'] = initialize_params
            if boot_disk is not None:
                kwargs['boot_disk'] = boot_disk
            if network_interface is not None:
                kwargs['network_interface'] = network_interface
            if scheduling is not None:
                kwargs['scheduling'] = scheduling
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
