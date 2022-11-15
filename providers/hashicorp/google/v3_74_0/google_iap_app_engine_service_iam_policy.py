
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleIapAppEngineServiceIamPolicy(ResourceObject):
    """    
    Args:
        app_id (str): 
        policy_data (str): 
        service (str): 
    """
    _type = 'google_iap_app_engine_service_iam_policy'
    
    def __init__(self,
        tf_id: str,
        app_id:str,
        policy_data:str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if app_id is not None:
                kwargs['app_id'] = app_id
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
