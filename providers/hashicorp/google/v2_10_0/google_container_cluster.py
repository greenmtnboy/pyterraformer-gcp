
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SandboxConfigItem():
        sandbox_type:str
        # non-optional-blocks
        
# wrapper list class
class SandboxConfig(BlockList):
        items: List[SandboxConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TaintItem():
        effect:str
        key:str
        value:str
        # non-optional-blocks
        
# wrapper list class
class Taint(BlockList):
        items: List[TaintItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkloadMetadataConfigItem():
        node_metadata:str
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
        sandbox_config: Optional[SandboxConfig]=None,
        taint: Optional[Taint]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        
# wrapper list class
class NodeConfig(BlockList):
        items: List[NodeConfigItem]





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
class HorizontalPodAutoscalingItem():
        # non-optional-blocks
        disabled: Optional[bool] = None
        
# wrapper list class
class HorizontalPodAutoscaling(BlockList):
        items: List[HorizontalPodAutoscalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpLoadBalancingItem():
        # non-optional-blocks
        disabled: Optional[bool] = None
        
# wrapper list class
class HttpLoadBalancing(BlockList):
        items: List[HttpLoadBalancingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KubernetesDashboardItem():
        # non-optional-blocks
        disabled: Optional[bool] = None
        
# wrapper list class
class KubernetesDashboard(BlockList):
        items: List[KubernetesDashboardItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkPolicyConfigItem():
        # non-optional-blocks
        disabled: Optional[bool] = None
        
# wrapper list class
class NetworkPolicyConfig(BlockList):
        items: List[NetworkPolicyConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AddonsConfigItem():
        # non-optional-blocks
        horizontal_pod_autoscaling: Optional[HorizontalPodAutoscaling]=None,
        http_load_balancing: Optional[HttpLoadBalancing]=None,
        kubernetes_dashboard: Optional[KubernetesDashboard]=None,
        network_policy_config: Optional[NetworkPolicyConfig]=None,
        
# wrapper list class
class AddonsConfig(BlockList):
        items: List[AddonsConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaintenancePolicyItem():
        # non-optional-blocks
        daily_maintenance_window: Optional[DailyMaintenanceWindow]=None,
        
# wrapper list class
class MaintenancePolicy(BlockList):
        items: List[MaintenancePolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MasterAuthItem():
        # non-optional-blocks
        password: Optional[str] = None
        username: Optional[str] = None
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
class NetworkPolicyItem():
        # non-optional-blocks
        enabled: Optional[bool] = None
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
        version: Optional[str] = None
        sandbox_config: Optional[SandboxConfig]=None,
        taint: Optional[Taint]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        autoscaling: Optional[Autoscaling]=None,
        management: Optional[Management]=None,
        node_config: Optional[NodeConfig]=None,
        
# wrapper list class
class NodePool(BlockList):
        items: List[NodePoolItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PodSecurityPolicyConfigItem():
        enabled:bool
        # non-optional-blocks
        
# wrapper list class
class PodSecurityPolicyConfig(BlockList):
        items: List[PodSecurityPolicyConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrivateClusterConfigItem():
        # non-optional-blocks
        enable_private_endpoint: Optional[bool] = None
        enable_private_nodes: Optional[bool] = None
        master_ipv4_cidr_block: Optional[str] = None
        
# wrapper list class
class PrivateClusterConfig(BlockList):
        items: List[PrivateClusterConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleContainerCluster(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_container_cluster'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        additional_zones: Optional[Set[str]] = None,
        cluster_ipv4_cidr: Optional[str] = None,
        description: Optional[str] = None,
        enable_binary_authorization: Optional[bool] = None,
        enable_intranode_visibility: Optional[bool] = None,
        enable_kubernetes_alpha: Optional[bool] = None,
        enable_legacy_abac: Optional[bool] = None,
        enable_tpu: Optional[bool] = None,
        id: Optional[str] = None,
        initial_node_count: Optional[float] = None,
        ip_allocation_policy: Optional[List[Dict[str,Any]]] = None,
        location: Optional[str] = None,
        logging_service: Optional[str] = None,
        min_master_version: Optional[str] = None,
        monitoring_service: Optional[str] = None,
        network: Optional[str] = None,
        node_locations: Optional[Set[str]] = None,
        node_version: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        remove_default_node_pool: Optional[bool] = None,
        resource_labels: Optional[Dict[str, str]] = None,
        subnetwork: Optional[str] = None,
        zone: Optional[str] = None,
        sandbox_config: Optional[SandboxConfig]=None,
        taint: Optional[Taint]=None,
        workload_metadata_config: Optional[WorkloadMetadataConfig]=None,
        autoscaling: Optional[Autoscaling]=None,
        management: Optional[Management]=None,
        node_config: Optional[NodeConfig]=None,
        cidr_blocks: Optional[CidrBlocks]=None,
        client_certificate_config: Optional[ClientCertificateConfig]=None,
        daily_maintenance_window: Optional[DailyMaintenanceWindow]=None,
        horizontal_pod_autoscaling: Optional[HorizontalPodAutoscaling]=None,
        http_load_balancing: Optional[HttpLoadBalancing]=None,
        kubernetes_dashboard: Optional[KubernetesDashboard]=None,
        network_policy_config: Optional[NetworkPolicyConfig]=None,
        addons_config: Optional[AddonsConfig]=None,
        maintenance_policy: Optional[MaintenancePolicy]=None,
        master_auth: Optional[MasterAuth]=None,
        master_authorized_networks_config: Optional[MasterAuthorizedNetworksConfig]=None,
        network_policy: Optional[NetworkPolicy]=None,
        node_pool: Optional[NodePool]=None,
        pod_security_policy_config: Optional[PodSecurityPolicyConfig]=None,
        private_cluster_config: Optional[PrivateClusterConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if additional_zones is not None:
                kwargs['additional_zones'] = additional_zones
            if cluster_ipv4_cidr is not None:
                kwargs['cluster_ipv4_cidr'] = cluster_ipv4_cidr
            if description is not None:
                kwargs['description'] = description
            if enable_binary_authorization is not None:
                kwargs['enable_binary_authorization'] = enable_binary_authorization
            if enable_intranode_visibility is not None:
                kwargs['enable_intranode_visibility'] = enable_intranode_visibility
            if enable_kubernetes_alpha is not None:
                kwargs['enable_kubernetes_alpha'] = enable_kubernetes_alpha
            if enable_legacy_abac is not None:
                kwargs['enable_legacy_abac'] = enable_legacy_abac
            if enable_tpu is not None:
                kwargs['enable_tpu'] = enable_tpu
            if id is not None:
                kwargs['id'] = id
            if initial_node_count is not None:
                kwargs['initial_node_count'] = initial_node_count
            if ip_allocation_policy is not None:
                kwargs['ip_allocation_policy'] = ip_allocation_policy
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
            if node_locations is not None:
                kwargs['node_locations'] = node_locations
            if node_version is not None:
                kwargs['node_version'] = node_version
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if remove_default_node_pool is not None:
                kwargs['remove_default_node_pool'] = remove_default_node_pool
            if resource_labels is not None:
                kwargs['resource_labels'] = resource_labels
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if zone is not None:
                kwargs['zone'] = zone
            if sandbox_config is not None:
                kwargs['sandbox_config'] = sandbox_config
            if taint is not None:
                kwargs['taint'] = taint
            if workload_metadata_config is not None:
                kwargs['workload_metadata_config'] = workload_metadata_config
            if autoscaling is not None:
                kwargs['autoscaling'] = autoscaling
            if management is not None:
                kwargs['management'] = management
            if node_config is not None:
                kwargs['node_config'] = node_config
            if cidr_blocks is not None:
                kwargs['cidr_blocks'] = cidr_blocks
            if client_certificate_config is not None:
                kwargs['client_certificate_config'] = client_certificate_config
            if daily_maintenance_window is not None:
                kwargs['daily_maintenance_window'] = daily_maintenance_window
            if horizontal_pod_autoscaling is not None:
                kwargs['horizontal_pod_autoscaling'] = horizontal_pod_autoscaling
            if http_load_balancing is not None:
                kwargs['http_load_balancing'] = http_load_balancing
            if kubernetes_dashboard is not None:
                kwargs['kubernetes_dashboard'] = kubernetes_dashboard
            if network_policy_config is not None:
                kwargs['network_policy_config'] = network_policy_config
            if addons_config is not None:
                kwargs['addons_config'] = addons_config
            if maintenance_policy is not None:
                kwargs['maintenance_policy'] = maintenance_policy
            if master_auth is not None:
                kwargs['master_auth'] = master_auth
            if master_authorized_networks_config is not None:
                kwargs['master_authorized_networks_config'] = master_authorized_networks_config
            if network_policy is not None:
                kwargs['network_policy'] = network_policy
            if node_pool is not None:
                kwargs['node_pool'] = node_pool
            if pod_security_policy_config is not None:
                kwargs['pod_security_policy_config'] = pod_security_policy_config
            if private_cluster_config is not None:
                kwargs['private_cluster_config'] = private_cluster_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
