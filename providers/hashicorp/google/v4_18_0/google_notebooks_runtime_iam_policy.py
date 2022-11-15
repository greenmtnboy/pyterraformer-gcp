
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleNotebooksRuntimeIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        runtime_name (str): 
    """
    _type = 'google_notebooks_runtime_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        runtime_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if runtime_name is not None:
                kwargs['runtime_name'] = runtime_name
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
