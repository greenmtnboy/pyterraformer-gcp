
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
        update: Optional[str] = None




class GoogleStorageHmacKey(ResourceObject):
    """    
    Args:
        service_account_email (str): The email address of the key's associated service account.
    """
    _type = 'google_storage_hmac_key'
    
    def __init__(self,
        tf_id: str,
        service_account_email:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        state: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if service_account_email is not None:
                kwargs['service_account_email'] = service_account_email
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if state is not None:
                kwargs['state'] = state
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
