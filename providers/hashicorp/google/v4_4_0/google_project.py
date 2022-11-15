
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        read: Optional[str] = None
        update: Optional[str] = None




class GoogleProject(ResourceObject):
    """    
    Args:
        name (str): The display name of the project.
        project_id (str): The project ID. Changing this forces a new project to be created.
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
        skip_delete: Optional[bool] = None,
        timeouts: Optional[Timeouts]=None,
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
            if skip_delete is not None:
                kwargs['skip_delete'] = skip_delete
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
