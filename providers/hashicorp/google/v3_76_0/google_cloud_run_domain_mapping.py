
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class MetadataItem():
        namespace:str
        # non-optional-blocks
        annotations: Optional[Dict[str, str]] = None
        labels: Optional[Dict[str, str]] = None
        
# wrapper list class
class Metadata(BlockList):
        items: List[MetadataItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SpecItem():
        route_name:str
        # non-optional-blocks
        certificate_mode: Optional[str] = None
        force_override: Optional[bool] = None
        
# wrapper list class
class Spec(BlockList):
        items: List[SpecItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleCloudRunDomainMapping(ResourceObject):
    """    
    Args:
        location (str): The location of the cloud run instance. eg us-central1
        name (str): Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
    """
    _type = 'google_cloud_run_domain_mapping'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        metadata: Optional[Metadata]=None,
        spec: Optional[Spec]=None,
        timeouts: Optional[Timeouts]=None,
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
            if metadata is not None:
                kwargs['metadata'] = metadata
            if spec is not None:
                kwargs['spec'] = spec
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
