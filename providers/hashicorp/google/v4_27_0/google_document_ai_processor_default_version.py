
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




class GoogleDocumentAiProcessorDefaultVersion(ResourceObject):
    """    
    Args:
        processor (str): The processor to set the version on.
        version (str): The version to set
    """
    _type = 'google_document_ai_processor_default_version'
    
    def __init__(self,
        tf_id: str,
        processor:str,
        version:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if processor is not None:
                kwargs['processor'] = processor
            if version is not None:
                kwargs['version'] = version
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
