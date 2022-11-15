
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class AuthorizedNetworksItem():
        value:str
        # non-optional-blocks
        expiration_time: Optional[str] = None
        name: Optional[str] = None
        
# wrapper list class
class AuthorizedNetworks(BlockSet):
        items: Set[AuthorizedNetworksItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class BackupConfigurationItem():
        # non-optional-blocks
        binary_log_enabled: Optional[bool] = None
        enabled: Optional[bool] = None
        location: Optional[str] = None
        point_in_time_recovery_enabled: Optional[bool] = None
        start_time: Optional[str] = None
        
# wrapper list class
class BackupConfiguration(BlockList):
        items: List[BackupConfigurationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DatabaseFlagsItem():
        name:str
        value:str
        # non-optional-blocks
        
# wrapper list class
class DatabaseFlags(BlockList):
        items: List[DatabaseFlagsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IpConfigurationItem():
        # non-optional-blocks
        ipv4_enabled: Optional[bool] = None
        private_network: Optional[str] = None
        require_ssl: Optional[bool] = None
        authorized_networks: Optional[AuthorizedNetworks]=None,
        
# wrapper list class
class IpConfiguration(BlockList):
        items: List[IpConfigurationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LocationPreferenceItem():
        # non-optional-blocks
        follow_gae_application: Optional[str] = None
        zone: Optional[str] = None
        
# wrapper list class
class LocationPreference(BlockList):
        items: List[LocationPreferenceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaintenanceWindowItem():
        # non-optional-blocks
        day: Optional[float] = None
        hour: Optional[float] = None
        update_track: Optional[str] = None
        
# wrapper list class
class MaintenanceWindow(BlockList):
        items: List[MaintenanceWindowItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReplicaConfigurationItem():
        # non-optional-blocks
        ca_certificate: Optional[str] = None
        client_certificate: Optional[str] = None
        client_key: Optional[str] = None
        connect_retry_interval: Optional[float] = None
        dump_file_path: Optional[str] = None
        failover_target: Optional[bool] = None
        master_heartbeat_period: Optional[float] = None
        password: Optional[str] = None
        ssl_cipher: Optional[str] = None
        username: Optional[str] = None
        verify_server_certificate: Optional[bool] = None
        
# wrapper list class
class ReplicaConfiguration(BlockList):
        items: List[ReplicaConfigurationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SettingsItem():
        tier:str
        # non-optional-blocks
        activation_policy: Optional[str] = None
        authorized_gae_applications: Optional[List[str]] = None
        availability_type: Optional[str] = None
        crash_safe_replication: Optional[bool] = None
        disk_autoresize: Optional[bool] = None
        disk_size: Optional[float] = None
        disk_type: Optional[str] = None
        pricing_plan: Optional[str] = None
        replication_type: Optional[str] = None
        user_labels: Optional[Dict[str, str]] = None
        authorized_networks: Optional[AuthorizedNetworks]=None,
        backup_configuration: Optional[BackupConfiguration]=None,
        database_flags: Optional[DatabaseFlags]=None,
        ip_configuration: Optional[IpConfiguration]=None,
        location_preference: Optional[LocationPreference]=None,
        maintenance_window: Optional[MaintenanceWindow]=None,
        
# wrapper list class
class Settings(BlockList):
        items: List[SettingsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleSqlDatabaseInstance(ResourceObject):
    """    
    Args:
    """
    _type = 'google_sql_database_instance'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        database_version: Optional[str] = None,
        id: Optional[str] = None,
        master_instance_name: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        root_password: Optional[str] = None,
        authorized_networks: Optional[AuthorizedNetworks]=None,
        backup_configuration: Optional[BackupConfiguration]=None,
        database_flags: Optional[DatabaseFlags]=None,
        ip_configuration: Optional[IpConfiguration]=None,
        location_preference: Optional[LocationPreference]=None,
        maintenance_window: Optional[MaintenanceWindow]=None,
        replica_configuration: Optional[ReplicaConfiguration]=None,
        settings: Optional[Settings]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if database_version is not None:
                kwargs['database_version'] = database_version
            if id is not None:
                kwargs['id'] = id
            if master_instance_name is not None:
                kwargs['master_instance_name'] = master_instance_name
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if root_password is not None:
                kwargs['root_password'] = root_password
            if authorized_networks is not None:
                kwargs['authorized_networks'] = authorized_networks
            if backup_configuration is not None:
                kwargs['backup_configuration'] = backup_configuration
            if database_flags is not None:
                kwargs['database_flags'] = database_flags
            if ip_configuration is not None:
                kwargs['ip_configuration'] = ip_configuration
            if location_preference is not None:
                kwargs['location_preference'] = location_preference
            if maintenance_window is not None:
                kwargs['maintenance_window'] = maintenance_window
            if replica_configuration is not None:
                kwargs['replica_configuration'] = replica_configuration
            if settings is not None:
                kwargs['settings'] = settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
