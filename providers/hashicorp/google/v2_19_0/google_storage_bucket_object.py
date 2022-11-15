
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleStorageBucketObject(ResourceObject):
    """    
    Args:
        bucket (str): 
        name (str): 
    """
    _type = 'google_storage_bucket_object'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        cache_control: Optional[str] = None,
        content: Optional[str] = None,
        content_disposition: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_language: Optional[str] = None,
        content_type: Optional[str] = None,
        detect_md5hash: Optional[str] = None,
        id: Optional[str] = None,
        predefined_acl: Optional[str] = None,
        source: Optional[str] = None,
        storage_class: Optional[str] = None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if name is not None:
                kwargs['name'] = name
            if cache_control is not None:
                kwargs['cache_control'] = cache_control
            if content is not None:
                kwargs['content'] = content
            if content_disposition is not None:
                kwargs['content_disposition'] = content_disposition
            if content_encoding is not None:
                kwargs['content_encoding'] = content_encoding
            if content_language is not None:
                kwargs['content_language'] = content_language
            if content_type is not None:
                kwargs['content_type'] = content_type
            if detect_md5hash is not None:
                kwargs['detect_md5hash'] = detect_md5hash
            if id is not None:
                kwargs['id'] = id
            if predefined_acl is not None:
                kwargs['predefined_acl'] = predefined_acl
            if source is not None:
                kwargs['source'] = source
            if storage_class is not None:
                kwargs['storage_class'] = storage_class
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
