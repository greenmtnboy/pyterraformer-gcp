
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleAccessContextManagerAccessPolicyIamPolicy(ResourceObject):
    """    
    Args:
        name (str): 
        policy_data (str): 
    """
    _type = 'google_access_context_manager_access_policy_iam_policy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        policy_data:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
