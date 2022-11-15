
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PartsItem():
        text:str
        # non-optional-blocks
        parameter_id: Optional[str] = None
        
# wrapper list class
class Parts(BlockList):
        items: List[PartsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ParametersItem():
        entity_type:str
        id:str
        # non-optional-blocks
        is_list: Optional[bool] = None
        redact: Optional[bool] = None
        
# wrapper list class
class Parameters(BlockList):
        items: List[ParametersItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TrainingPhrasesItem():
        # non-optional-blocks
        repeat_count: Optional[float] = None
        parts: Optional[Parts]=None,
        
# wrapper list class
class TrainingPhrases(BlockList):
        items: List[TrainingPhrasesItem]




class GoogleDialogflowCxIntent(ResourceObject):
    """    
    Args:
        display_name (str): The human-readable name of the intent, unique within the agent.
    """
    _type = 'google_dialogflow_cx_intent'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        is_fallback: Optional[bool] = None,
        labels: Optional[Dict[str, str]] = None,
        language_code: Optional[str] = None,
        parent: Optional[str] = None,
        priority: Optional[float] = None,
        parts: Optional[Parts]=None,
        parameters: Optional[Parameters]=None,
        timeouts: Optional[Timeouts]=None,
        training_phrases: Optional[TrainingPhrases]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if is_fallback is not None:
                kwargs['is_fallback'] = is_fallback
            if labels is not None:
                kwargs['labels'] = labels
            if language_code is not None:
                kwargs['language_code'] = language_code
            if parent is not None:
                kwargs['parent'] = parent
            if priority is not None:
                kwargs['priority'] = priority
            if parts is not None:
                kwargs['parts'] = parts
            if parameters is not None:
                kwargs['parameters'] = parameters
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if training_phrases is not None:
                kwargs['training_phrases'] = training_phrases
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
