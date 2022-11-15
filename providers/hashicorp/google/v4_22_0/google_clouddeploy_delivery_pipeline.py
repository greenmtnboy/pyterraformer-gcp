
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class StagesItem():
        # non-optional-blocks
        profiles: Optional[List[str]] = None
        target_id: Optional[str] = None
        
# wrapper list class
class Stages(BlockList):
        items: List[StagesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SerialPipelineItem():
        # non-optional-blocks
        stages: Optional[Stages]=None,
        
# wrapper list class
class SerialPipeline(BlockList):
        items: List[SerialPipelineItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleClouddeployDeliveryPipeline(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): Name of the `DeliveryPipeline`. Format is [a-z][a-z0-9\-]{0,62}.
    """
    _type = 'google_clouddeploy_delivery_pipeline'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        annotations: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        stages: Optional[Stages]=None,
        serial_pipeline: Optional[SerialPipeline]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if annotations is not None:
                kwargs['annotations'] = annotations
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if stages is not None:
                kwargs['stages'] = stages
            if serial_pipeline is not None:
                kwargs['serial_pipeline'] = serial_pipeline
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
