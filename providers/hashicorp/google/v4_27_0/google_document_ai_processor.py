
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleDocumentAiProcessor(ResourceObject):
    """    
    Args:
        display_name (str): The display name. Must be unique.
        location (str): The location of the resource.
        type (str): The type of processor. For possible types see the [official list](https://cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations/fetchProcessorTypes#google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes)
    """
    _type = 'google_document_ai_processor'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        location:str,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        kms_key_name: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if location is not None:
                kwargs['location'] = location
            if type is not None:
                kwargs['type'] = type
            if id is not None:
                kwargs['id'] = id
            if kms_key_name is not None:
                kwargs['kms_key_name'] = kms_key_name
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
