
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleSecretManagerSecretIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        secret_id (str): 
    """
    _type = 'google_secret_manager_secret_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        secret_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if secret_id is not None:
                kwargs['secret_id'] = secret_id
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
