
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleKmsCryptoKeyIamPolicy(ResourceObject):
    """    
    Args:
        crypto_key_id (str): 
        policy_data (str): 
    """
    _type = 'google_kms_crypto_key_iam_policy'
    
    def __init__(self,
        tf_id: str,
        crypto_key_id:str,
        policy_data:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if crypto_key_id is not None:
                kwargs['crypto_key_id'] = crypto_key_id
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
