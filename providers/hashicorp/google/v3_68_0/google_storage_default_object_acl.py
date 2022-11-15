
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleStorageDefaultObjectAcl(ResourceObject):
    """    
    Args:
        bucket (str): 
    """
    _type = 'google_storage_default_object_acl'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        role_entity: Optional[Set[str]] = None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if id is not None:
                kwargs['id'] = id
            if role_entity is not None:
                kwargs['role_entity'] = role_entity
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
