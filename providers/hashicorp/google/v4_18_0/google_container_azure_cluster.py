
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DatabaseEncryptionItem():
        key_id:str
        # non-optional-blocks
        
# wrapper list class
class DatabaseEncryption(BlockList):
        items: List[DatabaseEncryptionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MainVolumeItem():
        # non-optional-blocks
        size_gib: Optional[float] = None
        
# wrapper list class
class MainVolume(BlockList):
        items: List[MainVolumeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ProxyConfigItem():
        resource_group_id:str
        secret_id:str
        # non-optional-blocks
        
# wrapper list class
class ProxyConfig(BlockList):
        items: List[ProxyConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReplicaPlacementsItem():
        azure_availability_zone:str
        subnet_id:str
        # non-optional-blocks
        
# wrapper list class
class ReplicaPlacements(BlockList):
        items: List[ReplicaPlacementsItem]




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
        subnet_id:str
        version:str
        # non-optional-blocks
        tags: Optional[Dict[str, str]] = None
        vm_size: Optional[str] = None
        database_encryption: Optional[DatabaseEncryption]=None,
        main_volume: Optional[MainVolume]=None,
        proxy_config: Optional[ProxyConfig]=None,
        replica_placements: Optional[ReplicaPlacements]=None,
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
        virtual_network_id:str
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




class GoogleContainerAzureCluster(ResourceObject):
    """    
    Args:
        azure_region (str): The Azure region where the cluster runs. Each Google Cloud region supports a subset of nearby Azure regions. You can call to list all supported Azure regions within a given Google Cloud region.
        client (str): Name of the AzureClient. The `AzureClient` resource must reside on the same GCP project and region as the `AzureCluster`. `AzureClient` names are formatted as `projects/<project-number>/locations/<region>/azureClients/<client-id>`. See Resource Names (https:cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names.
        location (str): The location for the resource
        name (str): The name of this resource.
        resource_group_id (str): The ARM ID of the resource group where the cluster resources are deployed. For example: `/subscriptions/*/resourceGroups/*`
    """
    _type = 'google_container_azure_cluster'
    
    def __init__(self,
        tf_id: str,
        azure_region:str,
        client:str,
        location:str,
        name:str,
        resource_group_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        annotations: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        database_encryption: Optional[DatabaseEncryption]=None,
        main_volume: Optional[MainVolume]=None,
        proxy_config: Optional[ProxyConfig]=None,
        replica_placements: Optional[ReplicaPlacements]=None,
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
            if azure_region is not None:
                kwargs['azure_region'] = azure_region
            if client is not None:
                kwargs['client'] = client
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if resource_group_id is not None:
                kwargs['resource_group_id'] = resource_group_id
            if annotations is not None:
                kwargs['annotations'] = annotations
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if database_encryption is not None:
                kwargs['database_encryption'] = database_encryption
            if main_volume is not None:
                kwargs['main_volume'] = main_volume
            if proxy_config is not None:
                kwargs['proxy_config'] = proxy_config
            if replica_placements is not None:
                kwargs['replica_placements'] = replica_placements
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
            
        
        
