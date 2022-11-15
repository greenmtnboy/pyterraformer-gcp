
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




class GoogleComputeBackendBucketSignedUrlKey(ResourceObject):
    """    
    Args:
        backend_bucket (str): The backend bucket this signed URL key belongs.
        key_value (str): 128-bit key value used for signing the URL. The key value must be a
                    valid RFC 4648 Section 5 base64url encoded string.
        name (str): Name of the signed URL key.
    """
    _type = 'google_compute_backend_bucket_signed_url_key'
    
    def __init__(self,
        tf_id: str,
        backend_bucket:str,
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
            if backend_bucket is not None:
                kwargs['backend_bucket'] = backend_bucket
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
            
        
        
