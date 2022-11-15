
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




class GoogleComputeSslCertificate(ResourceObject):
    """    
    Args:
        certificate (str): 
        private_key (str): 
    """
    _type = 'google_compute_ssl_certificate'
    
    def __init__(self,
        tf_id: str,
        certificate:str,
        private_key:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if certificate is not None:
                kwargs['certificate'] = certificate
            if private_key is not None:
                kwargs['private_key'] = private_key
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if name is not None:
                kwargs['name'] = name
            if name_prefix is not None:
                kwargs['name_prefix'] = name_prefix
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
