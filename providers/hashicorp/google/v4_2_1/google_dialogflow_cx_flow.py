
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class TextItem():
        # non-optional-blocks
        text: Optional[List[str]] = None
        
# wrapper list class
class Text(BlockList):
        items: List[TextItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MessagesItem():
        # non-optional-blocks
        text: Optional[Text]=None,
        
# wrapper list class
class Messages(BlockList):
        items: List[MessagesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TriggerFulfillmentItem():
        # non-optional-blocks
        return_partial_responses: Optional[bool] = None
        tag: Optional[str] = None
        webhook: Optional[str] = None
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        
# wrapper list class
class TriggerFulfillment(BlockList):
        items: List[TriggerFulfillmentItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EventHandlersItem():
        # non-optional-blocks
        event: Optional[str] = None
        target_flow: Optional[str] = None
        target_page: Optional[str] = None
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        trigger_fulfillment: Optional[TriggerFulfillment]=None,
        
# wrapper list class
class EventHandlers(BlockList):
        items: List[EventHandlersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NluSettingsItem():
        # non-optional-blocks
        classification_threshold: Optional[float] = None
        model_training_mode: Optional[str] = None
        model_type: Optional[str] = None
        
# wrapper list class
class NluSettings(BlockList):
        items: List[NluSettingsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TransitionRoutesItem():
        # non-optional-blocks
        condition: Optional[str] = None
        intent: Optional[str] = None
        target_flow: Optional[str] = None
        target_page: Optional[str] = None
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        trigger_fulfillment: Optional[TriggerFulfillment]=None,
        
# wrapper list class
class TransitionRoutes(BlockList):
        items: List[TransitionRoutesItem]




class GoogleDialogflowCxFlow(ResourceObject):
    """    
    Args:
        display_name (str): The human-readable name of the flow.
    """
    _type = 'google_dialogflow_cx_flow'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        language_code: Optional[str] = None,
        parent: Optional[str] = None,
        transition_route_groups: Optional[List[str]] = None,
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        trigger_fulfillment: Optional[TriggerFulfillment]=None,
        event_handlers: Optional[EventHandlers]=None,
        nlu_settings: Optional[NluSettings]=None,
        timeouts: Optional[Timeouts]=None,
        transition_routes: Optional[TransitionRoutes]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if language_code is not None:
                kwargs['language_code'] = language_code
            if parent is not None:
                kwargs['parent'] = parent
            if transition_route_groups is not None:
                kwargs['transition_route_groups'] = transition_route_groups
            if text is not None:
                kwargs['text'] = text
            if messages is not None:
                kwargs['messages'] = messages
            if trigger_fulfillment is not None:
                kwargs['trigger_fulfillment'] = trigger_fulfillment
            if event_handlers is not None:
                kwargs['event_handlers'] = event_handlers
            if nlu_settings is not None:
                kwargs['nlu_settings'] = nlu_settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if transition_routes is not None:
                kwargs['transition_routes'] = transition_routes
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
