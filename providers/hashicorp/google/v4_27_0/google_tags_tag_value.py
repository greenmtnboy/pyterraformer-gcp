
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




class GoogleTagsTagValue(ResourceObject):
    """    
    Args:
        parent (str): Input only. The resource name of the new TagValue's parent. Must be of the form tagKeys/{tag_key_id}.
        short_name (str): Input only. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey.

                    The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.
    """
    _type = 'google_tags_tag_value'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        short_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if short_name is not None:
                kwargs['short_name'] = short_name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
