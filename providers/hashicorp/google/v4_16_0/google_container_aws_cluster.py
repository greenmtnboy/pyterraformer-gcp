
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AwsServicesAuthenticationItem():
        role_arn:str
        # non-optional-blocks
        role_session_name: Optional[str] = None
        
# wrapper list class
class AwsServicesAuthentication(BlockList):
        items: List[AwsServicesAuthenticationItem]




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
class DatabaseEncryptionItem():
        kms_key_arn:str
        # non-optional-blocks
        
# wrapper list class
class DatabaseEncryption(BlockList):
        items: List[DatabaseEncryptionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MainVolumeItem():
        # non-optional-blocks
        iops: Optional[float] = None
        kms_key_arn: Optional[str] = None
        size_gib: Optional[float] = None
        volume_type: Optional[str] = None
        
# wrapper list class
class MainVolume(BlockList):
        items: List[MainVolumeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ProxyConfigItem():
        secret_arn:str
        secret_version:str
        # non-optional-blocks
        
# wrapper list class
class ProxyConfig(BlockList):
        items: List[ProxyConfigItem]




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
class AdminUsersItem():
        username:str
        # non-optional-blocks
        
# wrapper list class
class AdminUsers(BlockList):
        items: List[AdminUsersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AuthorizationItem():
        # non-optional-blocks
        admin_users: Optional[AdminUsers]=None,
        
# wrapper list class
class Authorization(BlockList):
        items: List[AuthorizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ControlPlaneItem():
        iam_instance_profile:str
        subnet_ids:List[str]
        version:str
        # non-optional-blocks
        instance_type: Optional[str] = None
        security_group_ids: Optional[List[str]] = None
        tags: Optional[Dict[str, str]] = None
        aws_services_authentication: Optional[AwsServicesAuthentication]=None,
        config_encryption: Optional[ConfigEncryption]=None,
        database_encryption: Optional[DatabaseEncryption]=None,
        main_volume: Optional[MainVolume]=None,
        proxy_config: Optional[ProxyConfig]=None,
        root_volume: Optional[RootVolume]=None,
        ssh_config: Optional[SshConfig]=None,
        
# wrapper list class
class ControlPlane(BlockList):
        items: List[ControlPlaneItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FleetItem():
        # non-optional-blocks
        project: Optional[str] = None
        
# wrapper list class
class Fleet(BlockList):
        items: List[FleetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkingItem():
        pod_address_cidr_blocks:List[str]
        service_address_cidr_blocks:List[str]
        vpc_id:str
        # non-optional-blocks
        
# wrapper list class
class Networking(BlockList):
        items: List[NetworkingItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleContainerAwsCluster(ResourceObject):
    """    
    Args:
        aws_region (str): The AWS region where the cluster runs. Each Google Cloud region supports a subset of nearby AWS regions. You can call to list all supported AWS regions within a given Google Cloud region.
        location (str): The location for the resource
        name (str): The name of this resource.
    """
    _type = 'google_container_aws_cluster'
    
    def __init__(self,
        tf_id: str,
        aws_region:str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        annotations: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        aws_services_authentication: Optional[AwsServicesAuthentication]=None,
        config_encryption: Optional[ConfigEncryption]=None,
        database_encryption: Optional[DatabaseEncryption]=None,
        main_volume: Optional[MainVolume]=None,
        proxy_config: Optional[ProxyConfig]=None,
        root_volume: Optional[RootVolume]=None,
        ssh_config: Optional[SshConfig]=None,
        admin_users: Optional[AdminUsers]=None,
        authorization: Optional[Authorization]=None,
        control_plane: Optional[ControlPlane]=None,
        fleet: Optional[Fleet]=None,
        networking: Optional[Networking]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if aws_region is not None:
                kwargs['aws_region'] = aws_region
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if annotations is not None:
                kwargs['annotations'] = annotations
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if aws_services_authentication is not None:
                kwargs['aws_services_authentication'] = aws_services_authentication
            if config_encryption is not None:
                kwargs['config_encryption'] = config_encryption
            if database_encryption is not None:
                kwargs['database_encryption'] = database_encryption
            if main_volume is not None:
                kwargs['main_volume'] = main_volume
            if proxy_config is not None:
                kwargs['proxy_config'] = proxy_config
            if root_volume is not None:
                kwargs['root_volume'] = root_volume
            if ssh_config is not None:
                kwargs['ssh_config'] = ssh_config
            if admin_users is not None:
                kwargs['admin_users'] = admin_users
            if authorization is not None:
                kwargs['authorization'] = authorization
            if control_plane is not None:
                kwargs['control_plane'] = control_plane
            if fleet is not None:
                kwargs['fleet'] = fleet
            if networking is not None:
                kwargs['networking'] = networking
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
