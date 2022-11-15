
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleServiceAccountKey(ResourceObject):
    """    
    Args:
        service_account_id (str): 
    """
    _type = 'google_service_account_key'
    
    def __init__(self,
        tf_id: str,
        service_account_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        key_algorithm: Optional[str] = None,
        pgp_key: Optional[str] = None,
        private_key_type: Optional[str] = None,
        public_key_type: Optional[str] = None,
        ):
            kwargs = {}
            if service_account_id is not None:
                kwargs['service_account_id'] = service_account_id
            if id is not None:
                kwargs['id'] = id
            if key_algorithm is not None:
                kwargs['key_algorithm'] = key_algorithm
            if pgp_key is not None:
                kwargs['pgp_key'] = pgp_key
            if private_key_type is not None:
                kwargs['private_key_type'] = private_key_type
            if public_key_type is not None:
                kwargs['public_key_type'] = public_key_type
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
