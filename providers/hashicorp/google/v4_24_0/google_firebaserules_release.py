
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
        update: Optional[str] = None




class GoogleFirebaserulesRelease(ResourceObject):
    """    
    Args:
        name (str): Format: `projects/{project_id}/releases/{release_id}`
        ruleset_name (str): Name of the `Ruleset` referred to by this `Release`. The `Ruleset` must exist the `Release` to be created.
    """
    _type = 'google_firebaserules_release'
    
    def __init__(self,
        tf_id: str,
        name:str,
        ruleset_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if ruleset_name is not None:
                kwargs['ruleset_name'] = ruleset_name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
