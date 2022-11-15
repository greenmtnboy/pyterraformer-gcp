
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FieldsItem():
        # non-optional-blocks
        array_config: Optional[str] = None
        field_path: Optional[str] = None
        order: Optional[str] = None
        
# wrapper list class
class Fields(BlockList):
        items: List[FieldsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleFirestoreIndex(ResourceObject):
    """    
    Args:
        collection (str): 
    """
    _type = 'google_firestore_index'
    
    def __init__(self,
        tf_id: str,
        collection:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        database: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        query_scope: Optional[str] = None,
        fields: Optional[Fields]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if collection is not None:
                kwargs['collection'] = collection
            if database is not None:
                kwargs['database'] = database
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if query_scope is not None:
                kwargs['query_scope'] = query_scope
            if fields is not None:
                kwargs['fields'] = fields
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
