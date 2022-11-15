
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class LocalObjectReferenceItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class LocalObjectReference(BlockList):
        items: List[LocalObjectReferenceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigMapRefItem():
        # non-optional-blocks
        optional: Optional[bool] = None
        local_object_reference: Optional[LocalObjectReference]=None,
        
# wrapper list class
class ConfigMapRef(BlockList):
        items: List[ConfigMapRefItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecretRefItem():
        # non-optional-blocks
        optional: Optional[bool] = None
        local_object_reference: Optional[LocalObjectReference]=None,
        
# wrapper list class
class SecretRef(BlockList):
        items: List[SecretRefItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EnvItem():
        # non-optional-blocks
        name: Optional[str] = None
        value: Optional[str] = None
        
# wrapper list class
class Env(BlockList):
        items: List[EnvItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EnvFromItem():
        # non-optional-blocks
        prefix: Optional[str] = None
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        
# wrapper list class
class EnvFrom(BlockList):
        items: List[EnvFromItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourcesItem():
        # non-optional-blocks
        limits: Optional[Dict[str, str]] = None
        requests: Optional[Dict[str, str]] = None
        
# wrapper list class
class Resources(BlockList):
        items: List[ResourcesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ContainersItem():
        image:str
        # non-optional-blocks
        args: Optional[List[str]] = None
        command: Optional[List[str]] = None
        working_dir: Optional[str] = None
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        resources: Optional[Resources]=None,
        
# wrapper list class
class Containers(BlockList):
        items: List[ContainersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MetadataItem():
        # non-optional-blocks
        annotations: Optional[Dict[str, str]] = None
        labels: Optional[Dict[str, str]] = None
        namespace: Optional[str] = None
        
# wrapper list class
class Metadata(BlockList):
        items: List[MetadataItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SpecItem():
        # non-optional-blocks
        container_concurrency: Optional[float] = None
        service_account_name: Optional[str] = None
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        resources: Optional[Resources]=None,
        containers: Optional[Containers]=None,
        
# wrapper list class
class Spec(BlockList):
        items: List[SpecItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TemplateItem():
        # non-optional-blocks
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        resources: Optional[Resources]=None,
        containers: Optional[Containers]=None,
        metadata: Optional[Metadata]=None,
        spec: Optional[Spec]=None,
        
# wrapper list class
class Template(BlockList):
        items: List[TemplateItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TrafficItem():
        percent:float
        # non-optional-blocks
        latest_revision: Optional[bool] = None
        revision_name: Optional[str] = None
        
# wrapper list class
class Traffic(BlockList):
        items: List[TrafficItem]




class GoogleCloudRunService(ResourceObject):
    """    
    Args:
        location (str): The location of the cloud run instance. eg us-central1
        name (str): Name must be unique within a namespace, within a Cloud Run region.
                    Is required when creating resources. Name is primarily intended
                    for creation idempotence and configuration definition. Cannot be updated.
                    More info: http://kubernetes.io/docs/user-guide/identifiers#names
    """
    _type = 'google_cloud_run_service'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        resources: Optional[Resources]=None,
        containers: Optional[Containers]=None,
        metadata: Optional[Metadata]=None,
        spec: Optional[Spec]=None,
        template: Optional[Template]=None,
        timeouts: Optional[Timeouts]=None,
        traffic: Optional[Traffic]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if local_object_reference is not None:
                kwargs['local_object_reference'] = local_object_reference
            if config_map_ref is not None:
                kwargs['config_map_ref'] = config_map_ref
            if secret_ref is not None:
                kwargs['secret_ref'] = secret_ref
            if env is not None:
                kwargs['env'] = env
            if env_from is not None:
                kwargs['env_from'] = env_from
            if resources is not None:
                kwargs['resources'] = resources
            if containers is not None:
                kwargs['containers'] = containers
            if metadata is not None:
                kwargs['metadata'] = metadata
            if spec is not None:
                kwargs['spec'] = spec
            if template is not None:
                kwargs['template'] = template
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if traffic is not None:
                kwargs['traffic'] = traffic
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
