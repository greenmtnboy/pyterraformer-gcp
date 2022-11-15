
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NodeConfigItem():
        zone:str
        # non-optional-blocks
        disk_size_gb: Optional[float] = None
        ip_allocation_policy: Optional[List[Dict[str,Any]]] = None
        machine_type: Optional[str] = None
        network: Optional[str] = None
        oauth_scopes: Optional[Set[str]] = None
        service_account: Optional[str] = None
        subnetwork: Optional[str] = None
        tags: Optional[Set[str]] = None
        
# wrapper list class
class NodeConfig(BlockList):
        items: List[NodeConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrivateEnvironmentConfigItem():
        # non-optional-blocks
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
class ConfigItem():
        # non-optional-blocks
        node_count: Optional[float] = None
        node_config: Optional[NodeConfig]=None,
        private_environment_config: Optional[PrivateEnvironmentConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        
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
        node_config: Optional[NodeConfig]=None,
        private_environment_config: Optional[PrivateEnvironmentConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
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
            if node_config is not None:
                kwargs['node_config'] = node_config
            if private_environment_config is not None:
                kwargs['private_environment_config'] = private_environment_config
            if software_config is not None:
                kwargs['software_config'] = software_config
            if config is not None:
                kwargs['config'] = config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
