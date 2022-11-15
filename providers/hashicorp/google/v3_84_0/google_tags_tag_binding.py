
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




class GoogleTagsTagBinding(ResourceObject):
    """    
    Args:
        parent (str): The full resource name of the resource the TagValue is bound to. E.g. //cloudresourcemanager.googleapis.com/projects/123
        tag_value (str): The TagValue of the TagBinding. Must be of the form tagValues/456.
    """
    _type = 'google_tags_tag_binding'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        tag_value:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if tag_value is not None:
                kwargs['tag_value'] = tag_value
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
