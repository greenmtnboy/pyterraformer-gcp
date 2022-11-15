
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleProject(ResourceObject):
    """    
    Args:
        name (str): 
        project_id (str): 
    """
    _type = 'google_project'
    
    def __init__(self,
        tf_id: str,
        name:str,
        project_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        auto_create_network: Optional[bool] = None,
        billing_account: Optional[str] = None,
        folder_id: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        org_id: Optional[str] = None,
        policy_data: Optional[str] = None,
        skip_delete: Optional[bool] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if project_id is not None:
                kwargs['project_id'] = project_id
            if auto_create_network is not None:
                kwargs['auto_create_network'] = auto_create_network
            if billing_account is not None:
                kwargs['billing_account'] = billing_account
            if folder_id is not None:
                kwargs['folder_id'] = folder_id
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if org_id is not None:
                kwargs['org_id'] = org_id
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if skip_delete is not None:
                kwargs['skip_delete'] = skip_delete
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
