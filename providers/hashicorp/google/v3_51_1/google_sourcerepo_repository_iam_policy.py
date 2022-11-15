
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleSourcerepoRepositoryIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        repository (str): 
    """
    _type = 'google_sourcerepo_repository_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        repository:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if repository is not None:
                kwargs['repository'] = repository
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
