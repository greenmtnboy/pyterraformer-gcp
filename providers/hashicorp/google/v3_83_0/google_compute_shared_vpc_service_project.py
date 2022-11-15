
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




class GoogleComputeSharedVpcServiceProject(ResourceObject):
    """    
    Args:
        host_project (str): The ID of a host project to associate.
        service_project (str): The ID of the project that will serve as a Shared VPC service project.
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
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if host_project is not None:
                kwargs['host_project'] = host_project
            if service_project is not None:
                kwargs['service_project'] = service_project
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
