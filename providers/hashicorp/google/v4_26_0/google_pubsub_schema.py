
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




class GooglePubsubSchema(ResourceObject):
    """    
    Args:
        name (str): The ID to use for the schema, which will become the final component of the schema's resource name.
    """
    _type = 'google_pubsub_schema'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        definition: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        type: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if definition is not None:
                kwargs['definition'] = definition
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if type is not None:
                kwargs['type'] = type
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
