
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleServiceAccount(ResourceObject):
    """    
    Args:
        account_id (str): 
    """
    _type = 'google_service_account'
    
    def __init__(self,
        tf_id: str,
        account_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        policy_data: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if account_id is not None:
                kwargs['account_id'] = account_id
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
