
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class VolumesItem():
        name:str
        size_gb:float
        volume_type:str
        # non-optional-blocks
        
# wrapper list class
class Volumes(BlockList):
        items: List[VolumesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScriptItem():
        script_path:str
        # non-optional-blocks
        
# wrapper list class
class Script(BlockList):
        items: List[ScriptItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StaticFilesItem():
        # non-optional-blocks
        application_readable: Optional[bool] = None
        expiration: Optional[str] = None
        http_headers: Optional[Dict[str, str]] = None
        mime_type: Optional[str] = None
        path: Optional[str] = None
        require_matching_file: Optional[bool] = None
        upload_path_regex: Optional[str] = None
        
# wrapper list class
class StaticFiles(BlockList):
        items: List[StaticFilesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudBuildOptionsItem():
        app_yaml_path:str
        # non-optional-blocks
        cloud_build_timeout: Optional[str] = None
        
# wrapper list class
class CloudBuildOptions(BlockList):
        items: List[CloudBuildOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ContainerItem():
        image:str
        # non-optional-blocks
        
# wrapper list class
class Container(BlockList):
        items: List[ContainerItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class FilesItem():
        name:str
        source_url:str
        # non-optional-blocks
        sha1_sum: Optional[str] = None
        
# wrapper list class
class Files(BlockSet):
        items: Set[FilesItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class ZipItem():
        source_url:str
        # non-optional-blocks
        files_count: Optional[float] = None
        
# wrapper list class
class Zip(BlockList):
        items: List[ZipItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CpuUtilizationItem():
        target_utilization:float
        # non-optional-blocks
        aggregation_window_length: Optional[str] = None
        
# wrapper list class
class CpuUtilization(BlockList):
        items: List[CpuUtilizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DiskUtilizationItem():
        # non-optional-blocks
        target_read_bytes_per_second: Optional[float] = None
        target_read_ops_per_second: Optional[float] = None
        target_write_bytes_per_second: Optional[float] = None
        target_write_ops_per_second: Optional[float] = None
        
# wrapper list class
class DiskUtilization(BlockList):
        items: List[DiskUtilizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkUtilizationItem():
        # non-optional-blocks
        target_received_bytes_per_second: Optional[float] = None
        target_received_packets_per_second: Optional[float] = None
        target_sent_bytes_per_second: Optional[float] = None
        target_sent_packets_per_second: Optional[float] = None
        
# wrapper list class
class NetworkUtilization(BlockList):
        items: List[NetworkUtilizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RequestUtilizationItem():
        # non-optional-blocks
        target_concurrent_requests: Optional[float] = None
        target_request_count_per_second: Optional[str] = None
        
# wrapper list class
class RequestUtilization(BlockList):
        items: List[RequestUtilizationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ApiConfigItem():
        script:str
        # non-optional-blocks
        auth_fail_action: Optional[str] = None
        login: Optional[str] = None
        security_level: Optional[str] = None
        url: Optional[str] = None
        
# wrapper list class
class ApiConfig(BlockList):
        items: List[ApiConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AutomaticScalingItem():
        # non-optional-blocks
        cool_down_period: Optional[str] = None
        max_concurrent_requests: Optional[float] = None
        max_idle_instances: Optional[float] = None
        max_pending_latency: Optional[str] = None
        max_total_instances: Optional[float] = None
        min_idle_instances: Optional[float] = None
        min_pending_latency: Optional[str] = None
        min_total_instances: Optional[float] = None
        cpu_utilization: Optional[CpuUtilization]=None,
        disk_utilization: Optional[DiskUtilization]=None,
        network_utilization: Optional[NetworkUtilization]=None,
        request_utilization: Optional[RequestUtilization]=None,
        
# wrapper list class
class AutomaticScaling(BlockList):
        items: List[AutomaticScalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DeploymentItem():
        # non-optional-blocks
        cloud_build_options: Optional[CloudBuildOptions]=None,
        container: Optional[Container]=None,
        files: Optional[Files]=None,
        zip: Optional[Zip]=None,
        
# wrapper list class
class Deployment(BlockList):
        items: List[DeploymentItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EndpointsApiServiceItem():
        name:str
        # non-optional-blocks
        config_id: Optional[str] = None
        disable_trace_sampling: Optional[bool] = None
        rollout_strategy: Optional[str] = None
        
# wrapper list class
class EndpointsApiService(BlockList):
        items: List[EndpointsApiServiceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EntrypointItem():
        shell:str
        # non-optional-blocks
        
# wrapper list class
class Entrypoint(BlockList):
        items: List[EntrypointItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HandlersItem():
        # non-optional-blocks
        auth_fail_action: Optional[str] = None
        login: Optional[str] = None
        redirect_http_response_code: Optional[str] = None
        security_level: Optional[str] = None
        url_regex: Optional[str] = None
        script: Optional[Script]=None,
        static_files: Optional[StaticFiles]=None,
        
# wrapper list class
class Handlers(BlockList):
        items: List[HandlersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LivenessCheckItem():
        path:str
        # non-optional-blocks
        check_interval: Optional[str] = None
        failure_threshold: Optional[float] = None
        host: Optional[str] = None
        initial_delay: Optional[str] = None
        success_threshold: Optional[float] = None
        timeout: Optional[str] = None
        
# wrapper list class
class LivenessCheck(BlockList):
        items: List[LivenessCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ManualScalingItem():
        instances:float
        # non-optional-blocks
        
# wrapper list class
class ManualScaling(BlockList):
        items: List[ManualScalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkItem():
        name:str
        # non-optional-blocks
        forwarded_ports: Optional[List[str]] = None
        instance_tag: Optional[str] = None
        session_affinity: Optional[bool] = None
        subnetwork: Optional[str] = None
        
# wrapper list class
class Network(BlockList):
        items: List[NetworkItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReadinessCheckItem():
        path:str
        # non-optional-blocks
        app_start_timeout: Optional[str] = None
        check_interval: Optional[str] = None
        failure_threshold: Optional[float] = None
        host: Optional[str] = None
        success_threshold: Optional[float] = None
        timeout: Optional[str] = None
        
# wrapper list class
class ReadinessCheck(BlockList):
        items: List[ReadinessCheckItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourcesItem():
        # non-optional-blocks
        cpu: Optional[float] = None
        disk_gb: Optional[float] = None
        memory_gb: Optional[float] = None
        volumes: Optional[Volumes]=None,
        
# wrapper list class
class Resources(BlockList):
        items: List[ResourcesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class VpcAccessConnectorItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class VpcAccessConnector(BlockList):
        items: List[VpcAccessConnectorItem]




class GoogleAppEngineFlexibleAppVersion(ResourceObject):
    """    
    Args:
        runtime (str): Desired runtime. Example python27.
    """
    _type = 'google_app_engine_flexible_app_version'
    
    def __init__(self,
        tf_id: str,
        runtime:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        beta_settings: Optional[Dict[str, str]] = None,
        default_expiration: Optional[str] = None,
        delete_service_on_destroy: Optional[bool] = None,
        env_variables: Optional[Dict[str, str]] = None,
        id: Optional[str] = None,
        inbound_services: Optional[List[str]] = None,
        instance_class: Optional[str] = None,
        nobuild_files_regex: Optional[str] = None,
        noop_on_destroy: Optional[bool] = None,
        project: Optional[str] = None,
        runtime_api_version: Optional[str] = None,
        runtime_channel: Optional[str] = None,
        runtime_main_executable_path: Optional[str] = None,
        service: Optional[str] = None,
        serving_status: Optional[str] = None,
        version_id: Optional[str] = None,
        volumes: Optional[Volumes]=None,
        script: Optional[Script]=None,
        static_files: Optional[StaticFiles]=None,
        cloud_build_options: Optional[CloudBuildOptions]=None,
        container: Optional[Container]=None,
        files: Optional[Files]=None,
        zip: Optional[Zip]=None,
        cpu_utilization: Optional[CpuUtilization]=None,
        disk_utilization: Optional[DiskUtilization]=None,
        network_utilization: Optional[NetworkUtilization]=None,
        request_utilization: Optional[RequestUtilization]=None,
        api_config: Optional[ApiConfig]=None,
        automatic_scaling: Optional[AutomaticScaling]=None,
        deployment: Optional[Deployment]=None,
        endpoints_api_service: Optional[EndpointsApiService]=None,
        entrypoint: Optional[Entrypoint]=None,
        handlers: Optional[Handlers]=None,
        liveness_check: Optional[LivenessCheck]=None,
        manual_scaling: Optional[ManualScaling]=None,
        network: Optional[Network]=None,
        readiness_check: Optional[ReadinessCheck]=None,
        resources: Optional[Resources]=None,
        timeouts: Optional[Timeouts]=None,
        vpc_access_connector: Optional[VpcAccessConnector]=None,
        ):
            kwargs = {}
            if runtime is not None:
                kwargs['runtime'] = runtime
            if beta_settings is not None:
                kwargs['beta_settings'] = beta_settings
            if default_expiration is not None:
                kwargs['default_expiration'] = default_expiration
            if delete_service_on_destroy is not None:
                kwargs['delete_service_on_destroy'] = delete_service_on_destroy
            if env_variables is not None:
                kwargs['env_variables'] = env_variables
            if id is not None:
                kwargs['id'] = id
            if inbound_services is not None:
                kwargs['inbound_services'] = inbound_services
            if instance_class is not None:
                kwargs['instance_class'] = instance_class
            if nobuild_files_regex is not None:
                kwargs['nobuild_files_regex'] = nobuild_files_regex
            if noop_on_destroy is not None:
                kwargs['noop_on_destroy'] = noop_on_destroy
            if project is not None:
                kwargs['project'] = project
            if runtime_api_version is not None:
                kwargs['runtime_api_version'] = runtime_api_version
            if runtime_channel is not None:
                kwargs['runtime_channel'] = runtime_channel
            if runtime_main_executable_path is not None:
                kwargs['runtime_main_executable_path'] = runtime_main_executable_path
            if service is not None:
                kwargs['service'] = service
            if serving_status is not None:
                kwargs['serving_status'] = serving_status
            if version_id is not None:
                kwargs['version_id'] = version_id
            if volumes is not None:
                kwargs['volumes'] = volumes
            if script is not None:
                kwargs['script'] = script
            if static_files is not None:
                kwargs['static_files'] = static_files
            if cloud_build_options is not None:
                kwargs['cloud_build_options'] = cloud_build_options
            if container is not None:
                kwargs['container'] = container
            if files is not None:
                kwargs['files'] = files
            if zip is not None:
                kwargs['zip'] = zip
            if cpu_utilization is not None:
                kwargs['cpu_utilization'] = cpu_utilization
            if disk_utilization is not None:
                kwargs['disk_utilization'] = disk_utilization
            if network_utilization is not None:
                kwargs['network_utilization'] = network_utilization
            if request_utilization is not None:
                kwargs['request_utilization'] = request_utilization
            if api_config is not None:
                kwargs['api_config'] = api_config
            if automatic_scaling is not None:
                kwargs['automatic_scaling'] = automatic_scaling
            if deployment is not None:
                kwargs['deployment'] = deployment
            if endpoints_api_service is not None:
                kwargs['endpoints_api_service'] = endpoints_api_service
            if entrypoint is not None:
                kwargs['entrypoint'] = entrypoint
            if handlers is not None:
                kwargs['handlers'] = handlers
            if liveness_check is not None:
                kwargs['liveness_check'] = liveness_check
            if manual_scaling is not None:
                kwargs['manual_scaling'] = manual_scaling
            if network is not None:
                kwargs['network'] = network
            if readiness_check is not None:
                kwargs['readiness_check'] = readiness_check
            if resources is not None:
                kwargs['resources'] = resources
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if vpc_access_connector is not None:
                kwargs['vpc_access_connector'] = vpc_access_connector
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
