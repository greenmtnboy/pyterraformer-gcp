
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleIapWebBackendServiceIamMember(ResourceObject):
    """    
    Args:
        member (str): 
        role (str): 
        web_backend_service (str): 
    """
    _type = 'google_iap_web_backend_service_iam_member'
    
    def __init__(self,
        tf_id: str,
        member:str,
        role:str,
        web_backend_service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if web_backend_service is not None:
                kwargs['web_backend_service'] = web_backend_service
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
