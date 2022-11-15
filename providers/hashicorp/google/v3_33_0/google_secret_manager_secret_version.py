
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
    """
    _type = 'google_secret_manager_secret_version'
    
    def __init__(self,
        tf_id: str,
        secret:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        secret_data: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if secret is not None:
                kwargs['secret'] = secret
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if secret_data is not None:
                kwargs['secret_data'] = secret_data
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
