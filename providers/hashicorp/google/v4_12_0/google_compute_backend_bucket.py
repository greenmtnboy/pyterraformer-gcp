
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NegativeCachingPolicyItem():
        # non-optional-blocks
        code: Optional[float] = None
        ttl: Optional[float] = None
        
# wrapper list class
class NegativeCachingPolicy(BlockList):
        items: List[NegativeCachingPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CdnPolicyItem():
        # non-optional-blocks
        cache_mode: Optional[str] = None
        client_ttl: Optional[float] = None
        default_ttl: Optional[float] = None
        max_ttl: Optional[float] = None
        negative_caching: Optional[bool] = None
        serve_while_stale: Optional[float] = None
        signed_url_cache_max_age_sec: Optional[float] = None
        negative_caching_policy: Optional[NegativeCachingPolicy]=None,
        
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
        bucket_name (str): Cloud Storage bucket name.
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035.  Specifically, the name must be 1-63 characters long and
                    match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means
                    the first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the
                    last character, which cannot be a dash.
    """
    _type = 'google_compute_backend_bucket'
    
    def __init__(self,
        tf_id: str,
        bucket_name:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        custom_response_headers: Optional[List[str]] = None,
        description: Optional[str] = None,
        enable_cdn: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        negative_caching_policy: Optional[NegativeCachingPolicy]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if bucket_name is not None:
                kwargs['bucket_name'] = bucket_name
            if name is not None:
                kwargs['name'] = name
            if custom_response_headers is not None:
                kwargs['custom_response_headers'] = custom_response_headers
            if description is not None:
                kwargs['description'] = description
            if enable_cdn is not None:
                kwargs['enable_cdn'] = enable_cdn
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if negative_caching_policy is not None:
                kwargs['negative_caching_policy'] = negative_caching_policy
            if cdn_policy is not None:
                kwargs['cdn_policy'] = cdn_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
