
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class EntitiesItem():
        # non-optional-blocks
        synonyms: Optional[List[str]] = None
        value: Optional[str] = None
        
# wrapper list class
class Entities(BlockList):
        items: List[EntitiesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExcludedPhrasesItem():
        # non-optional-blocks
        value: Optional[str] = None
        
# wrapper list class
class ExcludedPhrases(BlockList):
        items: List[ExcludedPhrasesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDialogflowCxEntityType(ResourceObject):
    """    
    Args:
        display_name (str): The human-readable name of the entity type, unique within the agent.
        kind (str): Indicates whether the entity type can be automatically expanded.
                    * KIND_MAP: Map entity types allow mapping of a group of synonyms to a canonical value.
                    * KIND_LIST: List entity types contain a set of entries that do not map to canonical values. However, list entity types can contain references to other entity types (with or without aliases).
                    * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values. Possible values: ["KIND_MAP", "KIND_LIST", "KIND_REGEXP"]
    """
    _type = 'google_dialogflow_cx_entity_type'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        kind:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        auto_expansion_mode: Optional[str] = None,
        enable_fuzzy_extraction: Optional[bool] = None,
        id: Optional[str] = None,
        language_code: Optional[str] = None,
        parent: Optional[str] = None,
        redact: Optional[bool] = None,
        entities: Optional[Entities]=None,
        excluded_phrases: Optional[ExcludedPhrases]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if kind is not None:
                kwargs['kind'] = kind
            if auto_expansion_mode is not None:
                kwargs['auto_expansion_mode'] = auto_expansion_mode
            if enable_fuzzy_extraction is not None:
                kwargs['enable_fuzzy_extraction'] = enable_fuzzy_extraction
            if id is not None:
                kwargs['id'] = id
            if language_code is not None:
                kwargs['language_code'] = language_code
            if parent is not None:
                kwargs['parent'] = parent
            if redact is not None:
                kwargs['redact'] = redact
            if entities is not None:
                kwargs['entities'] = entities
            if excluded_phrases is not None:
                kwargs['excluded_phrases'] = excluded_phrases
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
