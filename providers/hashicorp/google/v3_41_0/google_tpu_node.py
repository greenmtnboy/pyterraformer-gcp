
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SchedulingConfigItem():
        preemptible:bool
        # non-optional-blocks
        
# wrapper list class
class SchedulingConfig(BlockList):
        items: List[SchedulingConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleTpuNode(ResourceObject):
    """    
    Args:
        accelerator_type (str): The type of hardware accelerators associated with this node.
        name (str): The immutable name of the TPU.
        tensorflow_version (str): The version of Tensorflow running in the Node.
        zone (str): The GCP location for the TPU.
    """
    _type = 'google_tpu_node'
    
    def __init__(self,
        tf_id: str,
        accelerator_type:str,
        name:str,
        tensorflow_version:str,
        zone:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        cidr_block: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        network: Optional[str] = None,
        project: Optional[str] = None,
        use_service_networking: Optional[bool] = None,
        scheduling_config: Optional[SchedulingConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if accelerator_type is not None:
                kwargs['accelerator_type'] = accelerator_type
            if name is not None:
                kwargs['name'] = name
            if tensorflow_version is not None:
                kwargs['tensorflow_version'] = tensorflow_version
            if zone is not None:
                kwargs['zone'] = zone
            if cidr_block is not None:
                kwargs['cidr_block'] = cidr_block
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if network is not None:
                kwargs['network'] = network
            if project is not None:
                kwargs['project'] = project
            if use_service_networking is not None:
                kwargs['use_service_networking'] = use_service_networking
            if scheduling_config is not None:
                kwargs['scheduling_config'] = scheduling_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
