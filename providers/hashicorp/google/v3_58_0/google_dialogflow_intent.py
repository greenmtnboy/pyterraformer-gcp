
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




class GoogleDialogflowIntent(ResourceObject):
    """    
    Args:
        display_name (str): The name of this intent to be displayed on the console.
    """
    _type = 'google_dialogflow_intent'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        action: Optional[str] = None,
        default_response_platforms: Optional[List[str]] = None,
        events: Optional[List[str]] = None,
        id: Optional[str] = None,
        input_context_names: Optional[List[str]] = None,
        is_fallback: Optional[bool] = None,
        ml_disabled: Optional[bool] = None,
        parent_followup_intent_name: Optional[str] = None,
        priority: Optional[float] = None,
        project: Optional[str] = None,
        reset_contexts: Optional[bool] = None,
        webhook_state: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if action is not None:
                kwargs['action'] = action
            if default_response_platforms is not None:
                kwargs['default_response_platforms'] = default_response_platforms
            if events is not None:
                kwargs['events'] = events
            if id is not None:
                kwargs['id'] = id
            if input_context_names is not None:
                kwargs['input_context_names'] = input_context_names
            if is_fallback is not None:
                kwargs['is_fallback'] = is_fallback
            if ml_disabled is not None:
                kwargs['ml_disabled'] = ml_disabled
            if parent_followup_intent_name is not None:
                kwargs['parent_followup_intent_name'] = parent_followup_intent_name
            if priority is not None:
                kwargs['priority'] = priority
            if project is not None:
                kwargs['project'] = project
            if reset_contexts is not None:
                kwargs['reset_contexts'] = reset_contexts
            if webhook_state is not None:
                kwargs['webhook_state'] = webhook_state
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
