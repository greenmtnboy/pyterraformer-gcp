
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



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
class StandardSchedulerSettingsItem():
        # non-optional-blocks
        max_instances: Optional[float] = None
        min_instances: Optional[float] = None
        target_cpu_utilization: Optional[float] = None
        target_throughput_utilization: Optional[float] = None
        
# wrapper list class
class StandardSchedulerSettings(BlockList):
        items: List[StandardSchedulerSettingsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AutomaticScalingItem():
        # non-optional-blocks
        max_concurrent_requests: Optional[float] = None
        max_idle_instances: Optional[float] = None
        max_pending_latency: Optional[str] = None
        min_idle_instances: Optional[float] = None
        min_pending_latency: Optional[str] = None
        standard_scheduler_settings: Optional[StandardSchedulerSettings]=None,
        
# wrapper list class
class AutomaticScaling(BlockList):
        items: List[AutomaticScalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BasicScalingItem():
        max_instances:float
        # non-optional-blocks
        idle_timeout: Optional[str] = None
        
# wrapper list class
class BasicScaling(BlockList):
        items: List[BasicScalingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DeploymentItem():
        # non-optional-blocks
        files: Optional[Files]=None,
        zip: Optional[Zip]=None,
        
# wrapper list class
class Deployment(BlockList):
        items: List[DeploymentItem]




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
class LibrariesItem():
        # non-optional-blocks
        name: Optional[str] = None
        version: Optional[str] = None
        
# wrapper list class
class Libraries(BlockList):
        items: List[LibrariesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ManualScalingItem():
        instances:float
        # non-optional-blocks
        
# wrapper list class
class ManualScaling(BlockList):
        items: List[ManualScalingItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAppEngineStandardAppVersion(ResourceObject):
    """    
    Args:
        runtime (str): Desired runtime. Example python27.
    """
    _type = 'google_app_engine_standard_app_version'
    
    def __init__(self,
        tf_id: str,
        runtime:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        delete_service_on_destroy: Optional[bool] = None,
        env_variables: Optional[Dict[str, str]] = None,
        id: Optional[str] = None,
        inbound_services: Optional[Set[str]] = None,
        instance_class: Optional[str] = None,
        noop_on_destroy: Optional[bool] = None,
        project: Optional[str] = None,
        runtime_api_version: Optional[str] = None,
        service: Optional[str] = None,
        threadsafe: Optional[bool] = None,
        version_id: Optional[str] = None,
        script: Optional[Script]=None,
        static_files: Optional[StaticFiles]=None,
        files: Optional[Files]=None,
        zip: Optional[Zip]=None,
        standard_scheduler_settings: Optional[StandardSchedulerSettings]=None,
        automatic_scaling: Optional[AutomaticScaling]=None,
        basic_scaling: Optional[BasicScaling]=None,
        deployment: Optional[Deployment]=None,
        entrypoint: Optional[Entrypoint]=None,
        handlers: Optional[Handlers]=None,
        libraries: Optional[Libraries]=None,
        manual_scaling: Optional[ManualScaling]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if runtime is not None:
                kwargs['runtime'] = runtime
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
            if noop_on_destroy is not None:
                kwargs['noop_on_destroy'] = noop_on_destroy
            if project is not None:
                kwargs['project'] = project
            if runtime_api_version is not None:
                kwargs['runtime_api_version'] = runtime_api_version
            if service is not None:
                kwargs['service'] = service
            if threadsafe is not None:
                kwargs['threadsafe'] = threadsafe
            if version_id is not None:
                kwargs['version_id'] = version_id
            if script is not None:
                kwargs['script'] = script
            if static_files is not None:
                kwargs['static_files'] = static_files
            if files is not None:
                kwargs['files'] = files
            if zip is not None:
                kwargs['zip'] = zip
            if standard_scheduler_settings is not None:
                kwargs['standard_scheduler_settings'] = standard_scheduler_settings
            if automatic_scaling is not None:
                kwargs['automatic_scaling'] = automatic_scaling
            if basic_scaling is not None:
                kwargs['basic_scaling'] = basic_scaling
            if deployment is not None:
                kwargs['deployment'] = deployment
            if entrypoint is not None:
                kwargs['entrypoint'] = entrypoint
            if handlers is not None:
                kwargs['handlers'] = handlers
            if libraries is not None:
                kwargs['libraries'] = libraries
            if manual_scaling is not None:
                kwargs['manual_scaling'] = manual_scaling
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
