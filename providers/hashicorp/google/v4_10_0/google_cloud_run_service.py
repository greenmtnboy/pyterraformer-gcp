
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ItemsItem():
        key:str
        path:str
        # non-optional-blocks
        mode: Optional[float] = None
        
# wrapper list class
class Items(BlockList):
        items: List[ItemsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecretItem():
        secret_name:str
        # non-optional-blocks
        default_mode: Optional[float] = None
        items: Optional[Items]=None,
        
# wrapper list class
class Secret(BlockList):
        items: List[SecretItem]




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
class SecretKeyRefItem():
        key:str
        name:str
        # non-optional-blocks
        
# wrapper list class
class SecretKeyRef(BlockList):
        items: List[SecretKeyRefItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ValueFromItem():
        # non-optional-blocks
        secret_key_ref: Optional[SecretKeyRef]=None,
        
# wrapper list class
class ValueFrom(BlockList):
        items: List[ValueFromItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class EnvItem():
        # non-optional-blocks
        name: Optional[str] = None
        value: Optional[str] = None
        secret_key_ref: Optional[SecretKeyRef]=None,
        value_from: Optional[ValueFrom]=None,
        
# wrapper list class
class Env(BlockSet):
        items: Set[EnvItem]



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
class PortsItem():
        container_port:float
        # non-optional-blocks
        name: Optional[str] = None
        protocol: Optional[str] = None
        
# wrapper list class
class Ports(BlockList):
        items: List[PortsItem]




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
class VolumeMountsItem():
        mount_path:str
        name:str
        # non-optional-blocks
        
# wrapper list class
class VolumeMounts(BlockList):
        items: List[VolumeMountsItem]




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
        secret_key_ref: Optional[SecretKeyRef]=None,
        value_from: Optional[ValueFrom]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        ports: Optional[Ports]=None,
        resources: Optional[Resources]=None,
        volume_mounts: Optional[VolumeMounts]=None,
        
# wrapper list class
class Containers(BlockList):
        items: List[ContainersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class VolumesItem():
        name:str
        # non-optional-blocks
        items: Optional[Items]=None,
        secret: Optional[Secret]=None,
        
# wrapper list class
class Volumes(BlockList):
        items: List[VolumesItem]




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
        timeout_seconds: Optional[float] = None
        items: Optional[Items]=None,
        secret: Optional[Secret]=None,
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        secret_key_ref: Optional[SecretKeyRef]=None,
        value_from: Optional[ValueFrom]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        ports: Optional[Ports]=None,
        resources: Optional[Resources]=None,
        volume_mounts: Optional[VolumeMounts]=None,
        containers: Optional[Containers]=None,
        volumes: Optional[Volumes]=None,
        
# wrapper list class
class Spec(BlockList):
        items: List[SpecItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TemplateItem():
        # non-optional-blocks
        items: Optional[Items]=None,
        secret: Optional[Secret]=None,
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        secret_key_ref: Optional[SecretKeyRef]=None,
        value_from: Optional[ValueFrom]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        ports: Optional[Ports]=None,
        resources: Optional[Resources]=None,
        volume_mounts: Optional[VolumeMounts]=None,
        containers: Optional[Containers]=None,
        volumes: Optional[Volumes]=None,
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
        autogenerate_revision_name: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        items: Optional[Items]=None,
        secret: Optional[Secret]=None,
        local_object_reference: Optional[LocalObjectReference]=None,
        config_map_ref: Optional[ConfigMapRef]=None,
        secret_ref: Optional[SecretRef]=None,
        secret_key_ref: Optional[SecretKeyRef]=None,
        value_from: Optional[ValueFrom]=None,
        env: Optional[Env]=None,
        env_from: Optional[EnvFrom]=None,
        ports: Optional[Ports]=None,
        resources: Optional[Resources]=None,
        volume_mounts: Optional[VolumeMounts]=None,
        containers: Optional[Containers]=None,
        volumes: Optional[Volumes]=None,
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
            if autogenerate_revision_name is not None:
                kwargs['autogenerate_revision_name'] = autogenerate_revision_name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if items is not None:
                kwargs['items'] = items
            if secret is not None:
                kwargs['secret'] = secret
            if local_object_reference is not None:
                kwargs['local_object_reference'] = local_object_reference
            if config_map_ref is not None:
                kwargs['config_map_ref'] = config_map_ref
            if secret_ref is not None:
                kwargs['secret_ref'] = secret_ref
            if secret_key_ref is not None:
                kwargs['secret_key_ref'] = secret_key_ref
            if value_from is not None:
                kwargs['value_from'] = value_from
            if env is not None:
                kwargs['env'] = env
            if env_from is not None:
                kwargs['env_from'] = env_from
            if ports is not None:
                kwargs['ports'] = ports
            if resources is not None:
                kwargs['resources'] = resources
            if volume_mounts is not None:
                kwargs['volume_mounts'] = volume_mounts
            if containers is not None:
                kwargs['containers'] = containers
            if volumes is not None:
                kwargs['volumes'] = volumes
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
            
        
        
