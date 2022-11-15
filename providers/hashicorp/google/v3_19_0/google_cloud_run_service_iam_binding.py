
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleCloudRunServiceIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        role (str): 
        service (str): 
    """
    _type = 'google_cloud_run_service_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        role:str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
