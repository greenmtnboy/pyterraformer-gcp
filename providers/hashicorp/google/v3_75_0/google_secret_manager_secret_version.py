
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




class GoogleSecretManagerSecretVersion(ResourceObject):
    """    
    Args:
        secret (str): Secret Manager secret resource
        secret_data (str): The secret data. Must be no larger than 64KiB.
    """
    _type = 'google_secret_manager_secret_version'
    
    def __init__(self,
        tf_id: str,
        secret:str,
        secret_data:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if secret is not None:
                kwargs['secret'] = secret
            if secret_data is not None:
                kwargs['secret_data'] = secret_data
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
