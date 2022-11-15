
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SchedulerItem():
        # non-optional-blocks
        count: Optional[float] = None
        cpu: Optional[float] = None
        memory_gb: Optional[float] = None
        storage_gb: Optional[float] = None
        
# wrapper list class
class Scheduler(BlockList):
        items: List[SchedulerItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WebServerItem():
        # non-optional-blocks
        cpu: Optional[float] = None
        memory_gb: Optional[float] = None
        storage_gb: Optional[float] = None
        
# wrapper list class
class WebServer(BlockList):
        items: List[WebServerItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkerItem():
        # non-optional-blocks
        cpu: Optional[float] = None
        max_count: Optional[float] = None
        memory_gb: Optional[float] = None
        min_count: Optional[float] = None
        storage_gb: Optional[float] = None
        
# wrapper list class
class Worker(BlockList):
        items: List[WorkerItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class AllowedIpRangeItem():
        value:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class AllowedIpRange(BlockSet):
        items: Set[AllowedIpRangeItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class DatabaseConfigItem():
        machine_type:str
        # non-optional-blocks
        
# wrapper list class
class DatabaseConfig(BlockList):
        items: List[DatabaseConfigItem]




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
class MaintenanceWindowItem():
        end_time:str
        recurrence:str
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class MaintenanceWindow(BlockList):
        items: List[MaintenanceWindowItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NodeConfigItem():
        # non-optional-blocks
        disk_size_gb: Optional[float] = None
        ip_allocation_policy: Optional[List[Dict[str,Any]]] = None
        machine_type: Optional[str] = None
        network: Optional[str] = None
        oauth_scopes: Optional[Set[str]] = None
        service_account: Optional[str] = None
        subnetwork: Optional[str] = None
        tags: Optional[Set[str]] = None
        zone: Optional[str] = None
        
# wrapper list class
class NodeConfig(BlockList):
        items: List[NodeConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrivateEnvironmentConfigItem():
        # non-optional-blocks
        cloud_composer_network_ipv4_cidr_block: Optional[str] = None
        cloud_sql_ipv4_cidr_block: Optional[str] = None
        enable_private_endpoint: Optional[bool] = None
        master_ipv4_cidr_block: Optional[str] = None
        web_server_ipv4_cidr_block: Optional[str] = None
        
# wrapper list class
class PrivateEnvironmentConfig(BlockList):
        items: List[PrivateEnvironmentConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SoftwareConfigItem():
        # non-optional-blocks
        airflow_config_overrides: Optional[Dict[str, str]] = None
        env_variables: Optional[Dict[str, str]] = None
        image_version: Optional[str] = None
        pypi_packages: Optional[Dict[str, str]] = None
        python_version: Optional[str] = None
        scheduler_count: Optional[float] = None
        
# wrapper list class
class SoftwareConfig(BlockList):
        items: List[SoftwareConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WebServerConfigItem():
        machine_type:str
        # non-optional-blocks
        
# wrapper list class
class WebServerConfig(BlockList):
        items: List[WebServerConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WebServerNetworkAccessControlItem():
        # non-optional-blocks
        allowed_ip_range: Optional[AllowedIpRange]=None,
        
# wrapper list class
class WebServerNetworkAccessControl(BlockList):
        items: List[WebServerNetworkAccessControlItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkloadsConfigItem():
        # non-optional-blocks
        scheduler: Optional[Scheduler]=None,
        web_server: Optional[WebServer]=None,
        worker: Optional[Worker]=None,
        
# wrapper list class
class WorkloadsConfig(BlockList):
        items: List[WorkloadsConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigItem():
        # non-optional-blocks
        environment_size: Optional[str] = None
        node_count: Optional[float] = None
        scheduler: Optional[Scheduler]=None,
        web_server: Optional[WebServer]=None,
        worker: Optional[Worker]=None,
        allowed_ip_range: Optional[AllowedIpRange]=None,
        database_config: Optional[DatabaseConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        maintenance_window: Optional[MaintenanceWindow]=None,
        node_config: Optional[NodeConfig]=None,
        private_environment_config: Optional[PrivateEnvironmentConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        web_server_config: Optional[WebServerConfig]=None,
        web_server_network_access_control: Optional[WebServerNetworkAccessControl]=None,
        workloads_config: Optional[WorkloadsConfig]=None,
        
# wrapper list class
class Config(BlockList):
        items: List[ConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComposerEnvironment(ResourceObject):
    """    
    Args:
        name (str): Name of the environment.
    """
    _type = 'google_composer_environment'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        scheduler: Optional[Scheduler]=None,
        web_server: Optional[WebServer]=None,
        worker: Optional[Worker]=None,
        allowed_ip_range: Optional[AllowedIpRange]=None,
        database_config: Optional[DatabaseConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        maintenance_window: Optional[MaintenanceWindow]=None,
        node_config: Optional[NodeConfig]=None,
        private_environment_config: Optional[PrivateEnvironmentConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        web_server_config: Optional[WebServerConfig]=None,
        web_server_network_access_control: Optional[WebServerNetworkAccessControl]=None,
        workloads_config: Optional[WorkloadsConfig]=None,
        config: Optional[Config]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if scheduler is not None:
                kwargs['scheduler'] = scheduler
            if web_server is not None:
                kwargs['web_server'] = web_server
            if worker is not None:
                kwargs['worker'] = worker
            if allowed_ip_range is not None:
                kwargs['allowed_ip_range'] = allowed_ip_range
            if database_config is not None:
                kwargs['database_config'] = database_config
            if encryption_config is not None:
                kwargs['encryption_config'] = encryption_config
            if maintenance_window is not None:
                kwargs['maintenance_window'] = maintenance_window
            if node_config is not None:
                kwargs['node_config'] = node_config
            if private_environment_config is not None:
                kwargs['private_environment_config'] = private_environment_config
            if software_config is not None:
                kwargs['software_config'] = software_config
            if web_server_config is not None:
                kwargs['web_server_config'] = web_server_config
            if web_server_network_access_control is not None:
                kwargs['web_server_network_access_control'] = web_server_network_access_control
            if workloads_config is not None:
                kwargs['workloads_config'] = workloads_config
            if config is not None:
                kwargs['config'] = config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
