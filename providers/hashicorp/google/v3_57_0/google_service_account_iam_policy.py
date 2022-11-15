
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleServiceAccountIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        service_account_id (str): 
    """
    _type = 'google_service_account_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        service_account_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if service_account_id is not None:
                kwargs['service_account_id'] = service_account_id
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
