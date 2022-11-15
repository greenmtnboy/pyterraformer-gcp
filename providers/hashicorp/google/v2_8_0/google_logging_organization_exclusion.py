
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleLoggingOrganizationExclusion(ResourceObject):
    """    
    Args:
        filter (str): 
        name (str): 
        org_id (str): 
    """
    _type = 'google_logging_organization_exclusion'
    
    def __init__(self,
        tf_id: str,
        filter:str,
        name:str,
        org_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if filter is not None:
                kwargs['filter'] = filter
            if name is not None:
                kwargs['name'] = name
            if org_id is not None:
                kwargs['org_id'] = org_id
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
