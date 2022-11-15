
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
class DiskEncryptionKeyItem():
        # non-optional-blocks
        kms_key_self_link: Optional[str] = None
        
# wrapper list class
class DiskEncryptionKey(BlockList):
        items: List[DiskEncryptionKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DiskItem():
        # non-optional-blocks
        auto_delete: Optional[bool] = None
        boot: Optional[bool] = None
        device_name: Optional[str] = None
        disk_name: Optional[str] = None
        disk_size_gb: Optional[float] = None
        disk_type: Optional[str] = None
        interface: Optional[str] = None
        labels: Optional[Dict[str, str]] = None
        mode: Optional[str] = None
        source: Optional[str] = None
        source_image: Optional[str] = None
        type: Optional[str] = None
        disk_encryption_key: Optional[DiskEncryptionKey]=None,
        
# wrapper list class
class Disk(BlockList):
        items: List[DiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GuestAcceleratorItem():
        count:float
        type:str
        # non-optional-blocks
        
# wrapper list class
class GuestAccelerator(BlockList):
        items: List[GuestAcceleratorItem]




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




class GoogleComputeInstanceTemplate(ResourceObject):
    """    
    Args:
        machine_type (str): 
    """
    _type = 'google_compute_instance_template'
    
    def __init__(self,
        tf_id: str,
        machine_type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        automatic_restart: Optional[bool] = None,
        can_ip_forward: Optional[bool] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        instance_description: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        metadata_startup_script: Optional[str] = None,
        min_cpu_platform: Optional[str] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        on_host_maintenance: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        tags: Optional[Set[str]] = None,
        node_affinities: Optional[NodeAffinities]=None,
        access_config: Optional[AccessConfig]=None,
        alias_ip_range: Optional[AliasIpRange]=None,
        disk_encryption_key: Optional[DiskEncryptionKey]=None,
        disk: Optional[Disk]=None,
        guest_accelerator: Optional[GuestAccelerator]=None,
        network_interface: Optional[NetworkInterface]=None,
        scheduling: Optional[Scheduling]=None,
        service_account: Optional[ServiceAccount]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        ):
            kwargs = {}
            if machine_type is not None:
                kwargs['machine_type'] = machine_type
            if automatic_restart is not None:
                kwargs['automatic_restart'] = automatic_restart
            if can_ip_forward is not None:
                kwargs['can_ip_forward'] = can_ip_forward
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if instance_description is not None:
                kwargs['instance_description'] = instance_description
            if labels is not None:
                kwargs['labels'] = labels
            if metadata is not None:
                kwargs['metadata'] = metadata
            if metadata_startup_script is not None:
                kwargs['metadata_startup_script'] = metadata_startup_script
            if min_cpu_platform is not None:
                kwargs['min_cpu_platform'] = min_cpu_platform
            if name is not None:
                kwargs['name'] = name
            if name_prefix is not None:
                kwargs['name_prefix'] = name_prefix
            if on_host_maintenance is not None:
                kwargs['on_host_maintenance'] = on_host_maintenance
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if tags is not None:
                kwargs['tags'] = tags
            if node_affinities is not None:
                kwargs['node_affinities'] = node_affinities
            if access_config is not None:
                kwargs['access_config'] = access_config
            if alias_ip_range is not None:
                kwargs['alias_ip_range'] = alias_ip_range
            if disk_encryption_key is not None:
                kwargs['disk_encryption_key'] = disk_encryption_key
            if disk is not None:
                kwargs['disk'] = disk
            if guest_accelerator is not None:
                kwargs['guest_accelerator'] = guest_accelerator
            if network_interface is not None:
                kwargs['network_interface'] = network_interface
            if scheduling is not None:
                kwargs['scheduling'] = scheduling
            if service_account is not None:
                kwargs['service_account'] = service_account
            if shielded_instance_config is not None:
                kwargs['shielded_instance_config'] = shielded_instance_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
