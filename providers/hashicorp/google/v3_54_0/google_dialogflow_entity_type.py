
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class EntitiesItem():
        synonyms:List[str]
        value:str
        # non-optional-blocks
        
# wrapper list class
class Entities(BlockList):
        items: List[EntitiesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDialogflowEntityType(ResourceObject):
    """    
    Args:
        display_name (str): The name of this entity type to be displayed on the console.
        kind (str): Indicates the kind of entity type.
                    * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
                    * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
                    types can contain references to other entity types (with or without aliases).
                    * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values. Possible values: ["KIND_MAP", "KIND_LIST", "KIND_REGEXP"]
    """
    _type = 'google_dialogflow_entity_type'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        kind:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enable_fuzzy_extraction: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        entities: Optional[Entities]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if kind is not None:
                kwargs['kind'] = kind
            if enable_fuzzy_extraction is not None:
                kwargs['enable_fuzzy_extraction'] = enable_fuzzy_extraction
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if entities is not None:
                kwargs['entities'] = entities
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
