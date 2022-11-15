
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
        update: Optional[str] = None




class GoogleProjectService(ResourceObject):
    """    
    Args:
        service (str): 
    """
    _type = 'google_project_service'
    
    def __init__(self,
        tf_id: str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        disable_dependent_services: Optional[bool] = None,
        disable_on_destroy: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if service is not None:
                kwargs['service'] = service
            if disable_dependent_services is not None:
                kwargs['disable_dependent_services'] = disable_dependent_services
            if disable_on_destroy is not None:
                kwargs['disable_on_destroy'] = disable_on_destroy
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
