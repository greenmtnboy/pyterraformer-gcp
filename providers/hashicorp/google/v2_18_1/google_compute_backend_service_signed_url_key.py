
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




class GoogleComputeBackendServiceSignedUrlKey(ResourceObject):
    """    
    Args:
        backend_service (str): 
        key_value (str): 
        name (str): 
    """
    _type = 'google_compute_backend_service_signed_url_key'
    
    def __init__(self,
        tf_id: str,
        backend_service:str,
        key_value:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if backend_service is not None:
                kwargs['backend_service'] = backend_service
            if key_value is not None:
                kwargs['key_value'] = key_value
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
