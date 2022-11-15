
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleStorageNotification(ResourceObject):
    """    
    Args:
        bucket (str): 
        payload_format (str): 
        topic (str): 
    """
    _type = 'google_storage_notification'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        payload_format:str,
        topic:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        custom_attributes: Optional[Dict[str, str]] = None,
        event_types: Optional[Set[str]] = None,
        id: Optional[str] = None,
        object_name_prefix: Optional[str] = None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if payload_format is not None:
                kwargs['payload_format'] = payload_format
            if topic is not None:
                kwargs['topic'] = topic
            if custom_attributes is not None:
                kwargs['custom_attributes'] = custom_attributes
            if event_types is not None:
                kwargs['event_types'] = event_types
            if id is not None:
                kwargs['id'] = id
            if object_name_prefix is not None:
                kwargs['object_name_prefix'] = object_name_prefix
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
