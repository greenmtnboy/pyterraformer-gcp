
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkConfigItem():
        peered_network:str
        # non-optional-blocks
        
# wrapper list class
class NetworkConfig(BlockList):
        items: List[NetworkConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkerConfigItem():
        # non-optional-blocks
        disk_size_gb: Optional[float] = None
        machine_type: Optional[str] = None
        no_external_ip: Optional[bool] = None
        
# wrapper list class
class WorkerConfig(BlockList):
        items: List[WorkerConfigItem]




class GoogleCloudbuildWorkerPool(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): User-defined name of the `WorkerPool`.
    """
    _type = 'google_cloudbuild_worker_pool'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        annotations: Optional[Dict[str, str]] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        network_config: Optional[NetworkConfig]=None,
        timeouts: Optional[Timeouts]=None,
        worker_config: Optional[WorkerConfig]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if annotations is not None:
                kwargs['annotations'] = annotations
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if network_config is not None:
                kwargs['network_config'] = network_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if worker_config is not None:
                kwargs['worker_config'] = worker_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
