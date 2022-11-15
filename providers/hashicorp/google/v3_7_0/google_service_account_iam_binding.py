
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleServiceAccountIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        role (str): 
        service_account_id (str): 
    """
    _type = 'google_service_account_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        role:str,
        service_account_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if service_account_id is not None:
                kwargs['service_account_id'] = service_account_id
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
