
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
class AccessConfigItem():
        # non-optional-blocks
        nat_ip: Optional[str] = None
        network_tier: Optional[str] = None
        public_ptr_domain_name: Optional[str] = None
        
# wrapper list class
class AccessConfig(BlockList):
        items: List[AccessConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AliasIpRangeItem():
        ip_cidr_range:str
        # non-optional-blocks
        subnetwork_range_name: Optional[str] = None
        
# wrapper list class
class AliasIpRange(BlockList):
        items: List[AliasIpRangeItem]




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
class AttachedDiskItem():
        source:str
        # non-optional-blocks
        device_name: Optional[str] = None
        disk_encryption_key_raw: Optional[str] = None
        kms_key_self_link: Optional[str] = None
        mode: Optional[str] = None
        
# wrapper list class
class AttachedDisk(BlockList):
        items: List[AttachedDiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BootDiskItem():
        # non-optional-blocks
        auto_delete: Optional[bool] = None
        device_name: Optional[str] = None
        disk_encryption_key_raw: Optional[str] = None
        kms_key_self_link: Optional[str] = None
        source: Optional[str] = None
        initialize_params: Optional[InitializeParams]=None,
        
# wrapper list class
class BootDisk(BlockList):
        items: List[BootDiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DiskItem():
        # non-optional-blocks
        auto_delete: Optional[bool] = None
        device_name: Optional[str] = None
        disk: Optional[str] = None
        disk_encryption_key_raw: Optional[str] = None
        image: Optional[str] = None
        scratch: Optional[bool] = None
        size: Optional[float] = None
        type: Optional[str] = None
        
# wrapper list class
class Disk(BlockList):
        items: List[DiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkInterfaceItem():
        # non-optional-blocks
        address: Optional[str] = None
        network: Optional[str] = None
        network_ip: Optional[str] = None
        subnetwork: Optional[str] = None
        subnetwork_project: Optional[str] = None
        access_config: Optional[AccessConfig]=None,
        alias_ip_range: Optional[AliasIpRange]=None,
        
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
class ScratchDiskItem():
        # non-optional-blocks
        interface: Optional[str] = None
        
# wrapper list class
class ScratchDisk(BlockList):
        items: List[ScratchDiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ServiceAccountItem():
        scopes:Set[str]
        # non-optional-blocks
        email: Optional[str] = None
        
# wrapper list class
class ServiceAccount(BlockList):
        items: List[ServiceAccountItem]




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




class GoogleComputeInstance(ResourceObject):
    """    
    Args:
        machine_type (str): 
        name (str): 
    """
    _type = 'google_compute_instance'
    
    def __init__(self,
        tf_id: str,
        machine_type:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        allow_stopping_for_update: Optional[bool] = None,
        can_ip_forward: Optional[bool] = None,
        deletion_protection: Optional[bool] = None,
        description: Optional[str] = None,
        guest_accelerator: Optional[List[Dict[str,Any]]] = None,
        hostname: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        metadata_startup_script: Optional[str] = None,
        min_cpu_platform: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[Set[str]] = None,
        zone: Optional[str] = None,
        node_affinities: Optional[NodeAffinities]=None,
        access_config: Optional[AccessConfig]=None,
        alias_ip_range: Optional[AliasIpRange]=None,
        initialize_params: Optional[InitializeParams]=None,
        attached_disk: Optional[AttachedDisk]=None,
        boot_disk: Optional[BootDisk]=None,
        disk: Optional[Disk]=None,
        network_interface: Optional[NetworkInterface]=None,
        scheduling: Optional[Scheduling]=None,
        scratch_disk: Optional[ScratchDisk]=None,
        service_account: Optional[ServiceAccount]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if machine_type is not None:
                kwargs['machine_type'] = machine_type
            if name is not None:
                kwargs['name'] = name
            if allow_stopping_for_update is not None:
                kwargs['allow_stopping_for_update'] = allow_stopping_for_update
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
            if metadata is not None:
                kwargs['metadata'] = metadata
            if metadata_startup_script is not None:
                kwargs['metadata_startup_script'] = metadata_startup_script
            if min_cpu_platform is not None:
                kwargs['min_cpu_platform'] = min_cpu_platform
            if project is not None:
                kwargs['project'] = project
            if tags is not None:
                kwargs['tags'] = tags
            if zone is not None:
                kwargs['zone'] = zone
            if node_affinities is not None:
                kwargs['node_affinities'] = node_affinities
            if access_config is not None:
                kwargs['access_config'] = access_config
            if alias_ip_range is not None:
                kwargs['alias_ip_range'] = alias_ip_range
            if initialize_params is not None:
                kwargs['initialize_params'] = initialize_params
            if attached_disk is not None:
                kwargs['attached_disk'] = attached_disk
            if boot_disk is not None:
                kwargs['boot_disk'] = boot_disk
            if disk is not None:
                kwargs['disk'] = disk
            if network_interface is not None:
                kwargs['network_interface'] = network_interface
            if scheduling is not None:
                kwargs['scheduling'] = scheduling
            if scratch_disk is not None:
                kwargs['scratch_disk'] = scratch_disk
            if service_account is not None:
                kwargs['service_account'] = service_account
            if shielded_instance_config is not None:
                kwargs['shielded_instance_config'] = shielded_instance_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
