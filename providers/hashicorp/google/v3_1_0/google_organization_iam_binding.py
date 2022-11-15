
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleOrganizationIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        org_id (str): 
        role (str): 
    """
    _type = 'google_organization_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        org_id:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if org_id is not None:
                kwargs['org_id'] = org_id
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
