
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleKmsKeyRingIamBinding(ResourceObject):
    """    
    Args:
        key_ring_id (str): 
        members (Set[str]): 
        role (str): 
    """
    _type = 'google_kms_key_ring_iam_binding'
    
    def __init__(self,
        tf_id: str,
        key_ring_id:str,
        members:Set[str],
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if key_ring_id is not None:
                kwargs['key_ring_id'] = key_ring_id
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
