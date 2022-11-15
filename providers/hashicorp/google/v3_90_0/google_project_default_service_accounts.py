
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




class GoogleProjectDefaultServiceAccounts(ResourceObject):
    """    
    Args:
        action (str): The action to be performed in the default service accounts. Valid values are: DEPRIVILEGE, DELETE, DISABLE.
                    				Note that DEPRIVILEGE action will ignore the REVERT configuration in the restore_policy.
        project (str): The project ID where service accounts are created.
    """
    _type = 'google_project_default_service_accounts'
    
    def __init__(self,
        tf_id: str,
        action:str,
        project:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        restore_policy: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if action is not None:
                kwargs['action'] = action
            if project is not None:
                kwargs['project'] = project
            if id is not None:
                kwargs['id'] = id
            if restore_policy is not None:
                kwargs['restore_policy'] = restore_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
