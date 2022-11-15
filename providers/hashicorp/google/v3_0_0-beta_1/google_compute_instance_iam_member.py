
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeInstanceIamMember(ResourceObject):
    """    
    Args:
        instance_name (str): 
        member (str): 
        role (str): 
    """
    _type = 'google_compute_instance_iam_member'
    
    def __init__(self,
        tf_id: str,
        instance_name:str,
        member:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        ):
            kwargs = {}
            if instance_name is not None:
                kwargs['instance_name'] = instance_name
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
