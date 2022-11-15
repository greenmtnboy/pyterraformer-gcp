
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeSharedVpcServiceProject(ResourceObject):
    """    
    Args:
        host_project (str): 
        service_project (str): 
    """
    _type = 'google_compute_shared_vpc_service_project'
    
    def __init__(self,
        tf_id: str,
        host_project:str,
        service_project:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if host_project is not None:
                kwargs['host_project'] = host_project
            if service_project is not None:
                kwargs['service_project'] = service_project
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
