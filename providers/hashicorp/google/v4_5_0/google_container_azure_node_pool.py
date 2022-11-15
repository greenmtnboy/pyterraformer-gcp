
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class RootVolumeItem():
        # non-optional-blocks
        size_gib: Optional[float] = None
        
# wrapper list class
class RootVolume(BlockList):
        items: List[RootVolumeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SshConfigItem():
        authorized_key:str
        # non-optional-blocks
        
# wrapper list class
class SshConfig(BlockList):
        items: List[SshConfigItem]




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
class ConfigItem():
        # non-optional-blocks
        tags: Optional[Dict[str, str]] = None
        vm_size: Optional[str] = None
        root_volume: Optional[RootVolume]=None,
        ssh_config: Optional[SshConfig]=None,
        
# wrapper list class
class Config(BlockList):
        items: List[ConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaxPodsConstraintItem():
        max_pods_per_node:float
        # non-optional-blocks
        
# wrapper list class
class MaxPodsConstraint(BlockList):
        items: List[MaxPodsConstraintItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleContainerAzureNodePool(ResourceObject):
    """    
    Args:
        cluster (str): The azureCluster for the resource
        location (str): The location for the resource
        name (str): The name of this resource.
        subnet_id (str): Required. The ARM ID of the subnet where the node pool VMs run. Make sure it's a subnet under the virtual network in the cluster configuration.
        version (str): Required. The Kubernetes version (e.g. `1.19.10-gke.1000`) running on this node pool.
    """
    _type = 'google_container_azure_node_pool'
    
    def __init__(self,
        tf_id: str,
        cluster:str,
        location:str,
        name:str,
        subnet_id:str,
        version:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        annotations: Optional[Dict[str, str]] = None,
        azure_availability_zone: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        root_volume: Optional[RootVolume]=None,
        ssh_config: Optional[SshConfig]=None,
        autoscaling: Optional[Autoscaling]=None,
        config: Optional[Config]=None,
        max_pods_constraint: Optional[MaxPodsConstraint]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if cluster is not None:
                kwargs['cluster'] = cluster
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if subnet_id is not None:
                kwargs['subnet_id'] = subnet_id
            if version is not None:
                kwargs['version'] = version
            if annotations is not None:
                kwargs['annotations'] = annotations
            if azure_availability_zone is not None:
                kwargs['azure_availability_zone'] = azure_availability_zone
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if root_volume is not None:
                kwargs['root_volume'] = root_volume
            if ssh_config is not None:
                kwargs['ssh_config'] = ssh_config
            if autoscaling is not None:
                kwargs['autoscaling'] = autoscaling
            if config is not None:
                kwargs['config'] = config
            if max_pods_constraint is not None:
                kwargs['max_pods_constraint'] = max_pods_constraint
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
