
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ManagedItem():
        domains:List[str]
        # non-optional-blocks
        
# wrapper list class
class Managed(BlockList):
        items: List[ManagedItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleComputeManagedSslCertificate(ResourceObject):
    """    
    Args:
    """
    _type = 'google_compute_managed_ssl_certificate'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        certificate_id: Optional[float] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        type: Optional[str] = None,
        managed: Optional[Managed]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if certificate_id is not None:
                kwargs['certificate_id'] = certificate_id
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if type is not None:
                kwargs['type'] = type
            if managed is not None:
                kwargs['managed'] = managed
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
