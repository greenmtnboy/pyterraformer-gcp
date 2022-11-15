
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleProjectServices(ResourceObject):
    """    
    Args:
        services (Set[str]): 
    """
    _type = 'google_project_services'
    
    def __init__(self,
        tf_id: str,
        services:Set[str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        disable_on_destroy: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if services is not None:
                kwargs['services'] = services
            if disable_on_destroy is not None:
                kwargs['disable_on_destroy'] = disable_on_destroy
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
