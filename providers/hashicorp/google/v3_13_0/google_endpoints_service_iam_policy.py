
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleEndpointsServiceIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        service_name (str): 
    """
    _type = 'google_endpoints_service_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        service_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if service_name is not None:
                kwargs['service_name'] = service_name
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
