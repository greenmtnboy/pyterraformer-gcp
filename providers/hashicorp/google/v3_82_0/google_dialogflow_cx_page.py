
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
class InitialPromptFulfillmentItem():
        # non-optional-blocks
        return_partial_responses: Optional[bool] = None
        tag: Optional[str] = None
        webhook: Optional[str] = None
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        
# wrapper list class
class InitialPromptFulfillment(BlockList):
        items: List[InitialPromptFulfillmentItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FillBehaviorItem():
        # non-optional-blocks
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        initial_prompt_fulfillment: Optional[InitialPromptFulfillment]=None,
        
# wrapper list class
class FillBehavior(BlockList):
        items: List[FillBehaviorItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ParametersItem():
        # non-optional-blocks
        display_name: Optional[str] = None
        entity_type: Optional[str] = None
        is_list: Optional[bool] = None
        redact: Optional[bool] = None
        required: Optional[bool] = None
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        initial_prompt_fulfillment: Optional[InitialPromptFulfillment]=None,
        fill_behavior: Optional[FillBehavior]=None,
        
# wrapper list class
class Parameters(BlockList):
        items: List[ParametersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EntryFulfillmentItem():
        # non-optional-blocks
        return_partial_responses: Optional[bool] = None
        tag: Optional[str] = None
        webhook: Optional[str] = None
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        
# wrapper list class
class EntryFulfillment(BlockList):
        items: List[EntryFulfillmentItem]




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
class FormItem():
        # non-optional-blocks
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        initial_prompt_fulfillment: Optional[InitialPromptFulfillment]=None,
        fill_behavior: Optional[FillBehavior]=None,
        parameters: Optional[Parameters]=None,
        
# wrapper list class
class Form(BlockList):
        items: List[FormItem]




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




class GoogleDialogflowCxPage(ResourceObject):
    """    
    Args:
        display_name (str): The human-readable name of the page, unique within the agent.
    """
    _type = 'google_dialogflow_cx_page'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        language_code: Optional[str] = None,
        parent: Optional[str] = None,
        transition_route_groups: Optional[List[str]] = None,
        text: Optional[Text]=None,
        messages: Optional[Messages]=None,
        trigger_fulfillment: Optional[TriggerFulfillment]=None,
        initial_prompt_fulfillment: Optional[InitialPromptFulfillment]=None,
        fill_behavior: Optional[FillBehavior]=None,
        parameters: Optional[Parameters]=None,
        entry_fulfillment: Optional[EntryFulfillment]=None,
        event_handlers: Optional[EventHandlers]=None,
        form: Optional[Form]=None,
        timeouts: Optional[Timeouts]=None,
        transition_routes: Optional[TransitionRoutes]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
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
            if initial_prompt_fulfillment is not None:
                kwargs['initial_prompt_fulfillment'] = initial_prompt_fulfillment
            if fill_behavior is not None:
                kwargs['fill_behavior'] = fill_behavior
            if parameters is not None:
                kwargs['parameters'] = parameters
            if entry_fulfillment is not None:
                kwargs['entry_fulfillment'] = entry_fulfillment
            if event_handlers is not None:
                kwargs['event_handlers'] = event_handlers
            if form is not None:
                kwargs['form'] = form
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if transition_routes is not None:
                kwargs['transition_routes'] = transition_routes
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
