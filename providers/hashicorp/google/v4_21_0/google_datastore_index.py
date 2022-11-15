
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PropertiesItem():
        direction:str
        name:str
        # non-optional-blocks
        
# wrapper list class
class Properties(BlockList):
        items: List[PropertiesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleDatastoreIndex(ResourceObject):
    """    
    Args:
        kind (str): The entity kind which the index applies to.
    """
    _type = 'google_datastore_index'
    
    def __init__(self,
        tf_id: str,
        kind:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        ancestor: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        properties: Optional[Properties]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if kind is not None:
                kwargs['kind'] = kind
            if ancestor is not None:
                kwargs['ancestor'] = ancestor
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if properties is not None:
                kwargs['properties'] = properties
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
