
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
        labels: Optional[Dict[str, str]] = None
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
        kms_key_self_link: Optional[str] = None
        mode: Optional[str] = None
        source: Optional[str] = None
        initialize_params: Optional[InitializeParams]=None,
        
# wrapper list class
class BootDisk(BlockList):
        items: List[BootDiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConfidentialInstanceConfigItem():
        enable_confidential_compute:bool
        # non-optional-blocks
        
# wrapper list class
class ConfidentialInstanceConfig(BlockList):
        items: List[ConfidentialInstanceConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkInterfaceItem():
        # non-optional-blocks
        access_config: Optional[List[Dict[str,Any]]] = None
        alias_ip_range: Optional[List[Dict[str,Any]]] = None
        network: Optional[str] = None
        network_ip: Optional[str] = None
        nic_type: Optional[str] = None
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




# this block can contain multiple items, items in a list are required
@dataclass 
class ShieldedInstanceConfigItem():
        # non-optional-blocks
        enable_integrity_monitoring: Optional[bool] = None
        enable_secure_boot: Optional[bool] = None
        enable_vtpm: Optional[bool] = None
        
# wrapper list class
class ShieldedInstanceConfig(BlockList):
        items: List[ShieldedInstanceConfigItem]




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
        name (str): The name of the instance. One of name or self_link must be provided.
        source_instance_template (str): Name or self link of an instance template to create the instance based on.
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
        desired_status: Optional[str] = None,
        enable_display: Optional[bool] = None,
        guest_accelerator: Optional[List[Dict[str,Any]]] = None,
        hostname: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        machine_type: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        metadata_startup_script: Optional[str] = None,
        min_cpu_platform: Optional[str] = None,
        project: Optional[str] = None,
        resource_policies: Optional[List[str]] = None,
        scratch_disk: Optional[List[Dict[str,Any]]] = None,
        service_account: Optional[List[Dict[str,Any]]] = None,
        tags: Optional[Set[str]] = None,
        zone: Optional[str] = None,
        node_affinities: Optional[NodeAffinities]=None,
        initialize_params: Optional[InitializeParams]=None,
        boot_disk: Optional[BootDisk]=None,
        confidential_instance_config: Optional[ConfidentialInstanceConfig]=None,
        network_interface: Optional[NetworkInterface]=None,
        scheduling: Optional[Scheduling]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
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
            if desired_status is not None:
                kwargs['desired_status'] = desired_status
            if enable_display is not None:
                kwargs['enable_display'] = enable_display
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
            if resource_policies is not None:
                kwargs['resource_policies'] = resource_policies
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
            if confidential_instance_config is not None:
                kwargs['confidential_instance_config'] = confidential_instance_config
            if network_interface is not None:
                kwargs['network_interface'] = network_interface
            if scheduling is not None:
                kwargs['scheduling'] = scheduling
            if shielded_instance_config is not None:
                kwargs['shielded_instance_config'] = shielded_instance_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
