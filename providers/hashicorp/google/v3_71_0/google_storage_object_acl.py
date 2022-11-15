
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleStorageObjectAcl(ResourceObject):
    """    
    Args:
        bucket (str): 
        object (str): 
    """
    _type = 'google_storage_object_acl'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        object:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        predefined_acl: Optional[str] = None,
        role_entity: Optional[Set[str]] = None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if object is not None:
                kwargs['object'] = object
            if id is not None:
                kwargs['id'] = id
            if predefined_acl is not None:
                kwargs['predefined_acl'] = predefined_acl
            if role_entity is not None:
                kwargs['role_entity'] = role_entity
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
