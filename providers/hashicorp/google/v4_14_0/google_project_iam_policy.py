
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleProjectIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        project (str): 
    """
    _type = 'google_project_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        project:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if project is not None:
                kwargs['project'] = project
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
