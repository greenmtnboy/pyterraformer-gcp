
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleKmsCryptoKeyIamBinding(ResourceObject):
    """    
    Args:
        crypto_key_id (str): 
        members (Set[str]): 
        role (str): 
    """
    _type = 'google_kms_crypto_key_iam_binding'
    
    def __init__(self,
        tf_id: str,
        crypto_key_id:str,
        members:Set[str],
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if crypto_key_id is not None:
                kwargs['crypto_key_id'] = crypto_key_id
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
