
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class AcceleratorsItem():
        accelerator_count:float
        accelerator_type:str
        # non-optional-blocks
        
# wrapper list class
class Accelerators(BlockSet):
        items: Set[AcceleratorsItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class DiskConfigItem():
        # non-optional-blocks
        boot_disk_size_gb: Optional[float] = None
        boot_disk_type: Optional[str] = None
        num_local_ssds: Optional[float] = None
        
# wrapper list class
class DiskConfig(BlockList):
        items: List[DiskConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KerberosConfigItem():
        kms_key_uri:str
        root_principal_password_uri:str
        # non-optional-blocks
        cross_realm_trust_admin_server: Optional[str] = None
        cross_realm_trust_kdc: Optional[str] = None
        cross_realm_trust_realm: Optional[str] = None
        cross_realm_trust_shared_password_uri: Optional[str] = None
        enable_kerberos: Optional[bool] = None
        kdc_db_key_uri: Optional[str] = None
        key_password_uri: Optional[str] = None
        keystore_password_uri: Optional[str] = None
        keystore_uri: Optional[str] = None
        realm: Optional[str] = None
        tgt_lifetime_hours: Optional[float] = None
        truststore_password_uri: Optional[str] = None
        truststore_uri: Optional[str] = None
        
# wrapper list class
class KerberosConfig(BlockList):
        items: List[KerberosConfigItem]




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




# this block can contain multiple items, items in a list are required
@dataclass 
class AutoscalingConfigItem():
        policy_uri:str
        # non-optional-blocks
        
# wrapper list class
class AutoscalingConfig(BlockList):
        items: List[AutoscalingConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EncryptionConfigItem():
        kms_key_name:str
        # non-optional-blocks
        
# wrapper list class
class EncryptionConfig(BlockList):
        items: List[EncryptionConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GceClusterConfigItem():
        # non-optional-blocks
        internal_ip_only: Optional[bool] = None
        metadata: Optional[Dict[str, str]] = None
        network: Optional[str] = None
        service_account: Optional[str] = None
        service_account_scopes: Optional[Set[str]] = None
        subnetwork: Optional[str] = None
        tags: Optional[Set[str]] = None
        zone: Optional[str] = None
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        
# wrapper list class
class GceClusterConfig(BlockList):
        items: List[GceClusterConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InitializationActionItem():
        script:str
        # non-optional-blocks
        timeout_sec: Optional[float] = None
        
# wrapper list class
class InitializationAction(BlockList):
        items: List[InitializationActionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MasterConfigItem():
        # non-optional-blocks
        image_uri: Optional[str] = None
        machine_type: Optional[str] = None
        min_cpu_platform: Optional[str] = None
        num_instances: Optional[float] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        
# wrapper list class
class MasterConfig(BlockList):
        items: List[MasterConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PreemptibleWorkerConfigItem():
        # non-optional-blocks
        num_instances: Optional[float] = None
        disk_config: Optional[DiskConfig]=None,
        
# wrapper list class
class PreemptibleWorkerConfig(BlockList):
        items: List[PreemptibleWorkerConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecurityConfigItem():
        # non-optional-blocks
        kerberos_config: Optional[KerberosConfig]=None,
        
# wrapper list class
class SecurityConfig(BlockList):
        items: List[SecurityConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SoftwareConfigItem():
        # non-optional-blocks
        image_version: Optional[str] = None
        optional_components: Optional[Set[str]] = None
        override_properties: Optional[Dict[str, str]] = None
        
# wrapper list class
class SoftwareConfig(BlockList):
        items: List[SoftwareConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkerConfigItem():
        # non-optional-blocks
        image_uri: Optional[str] = None
        machine_type: Optional[str] = None
        min_cpu_platform: Optional[str] = None
        num_instances: Optional[float] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        
# wrapper list class
class WorkerConfig(BlockList):
        items: List[WorkerConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ClusterConfigItem():
        # non-optional-blocks
        staging_bucket: Optional[str] = None
        temp_bucket: Optional[str] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        kerberos_config: Optional[KerberosConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        autoscaling_config: Optional[AutoscalingConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        gce_cluster_config: Optional[GceClusterConfig]=None,
        initialization_action: Optional[InitializationAction]=None,
        master_config: Optional[MasterConfig]=None,
        preemptible_worker_config: Optional[PreemptibleWorkerConfig]=None,
        security_config: Optional[SecurityConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        worker_config: Optional[WorkerConfig]=None,
        
# wrapper list class
class ClusterConfig(BlockList):
        items: List[ClusterConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataprocCluster(ResourceObject):
    """    
    Args:
        name (str): The name of the cluster, unique within the project and zone.
    """
    _type = 'google_dataproc_cluster'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        graceful_decommission_timeout: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        kerberos_config: Optional[KerberosConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        autoscaling_config: Optional[AutoscalingConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        gce_cluster_config: Optional[GceClusterConfig]=None,
        initialization_action: Optional[InitializationAction]=None,
        master_config: Optional[MasterConfig]=None,
        preemptible_worker_config: Optional[PreemptibleWorkerConfig]=None,
        security_config: Optional[SecurityConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        worker_config: Optional[WorkerConfig]=None,
        cluster_config: Optional[ClusterConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if graceful_decommission_timeout is not None:
                kwargs['graceful_decommission_timeout'] = graceful_decommission_timeout
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if accelerators is not None:
                kwargs['accelerators'] = accelerators
            if disk_config is not None:
                kwargs['disk_config'] = disk_config
            if kerberos_config is not None:
                kwargs['kerberos_config'] = kerberos_config
            if shielded_instance_config is not None:
                kwargs['shielded_instance_config'] = shielded_instance_config
            if autoscaling_config is not None:
                kwargs['autoscaling_config'] = autoscaling_config
            if encryption_config is not None:
                kwargs['encryption_config'] = encryption_config
            if gce_cluster_config is not None:
                kwargs['gce_cluster_config'] = gce_cluster_config
            if initialization_action is not None:
                kwargs['initialization_action'] = initialization_action
            if master_config is not None:
                kwargs['master_config'] = master_config
            if preemptible_worker_config is not None:
                kwargs['preemptible_worker_config'] = preemptible_worker_config
            if security_config is not None:
                kwargs['security_config'] = security_config
            if software_config is not None:
                kwargs['software_config'] = software_config
            if worker_config is not None:
                kwargs['worker_config'] = worker_config
            if cluster_config is not None:
                kwargs['cluster_config'] = cluster_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
