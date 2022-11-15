
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CdnPolicyItem():
        # non-optional-blocks
        signed_url_cache_max_age_sec: Optional[float] = None
        
# wrapper list class
class CdnPolicy(BlockList):
        items: List[CdnPolicyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeBackendBucket(ResourceObject):
    """    
    Args:
        bucket_name (str): 
        name (str): 
    """
    _type = 'google_compute_backend_bucket'
    
    def __init__(self,
        tf_id: str,
        bucket_name:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        enable_cdn: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        cdn_policy: Optional[CdnPolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if bucket_name is not None:
                kwargs['bucket_name'] = bucket_name
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if enable_cdn is not None:
                kwargs['enable_cdn'] = enable_cdn
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if cdn_policy is not None:
                kwargs['cdn_policy'] = cdn_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
