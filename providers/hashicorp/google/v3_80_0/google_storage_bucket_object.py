
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CustomerEncryptionItem():
        encryption_key:str
        # non-optional-blocks
        encryption_algorithm: Optional[str] = None
        
# wrapper list class
class CustomerEncryption(BlockList):
        items: List[CustomerEncryptionItem]




class GoogleStorageBucketObject(ResourceObject):
    """    
    Args:
        bucket (str): The name of the containing bucket.
        name (str): The name of the object. If you're interpolating the name of this object, see output_name instead.
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
        event_based_hold: Optional[bool] = None,
        id: Optional[str] = None,
        kms_key_name: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        source: Optional[str] = None,
        storage_class: Optional[str] = None,
        temporary_hold: Optional[bool] = None,
        customer_encryption: Optional[CustomerEncryption]=None,
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
            if event_based_hold is not None:
                kwargs['event_based_hold'] = event_based_hold
            if id is not None:
                kwargs['id'] = id
            if kms_key_name is not None:
                kwargs['kms_key_name'] = kms_key_name
            if metadata is not None:
                kwargs['metadata'] = metadata
            if source is not None:
                kwargs['source'] = source
            if storage_class is not None:
                kwargs['storage_class'] = storage_class
            if temporary_hold is not None:
                kwargs['temporary_hold'] = temporary_hold
            if customer_encryption is not None:
                kwargs['customer_encryption'] = customer_encryption
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
