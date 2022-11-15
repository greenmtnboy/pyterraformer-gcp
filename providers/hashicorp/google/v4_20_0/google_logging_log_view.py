
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




class GoogleLoggingLogView(ResourceObject):
    """    
    Args:
        bucket (str): The bucket of the resource
        name (str): The resource name of the view. For example: `projects/my-project/locations/global/buckets/my-bucket/views/my-view`
    """
    _type = 'google_logging_log_view'
    
    def __init__(self,
        tf_id: str,
        bucket:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        parent: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if bucket is not None:
                kwargs['bucket'] = bucket
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if parent is not None:
                kwargs['parent'] = parent
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
