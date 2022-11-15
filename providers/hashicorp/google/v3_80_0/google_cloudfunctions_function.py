
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FailurePolicyItem():
        retry:bool
        # non-optional-blocks
        
# wrapper list class
class FailurePolicy(BlockList):
        items: List[FailurePolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EventTriggerItem():
        event_type:str
        resource:str
        # non-optional-blocks
        failure_policy: Optional[FailurePolicy]=None,
        
# wrapper list class
class EventTrigger(BlockList):
        items: List[EventTriggerItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceRepositoryItem():
        url:str
        # non-optional-blocks
        
# wrapper list class
class SourceRepository(BlockList):
        items: List[SourceRepositoryItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        read: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudfunctionsFunction(ResourceObject):
    """    
    Args:
        name (str): A user-defined name of the function. Function names must be unique globally.
        runtime (str): The runtime in which the function is going to run. Eg. "nodejs8", "nodejs10", "python37", "go111".
    """
    _type = 'google_cloudfunctions_function'
    
    def __init__(self,
        tf_id: str,
        name:str,
        runtime:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        available_memory_mb: Optional[float] = None,
        build_environment_variables: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        entry_point: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        https_trigger_url: Optional[str] = None,
        id: Optional[str] = None,
        ingress_settings: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        max_instances: Optional[float] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        service_account_email: Optional[str] = None,
        source_archive_bucket: Optional[str] = None,
        source_archive_object: Optional[str] = None,
        timeout: Optional[float] = None,
        trigger_http: Optional[bool] = None,
        vpc_connector: Optional[str] = None,
        vpc_connector_egress_settings: Optional[str] = None,
        failure_policy: Optional[FailurePolicy]=None,
        event_trigger: Optional[EventTrigger]=None,
        source_repository: Optional[SourceRepository]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if runtime is not None:
                kwargs['runtime'] = runtime
            if available_memory_mb is not None:
                kwargs['available_memory_mb'] = available_memory_mb
            if build_environment_variables is not None:
                kwargs['build_environment_variables'] = build_environment_variables
            if description is not None:
                kwargs['description'] = description
            if entry_point is not None:
                kwargs['entry_point'] = entry_point
            if environment_variables is not None:
                kwargs['environment_variables'] = environment_variables
            if https_trigger_url is not None:
                kwargs['https_trigger_url'] = https_trigger_url
            if id is not None:
                kwargs['id'] = id
            if ingress_settings is not None:
                kwargs['ingress_settings'] = ingress_settings
            if labels is not None:
                kwargs['labels'] = labels
            if max_instances is not None:
                kwargs['max_instances'] = max_instances
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if service_account_email is not None:
                kwargs['service_account_email'] = service_account_email
            if source_archive_bucket is not None:
                kwargs['source_archive_bucket'] = source_archive_bucket
            if source_archive_object is not None:
                kwargs['source_archive_object'] = source_archive_object
            if timeout is not None:
                kwargs['timeout'] = timeout
            if trigger_http is not None:
                kwargs['trigger_http'] = trigger_http
            if vpc_connector is not None:
                kwargs['vpc_connector'] = vpc_connector
            if vpc_connector_egress_settings is not None:
                kwargs['vpc_connector_egress_settings'] = vpc_connector_egress_settings
            if failure_policy is not None:
                kwargs['failure_policy'] = failure_policy
            if event_trigger is not None:
                kwargs['event_trigger'] = event_trigger
            if source_repository is not None:
                kwargs['source_repository'] = source_repository
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
