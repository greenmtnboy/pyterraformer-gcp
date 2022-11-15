
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleEndpointsServiceIamMember(ResourceObject):
    """    
    Args:
        member (str): 
        role (str): 
        service_name (str): 
    """
    _type = 'google_endpoints_service_iam_member'
    
    def __init__(self,
        tf_id: str,
        member:str,
        role:str,
        service_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if service_name is not None:
                kwargs['service_name'] = service_name
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
