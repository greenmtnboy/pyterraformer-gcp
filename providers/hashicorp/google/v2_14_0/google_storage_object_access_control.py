
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
        update: Optional[str] = None




class GoogleStorageObjectAccessControl(ResourceObject):
    """    
    Args:
        bucket (str): 
        entity (str): 
        object (str): 
        role (str): 
    """
    _type = 'google_storage_object_access_control'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        entity:str,
        object:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if entity is not None:
                kwargs['entity'] = entity
            if object is not None:
                kwargs['object'] = object
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
