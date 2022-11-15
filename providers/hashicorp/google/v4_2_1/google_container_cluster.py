
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class BigqueryDestinationItem():
        dataset_id:str
        # non-optional-blocks
        
# wrapper list class
class BigqueryDestination(BlockList):
        items: List[BigqueryDestinationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MasterGlobalAccessConfigItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class MasterGlobalAccessConfig(BlockList):
        items: List[MasterGlobalAccessConfigItem]




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
        disk_size_gb: Optional[float] = None
        disk_type: Optional[str] = None
        guest_accelerator: Optional[List[Dict[str,Any]]] = None
        image_type: Optional[str] = None
        labels: Optional[Dict[str, str]] = None
        local_ssd_count: Optional[float] = None
        machine_type: Optional[str] = None
        metadata: Optional[Dict[str, str]] = None
        min_cpu_platform: Optional[str] = None
        oauth_scopes: Optional[Set[str]] = None
        preemptible: Optional[bool] = None
        service_account: Optional[str] = None
        tags: Optional[List[str]] = None
        taint: Optional[List[Dict[str,Any]]] = None
        gcfs_config: Optional[GcfsConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        
# wrapper list class
class NodeConfig(BlockList):
        items: List[NodeConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UpgradeSettingsItem():
        max_surge:float
        max_unavailable:float
        # non-optional-blocks
        
# wrapper list class
class UpgradeSettings(BlockList):
        items: List[UpgradeSettingsItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class CidrBlocksItem():
        cidr_block:str
        # non-optional-blocks
        display_name: Optional[str] = None
        
# wrapper list class
class CidrBlocks(BlockSet):
        items: Set[CidrBlocksItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class ClientCertificateConfigItem():
        issue_client_certificate:bool
        # non-optional-blocks
        
# wrapper list class
class ClientCertificateConfig(BlockList):
        items: List[ClientCertificateConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DailyMaintenanceWindowItem():
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class DailyMaintenanceWindow(BlockList):
        items: List[DailyMaintenanceWindowItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class MaintenanceExclusionItem():
        end_time:str
        exclusion_name:str
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class MaintenanceExclusion(BlockSet):
        items: Set[MaintenanceExclusionItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class RecurringWindowItem():
        end_time:str
        recurrence:str
        start_time:str
        # non-optional-blocks
        
# wrapper list class
class RecurringWindow(BlockList):
        items: List[RecurringWindowItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AutoProvisioningDefaultsItem():
        # non-optional-blocks
        oauth_scopes: Optional[List[str]] = None
        service_account: Optional[str] = None
        
# wrapper list class
class AutoProvisioningDefaults(BlockList):
        items: List[AutoProvisioningDefaultsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourceLimitsItem():
        resource_type:str
        # non-optional-blocks
        maximum: Optional[float] = None
        minimum: Optional[float] = None
        
# wrapper list class
class ResourceLimits(BlockList):
        items: List[ResourceLimitsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudrunConfigItem():
        disabled:bool
        # non-optional-blocks
        load_balancer_type: Optional[str] = None
        
# wrapper list class
class CloudrunConfig(BlockList):
        items: List[CloudrunConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HorizontalPodAutoscalingItem():
        disabled:bool
        # non-optional-blocks
        
# wrapper list class
class HorizontalPodAutoscaling(BlockList):
        items: List[HorizontalPodAutoscalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpLoadBalancingItem():
        disabled:bool
        # non-optional-blocks
        
# wrapper list class
class HttpLoadBalancing(BlockList):
        items: List[HttpLoadBalancingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkPolicyConfigItem():
        disabled:bool
        # non-optional-blocks
        
# wrapper list class
class NetworkPolicyConfig(BlockList):
        items: List[NetworkPolicyConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AddonsConfigItem():
        # non-optional-blocks
        cloudrun_config: Optional[CloudrunConfig]=None,
        horizontal_pod_autoscaling: Optional[HorizontalPodAutoscaling]=None,
        http_load_balancing: Optional[HttpLoadBalancing]=None,
        network_policy_config: Optional[NetworkPolicyConfig]=None,
        
# wrapper list class
class AddonsConfig(BlockList):
        items: List[AddonsConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AuthenticatorGroupsConfigItem():
        security_group:str
        # non-optional-blocks
        
# wrapper list class
class AuthenticatorGroupsConfig(BlockList):
        items: List[AuthenticatorGroupsConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ClusterAutoscalingItem():
        enabled:bool
        # non-optional-blocks
        auto_provisioning_defaults: Optional[AutoProvisioningDefaults]=None,
        resource_limits: Optional[ResourceLimits]=None,
        
# wrapper list class
class ClusterAutoscaling(BlockList):
        items: List[ClusterAutoscalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConfidentialNodesItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class ConfidentialNodes(BlockList):
        items: List[ConfidentialNodesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DatabaseEncryptionItem():
        state:str
        # non-optional-blocks
        key_name: Optional[str] = None
        
# wrapper list class
class DatabaseEncryption(BlockList):
        items: List[DatabaseEncryptionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DefaultSnatStatusItem():
        disabled:bool
        # non-optional-blocks
        
# wrapper list class
class DefaultSnatStatus(BlockList):
        items: List[DefaultSnatStatusItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IpAllocationPolicyItem():
        # non-optional-blocks
        cluster_ipv4_cidr_block: Optional[str] = None
        cluster_secondary_range_name: Optional[str] = None
        services_ipv4_cidr_block: Optional[str] = None
        services_secondary_range_name: Optional[str] = None
        
# wrapper list class
class IpAllocationPolicy(BlockList):
        items: List[IpAllocationPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LoggingConfigItem():
        enable_components:List[str]
        # non-optional-blocks
        
# wrapper list class
class LoggingConfig(BlockList):
        items: List[LoggingConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaintenancePolicyItem():
        # non-optional-blocks
        daily_maintenance_window: Optional[DailyMaintenanceWindow]=None,
        maintenance_exclusion: Optional[MaintenanceExclusion]=None,
        recurring_window: Optional[RecurringWindow]=None,
        
# wrapper list class
class MaintenancePolicy(BlockList):
        items: List[MaintenancePolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MasterAuthItem():
        # non-optional-blocks
        client_certificate_config: Optional[ClientCertificateConfig]=None,
        
# wrapper list class
class MasterAuth(BlockList):
        items: List[MasterAuthItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MasterAuthorizedNetworksConfigItem():
        # non-optional-blocks
        cidr_blocks: Optional[CidrBlocks]=None,
        
# wrapper list class
class MasterAuthorizedNetworksConfig(BlockList):
        items: List[MasterAuthorizedNetworksConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MonitoringConfigItem():
        enable_components:List[str]
        # non-optional-blocks
        
# wrapper list class
class MonitoringConfig(BlockList):
        items: List[MonitoringConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkPolicyItem():
        enabled:bool
        # non-optional-blocks
        provider: Optional[str] = None
        
# wrapper list class
class NetworkPolicy(BlockList):
        items: List[NetworkPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NodePoolItem():
        # non-optional-blocks
        initial_node_count: Optional[float] = None
        max_pods_per_node: Optional[float] = None
        name: Optional[str] = None
        name_prefix: Optional[str] = None
        node_count: Optional[float] = None
        node_locations: Optional[Set[str]] = None
        version: Optional[str] = None
        gcfs_config: Optional[GcfsConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        autoscaling: Optional[Autoscaling]=None,
        management: Optional[Management]=None,
        node_config: Optional[NodeConfig]=None,
        upgrade_settings: Optional[UpgradeSettings]=None,
        
# wrapper list class
class NodePool(BlockList):
        items: List[NodePoolItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrivateClusterConfigItem():
        enable_private_endpoint:bool
        # non-optional-blocks
        enable_private_nodes: Optional[bool] = None
        master_ipv4_cidr_block: Optional[str] = None
        master_global_access_config: Optional[MasterGlobalAccessConfig]=None,
        
# wrapper list class
class PrivateClusterConfig(BlockList):
        items: List[PrivateClusterConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReleaseChannelItem():
        channel:str
        # non-optional-blocks
        
# wrapper list class
class ReleaseChannel(BlockList):
        items: List[ReleaseChannelItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourceUsageExportConfigItem():
        # non-optional-blocks
        enable_network_egress_metering: Optional[bool] = None
        enable_resource_consumption_metering: Optional[bool] = None
        bigquery_destination: Optional[BigqueryDestination]=None,
        
# wrapper list class
class ResourceUsageExportConfig(BlockList):
        items: List[ResourceUsageExportConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        read: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class VerticalPodAutoscalingItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class VerticalPodAutoscaling(BlockList):
        items: List[VerticalPodAutoscalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkloadIdentityConfigItem():
        # non-optional-blocks
        workload_pool: Optional[str] = None
        
# wrapper list class
class WorkloadIdentityConfig(BlockList):
        items: List[WorkloadIdentityConfigItem]




class GoogleContainerCluster(ResourceObject):
    """    
    Args:
        name (str): The name of the cluster, unique within the project and location.
    """
    _type = 'google_container_cluster'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        cluster_ipv4_cidr: Optional[str] = None,
        datapath_provider: Optional[str] = None,
        default_max_pods_per_node: Optional[float] = None,
        description: Optional[str] = None,
        enable_autopilot: Optional[bool] = None,
        enable_binary_authorization: Optional[bool] = None,
        enable_intranode_visibility: Optional[bool] = None,
        enable_kubernetes_alpha: Optional[bool] = None,
        enable_legacy_abac: Optional[bool] = None,
        enable_shielded_nodes: Optional[bool] = None,
        enable_tpu: Optional[bool] = None,
        id: Optional[str] = None,
        initial_node_count: Optional[float] = None,
        location: Optional[str] = None,
        logging_service: Optional[str] = None,
        min_master_version: Optional[str] = None,
        monitoring_service: Optional[str] = None,
        network: Optional[str] = None,
        networking_mode: Optional[str] = None,
        node_locations: Optional[Set[str]] = None,
        node_version: Optional[str] = None,
        private_ipv6_google_access: Optional[str] = None,
        project: Optional[str] = None,
        remove_default_node_pool: Optional[bool] = None,
        resource_labels: Optional[Dict[str, str]] = None,
        subnetwork: Optional[str] = None,
        bigquery_destination: Optional[BigqueryDestination]=None,
        master_global_access_config: Optional[MasterGlobalAccessConfig]=None,
        gcfs_config: Optional[GcfsConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        autoscaling: Optional[Autoscaling]=None,
        management: Optional[Management]=None,
        node_config: Optional[NodeConfig]=None,
        upgrade_settings: Optional[UpgradeSettings]=None,
        cidr_blocks: Optional[CidrBlocks]=None,
        client_certificate_config: Optional[ClientCertificateConfig]=None,
        daily_maintenance_window: Optional[DailyMaintenanceWindow]=None,
        maintenance_exclusion: Optional[MaintenanceExclusion]=None,
        recurring_window: Optional[RecurringWindow]=None,
        auto_provisioning_defaults: Optional[AutoProvisioningDefaults]=None,
        resource_limits: Optional[ResourceLimits]=None,
        cloudrun_config: Optional[CloudrunConfig]=None,
        horizontal_pod_autoscaling: Optional[HorizontalPodAutoscaling]=None,
        http_load_balancing: Optional[HttpLoadBalancing]=None,
        network_policy_config: Optional[NetworkPolicyConfig]=None,
        addons_config: Optional[AddonsConfig]=None,
        authenticator_groups_config: Optional[AuthenticatorGroupsConfig]=None,
        cluster_autoscaling: Optional[ClusterAutoscaling]=None,
        confidential_nodes: Optional[ConfidentialNodes]=None,
        database_encryption: Optional[DatabaseEncryption]=None,
        default_snat_status: Optional[DefaultSnatStatus]=None,
        ip_allocation_policy: Optional[IpAllocationPolicy]=None,
        logging_config: Optional[LoggingConfig]=None,
        maintenance_policy: Optional[MaintenancePolicy]=None,
        master_auth: Optional[MasterAuth]=None,
        master_authorized_networks_config: Optional[MasterAuthorizedNetworksConfig]=None,
        monitoring_config: Optional[MonitoringConfig]=None,
        network_policy: Optional[NetworkPolicy]=None,
        node_pool: Optional[NodePool]=None,
        private_cluster_config: Optional[PrivateClusterConfig]=None,
        release_channel: Optional[ReleaseChannel]=None,
        resource_usage_export_config: Optional[ResourceUsageExportConfig]=None,
        timeouts: Optional[Timeouts]=None,
        vertical_pod_autoscaling: Optional[VerticalPodAutoscaling]=None,
        workload_identity_config: Optional[WorkloadIdentityConfig]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if cluster_ipv4_cidr is not None:
                kwargs['cluster_ipv4_cidr'] = cluster_ipv4_cidr
            if datapath_provider is not None:
                kwargs['datapath_provider'] = datapath_provider
            if default_max_pods_per_node is not None:
                kwargs['default_max_pods_per_node'] = default_max_pods_per_node
            if description is not None:
                kwargs['description'] = description
            if enable_autopilot is not None:
                kwargs['enable_autopilot'] = enable_autopilot
            if enable_binary_authorization is not None:
                kwargs['enable_binary_authorization'] = enable_binary_authorization
            if enable_intranode_visibility is not None:
                kwargs['enable_intranode_visibility'] = enable_intranode_visibility
            if enable_kubernetes_alpha is not None:
                kwargs['enable_kubernetes_alpha'] = enable_kubernetes_alpha
            if enable_legacy_abac is not None:
                kwargs['enable_legacy_abac'] = enable_legacy_abac
            if enable_shielded_nodes is not None:
                kwargs['enable_shielded_nodes'] = enable_shielded_nodes
            if enable_tpu is not None:
                kwargs['enable_tpu'] = enable_tpu
            if id is not None:
                kwargs['id'] = id
            if initial_node_count is not None:
                kwargs['initial_node_count'] = initial_node_count
            if location is not None:
                kwargs['location'] = location
            if logging_service is not None:
                kwargs['logging_service'] = logging_service
            if min_master_version is not None:
                kwargs['min_master_version'] = min_master_version
            if monitoring_service is not None:
                kwargs['monitoring_service'] = monitoring_service
            if network is not None:
                kwargs['network'] = network
            if networking_mode is not None:
                kwargs['networking_mode'] = networking_mode
            if node_locations is not None:
                kwargs['node_locations'] = node_locations
            if node_version is not None:
                kwargs['node_version'] = node_version
            if private_ipv6_google_access is not None:
                kwargs['private_ipv6_google_access'] = private_ipv6_google_access
            if project is not None:
                kwargs['project'] = project
            if remove_default_node_pool is not None:
                kwargs['remove_default_node_pool'] = remove_default_node_pool
            if resource_labels is not None:
                kwargs['resource_labels'] = resource_labels
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if bigquery_destination is not None:
                kwargs['bigquery_destination'] = bigquery_destination
            if master_global_access_config is not None:
                kwargs['master_global_access_config'] = master_global_access_config
            if gcfs_config is not None:
                kwargs['gcfs_config'] = gcfs_config
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
            if upgrade_settings is not None:
                kwargs['upgrade_settings'] = upgrade_settings
            if cidr_blocks is not None:
                kwargs['cidr_blocks'] = cidr_blocks
            if client_certificate_config is not None:
                kwargs['client_certificate_config'] = client_certificate_config
            if daily_maintenance_window is not None:
                kwargs['daily_maintenance_window'] = daily_maintenance_window
            if maintenance_exclusion is not None:
                kwargs['maintenance_exclusion'] = maintenance_exclusion
            if recurring_window is not None:
                kwargs['recurring_window'] = recurring_window
            if auto_provisioning_defaults is not None:
                kwargs['auto_provisioning_defaults'] = auto_provisioning_defaults
            if resource_limits is not None:
                kwargs['resource_limits'] = resource_limits
            if cloudrun_config is not None:
                kwargs['cloudrun_config'] = cloudrun_config
            if horizontal_pod_autoscaling is not None:
                kwargs['horizontal_pod_autoscaling'] = horizontal_pod_autoscaling
            if http_load_balancing is not None:
                kwargs['http_load_balancing'] = http_load_balancing
            if network_policy_config is not None:
                kwargs['network_policy_config'] = network_policy_config
            if addons_config is not None:
                kwargs['addons_config'] = addons_config
            if authenticator_groups_config is not None:
                kwargs['authenticator_groups_config'] = authenticator_groups_config
            if cluster_autoscaling is not None:
                kwargs['cluster_autoscaling'] = cluster_autoscaling
            if confidential_nodes is not None:
                kwargs['confidential_nodes'] = confidential_nodes
            if database_encryption is not None:
                kwargs['database_encryption'] = database_encryption
            if default_snat_status is not None:
                kwargs['default_snat_status'] = default_snat_status
            if ip_allocation_policy is not None:
                kwargs['ip_allocation_policy'] = ip_allocation_policy
            if logging_config is not None:
                kwargs['logging_config'] = logging_config
            if maintenance_policy is not None:
                kwargs['maintenance_policy'] = maintenance_policy
            if master_auth is not None:
                kwargs['master_auth'] = master_auth
            if master_authorized_networks_config is not None:
                kwargs['master_authorized_networks_config'] = master_authorized_networks_config
            if monitoring_config is not None:
                kwargs['monitoring_config'] = monitoring_config
            if network_policy is not None:
                kwargs['network_policy'] = network_policy
            if node_pool is not None:
                kwargs['node_pool'] = node_pool
            if private_cluster_config is not None:
                kwargs['private_cluster_config'] = private_cluster_config
            if release_channel is not None:
                kwargs['release_channel'] = release_channel
            if resource_usage_export_config is not None:
                kwargs['resource_usage_export_config'] = resource_usage_export_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if vertical_pod_autoscaling is not None:
                kwargs['vertical_pod_autoscaling'] = vertical_pod_autoscaling
            if workload_identity_config is not None:
                kwargs['workload_identity_config'] = workload_identity_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
