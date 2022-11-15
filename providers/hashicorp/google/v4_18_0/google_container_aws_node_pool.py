
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigEncryptionItem():
        kms_key_arn:str
        # non-optional-blocks
        
# wrapper list class
class ConfigEncryption(BlockList):
        items: List[ConfigEncryptionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RootVolumeItem():
        # non-optional-blocks
        iops: Optional[float] = None
        kms_key_arn: Optional[str] = None
        size_gib: Optional[float] = None
        volume_type: Optional[str] = None
        
# wrapper list class
class RootVolume(BlockList):
        items: List[RootVolumeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SshConfigItem():
        ec2_key_pair:str
        # non-optional-blocks
        
# wrapper list class
class SshConfig(BlockList):
        items: List[SshConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TaintsItem():
        effect:str
        key:str
        value:str
        # non-optional-blocks
        
# wrapper list class
class Taints(BlockList):
        items: List[TaintsItem]




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
        iam_instance_profile:str
        # non-optional-blocks
        instance_type: Optional[str] = None
        labels: Optional[Dict[str, str]] = None
        security_group_ids: Optional[List[str]] = None
        tags: Optional[Dict[str, str]] = None
        config_encryption: Optional[ConfigEncryption]=None,
        root_volume: Optional[RootVolume]=None,
        ssh_config: Optional[SshConfig]=None,
        taints: Optional[Taints]=None,
        
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




class GoogleContainerAwsNodePool(ResourceObject):
    """    
    Args:
        cluster (str): The awsCluster for the resource
        location (str): The location for the resource
        name (str): The name of this resource.
        subnet_id (str): The subnet where the node pool node run.
        version (str): The Kubernetes version to run on this node pool (e.g. `1.19.10-gke.1000`). You can list all supported versions on a given Google Cloud region by calling GetAwsServerConfig.
    """
    _type = 'google_container_aws_node_pool'
    
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
        id: Optional[str] = None,
        project: Optional[str] = None,
        config_encryption: Optional[ConfigEncryption]=None,
        root_volume: Optional[RootVolume]=None,
        ssh_config: Optional[SshConfig]=None,
        taints: Optional[Taints]=None,
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
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if config_encryption is not None:
                kwargs['config_encryption'] = config_encryption
            if root_volume is not None:
                kwargs['root_volume'] = root_volume
            if ssh_config is not None:
                kwargs['ssh_config'] = ssh_config
            if taints is not None:
                kwargs['taints'] = taints
            if autoscaling is not None:
                kwargs['autoscaling'] = autoscaling
            if config is not None:
                kwargs['config'] = config
            if max_pods_constraint is not None:
                kwargs['max_pods_constraint'] = max_pods_constraint
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
