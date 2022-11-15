
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleSourcerepoRepositoryIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        repository (str): 
        role (str): 
    """
    _type = 'google_sourcerepo_repository_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        repository:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if repository is not None:
                kwargs['repository'] = repository
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
