
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleStorageBucketAcl(ResourceObject):
    """    
    Args:
        bucket (str): The name of the bucket it applies to.
    """
    _type = 'google_storage_bucket_acl'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        default_acl: Optional[str] = None,
        id: Optional[str] = None,
        predefined_acl: Optional[str] = None,
        role_entity: Optional[List[str]] = None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if default_acl is not None:
                kwargs['default_acl'] = default_acl
            if id is not None:
                kwargs['id'] = id
            if predefined_acl is not None:
                kwargs['predefined_acl'] = predefined_acl
            if role_entity is not None:
                kwargs['role_entity'] = role_entity
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
