
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




# this block can contain multiple items, items in a list are required
@dataclass 
class VersionConfigsItem():
        version:str
        # non-optional-blocks
        
# wrapper list class
class VersionConfigs(BlockList):
        items: List[VersionConfigsItem]




class GoogleDialogflowCxEnvironment(ResourceObject):
    """    
    Args:
        display_name (str): The human-readable name of the environment (unique in an agent). Limit of 64 characters.
    """
    _type = 'google_dialogflow_cx_environment'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        parent: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        version_configs: Optional[VersionConfigs]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if parent is not None:
                kwargs['parent'] = parent
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if version_configs is not None:
                kwargs['version_configs'] = version_configs
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
