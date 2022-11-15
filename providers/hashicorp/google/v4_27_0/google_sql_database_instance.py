
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
class BackupRetentionSettingsItem():
        retained_backups:float
        # non-optional-blocks
        retention_unit: Optional[str] = None
        
# wrapper list class
class BackupRetentionSettings(BlockList):
        items: List[BackupRetentionSettingsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ActiveDirectoryConfigItem():
        domain:str
        # non-optional-blocks
        
# wrapper list class
class ActiveDirectoryConfig(BlockList):
        items: List[ActiveDirectoryConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BackupConfigurationItem():
        # non-optional-blocks
        binary_log_enabled: Optional[bool] = None
        enabled: Optional[bool] = None
        location: Optional[str] = None
        point_in_time_recovery_enabled: Optional[bool] = None
        start_time: Optional[str] = None
        transaction_log_retention_days: Optional[float] = None
        backup_retention_settings: Optional[BackupRetentionSettings]=None,
        
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
class InsightsConfigItem():
        # non-optional-blocks
        query_insights_enabled: Optional[bool] = None
        query_string_length: Optional[float] = None
        record_application_tags: Optional[bool] = None
        record_client_address: Optional[bool] = None
        
# wrapper list class
class InsightsConfig(BlockList):
        items: List[InsightsConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IpConfigurationItem():
        # non-optional-blocks
        allocated_ip_range: Optional[str] = None
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
class CloneItem():
        source_instance_name:str
        # non-optional-blocks
        allocated_ip_range: Optional[str] = None
        point_in_time: Optional[str] = None
        
# wrapper list class
class Clone(BlockList):
        items: List[CloneItem]




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
class RestoreBackupContextItem():
        backup_run_id:float
        # non-optional-blocks
        instance_id: Optional[str] = None
        project: Optional[str] = None
        
# wrapper list class
class RestoreBackupContext(BlockList):
        items: List[RestoreBackupContextItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SettingsItem():
        tier:str
        # non-optional-blocks
        activation_policy: Optional[str] = None
        availability_type: Optional[str] = None
        collation: Optional[str] = None
        disk_autoresize: Optional[bool] = None
        disk_autoresize_limit: Optional[float] = None
        disk_size: Optional[float] = None
        disk_type: Optional[str] = None
        pricing_plan: Optional[str] = None
        user_labels: Optional[Dict[str, str]] = None
        authorized_networks: Optional[AuthorizedNetworks]=None,
        backup_retention_settings: Optional[BackupRetentionSettings]=None,
        active_directory_config: Optional[ActiveDirectoryConfig]=None,
        backup_configuration: Optional[BackupConfiguration]=None,
        database_flags: Optional[DatabaseFlags]=None,
        insights_config: Optional[InsightsConfig]=None,
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
        database_version (str): The MySQL, PostgreSQL or SQL Server (beta) version to use. Supported values include MYSQL_5_6, MYSQL_5_7, MYSQL_8_0, POSTGRES_9_6, POSTGRES_10, POSTGRES_11, POSTGRES_12, POSTGRES_13, POSTGRES_14, SQLSERVER_2017_STANDARD, SQLSERVER_2017_ENTERPRISE, SQLSERVER_2017_EXPRESS, SQLSERVER_2017_WEB. Database Version Policies includes an up-to-date reference of supported versions.
    """
    _type = 'google_sql_database_instance'
    
    def __init__(self,
        tf_id: str,
        database_version:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        deletion_protection: Optional[bool] = None,
        id: Optional[str] = None,
        master_instance_name: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        root_password: Optional[str] = None,
        authorized_networks: Optional[AuthorizedNetworks]=None,
        backup_retention_settings: Optional[BackupRetentionSettings]=None,
        active_directory_config: Optional[ActiveDirectoryConfig]=None,
        backup_configuration: Optional[BackupConfiguration]=None,
        database_flags: Optional[DatabaseFlags]=None,
        insights_config: Optional[InsightsConfig]=None,
        ip_configuration: Optional[IpConfiguration]=None,
        location_preference: Optional[LocationPreference]=None,
        maintenance_window: Optional[MaintenanceWindow]=None,
        clone: Optional[Clone]=None,
        replica_configuration: Optional[ReplicaConfiguration]=None,
        restore_backup_context: Optional[RestoreBackupContext]=None,
        settings: Optional[Settings]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if database_version is not None:
                kwargs['database_version'] = database_version
            if deletion_protection is not None:
                kwargs['deletion_protection'] = deletion_protection
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
            if backup_retention_settings is not None:
                kwargs['backup_retention_settings'] = backup_retention_settings
            if active_directory_config is not None:
                kwargs['active_directory_config'] = active_directory_config
            if backup_configuration is not None:
                kwargs['backup_configuration'] = backup_configuration
            if database_flags is not None:
                kwargs['database_flags'] = database_flags
            if insights_config is not None:
                kwargs['insights_config'] = insights_config
            if ip_configuration is not None:
                kwargs['ip_configuration'] = ip_configuration
            if location_preference is not None:
                kwargs['location_preference'] = location_preference
            if maintenance_window is not None:
                kwargs['maintenance_window'] = maintenance_window
            if clone is not None:
                kwargs['clone'] = clone
            if replica_configuration is not None:
                kwargs['replica_configuration'] = replica_configuration
            if restore_backup_context is not None:
                kwargs['restore_backup_context'] = restore_backup_context
            if settings is not None:
                kwargs['settings'] = settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
