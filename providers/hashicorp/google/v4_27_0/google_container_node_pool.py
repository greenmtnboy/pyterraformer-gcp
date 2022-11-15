
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GcfsConfigItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class GcfsConfig(BlockList):
        items: List[GcfsConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GvnicItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class Gvnic(BlockList):
        items: List[GvnicItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ShieldedInstanceConfigItem():
        # non-optional-blocks
        enable_integrity_monitoring: Optional[bool] = None
        enable_secure_boot: Optional[bool] = None
        
# wrapper list class
class ShieldedInstanceConfig(BlockList):
        items: List[ShieldedInstanceConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkloadMetadataConfigItem():
        mode:str
        # non-optional-blocks
        
# wrapper list class
class WorkloadMetadataConfig(BlockList):
        items: List[WorkloadMetadataConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AutoscalingItem():
        max_node_count:float
        min_node_count:float
        # non-optional-blocks
        
# wrapper list class
class Autoscaling(BlockList):
        items: List[AutoscalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ManagementItem():
        # non-optional-blocks
        auto_repair: Optional[bool] = None
        auto_upgrade: Optional[bool] = None
        
# wrapper list class
class Management(BlockList):
        items: List[ManagementItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NodeConfigItem():
        # non-optional-blocks
        boot_disk_kms_key: Optional[str] = None
        disk_size_gb: Optional[float] = None
        disk_type: Optional[str] = None
        guest_accelerator: Optional[List[Dict[str,Any]]] = None
        image_type: Optional[str] = None
        labels: Optional[Dict[str, str]] = None
        local_ssd_count: Optional[float] = None
        machine_type: Optional[str] = None
        metadata: Optional[Dict[str, str]] = None
        min_cpu_platform: Optional[str] = None
        node_group: Optional[str] = None
        oauth_scopes: Optional[Set[str]] = None
        preemptible: Optional[bool] = None
        service_account: Optional[str] = None
        spot: Optional[bool] = None
        tags: Optional[List[str]] = None
        taint: Optional[List[Dict[str,Any]]] = None
        gcfs_config: Optional[GcfsConfig]=None,
        gvnic: Optional[Gvnic]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        
# wrapper list class
class NodeConfig(BlockList):
        items: List[NodeConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class UpgradeSettingsItem():
        max_surge:float
        max_unavailable:float
        # non-optional-blocks
        
# wrapper list class
class UpgradeSettings(BlockList):
        items: List[UpgradeSettingsItem]




class GoogleContainerNodePool(ResourceObject):
    """    
    Args:
        cluster (str): The cluster to create the node pool for. Cluster must be present in location provided for zonal clusters.
    """
    _type = 'google_container_node_pool'
    
    def __init__(self,
        tf_id: str,
        cluster:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        initial_node_count: Optional[float] = None,
        location: Optional[str] = None,
        max_pods_per_node: Optional[float] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        node_count: Optional[float] = None,
        node_locations: Optional[Set[str]] = None,
        project: Optional[str] = None,
        version: Optional[str] = None,
        gcfs_config: Optional[GcfsConfig]=None,
        gvnic: Optional[Gvnic]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        autoscaling: Optional[Autoscaling]=None,
        management: Optional[Management]=None,
        node_config: Optional[NodeConfig]=None,
        timeouts: Optional[Timeouts]=None,
        upgrade_settings: Optional[UpgradeSettings]=None,
        ):
            kwargs = {}
            if cluster is not None:
                kwargs['cluster'] = cluster
            if id is not None:
                kwargs['id'] = id
            if initial_node_count is not None:
                kwargs['initial_node_count'] = initial_node_count
            if location is not None:
                kwargs['location'] = location
            if max_pods_per_node is not None:
                kwargs['max_pods_per_node'] = max_pods_per_node
            if name is not None:
                kwargs['name'] = name
            if name_prefix is not None:
                kwargs['name_prefix'] = name_prefix
            if node_count is not None:
                kwargs['node_count'] = node_count
            if node_locations is not None:
                kwargs['node_locations'] = node_locations
            if project is not None:
                kwargs['project'] = project
            if version is not None:
                kwargs['version'] = version
            if gcfs_config is not None:
                kwargs['gcfs_config'] = gcfs_config
            if gvnic is not None:
                kwargs['gvnic'] = gvnic
            if shielded_instance_config is not None:
                kwargs['shielded_instance_config'] = shielded_instance_config
            if workload_metadata_config is not None:
                kwargs['workload_metadata_config'] = workload_metadata_config
            if autoscaling is not None:
                kwargs['autoscaling'] = autoscaling
            if management is not None:
                kwargs['management'] = management
            if node_config is not None:
                kwargs['node_config'] = node_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if upgrade_settings is not None:
                kwargs['upgrade_settings'] = upgrade_settings
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
