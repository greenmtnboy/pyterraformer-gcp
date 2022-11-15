
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleOrganizationIamCustomRole(ResourceObject):
    """    
    Args:
        org_id (str): 
        permissions (Set[str]): 
        role_id (str): 
        title (str): 
    """
    _type = 'google_organization_iam_custom_role'
    
    def __init__(self,
        tf_id: str,
        org_id:str,
        permissions:Set[str],
        role_id:str,
        title:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        stage: Optional[str] = None,
        ):
            kwargs = {}
            if org_id is not None:
                kwargs['org_id'] = org_id
            if permissions is not None:
                kwargs['permissions'] = permissions
            if role_id is not None:
                kwargs['role_id'] = role_id
            if title is not None:
                kwargs['title'] = title
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if stage is not None:
                kwargs['stage'] = stage
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
