
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




class GoogleOsLoginSshPublicKey(ResourceObject):
    """    
    Args:
        key (str): Public key text in SSH format, defined by RFC4253 section 6.6.
        user (str): The user email.
    """
    _type = 'google_os_login_ssh_public_key'
    
    def __init__(self,
        tf_id: str,
        key:str,
        user:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        expiration_time_usec: Optional[str] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if key is not None:
                kwargs['key'] = key
            if user is not None:
                kwargs['user'] = user
            if expiration_time_usec is not None:
                kwargs['expiration_time_usec'] = expiration_time_usec
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
