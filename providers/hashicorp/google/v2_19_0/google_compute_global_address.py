
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




class GoogleComputeGlobalAddress(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_compute_global_address'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        address: Optional[str] = None,
        address_type: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ip_version: Optional[str] = None,
        network: Optional[str] = None,
        prefix_length: Optional[float] = None,
        project: Optional[str] = None,
        purpose: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if address is not None:
                kwargs['address'] = address
            if address_type is not None:
                kwargs['address_type'] = address_type
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ip_version is not None:
                kwargs['ip_version'] = ip_version
            if network is not None:
                kwargs['network'] = network
            if prefix_length is not None:
                kwargs['prefix_length'] = prefix_length
            if project is not None:
                kwargs['project'] = project
            if purpose is not None:
                kwargs['purpose'] = purpose
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
