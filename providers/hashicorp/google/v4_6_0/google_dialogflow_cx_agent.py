
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SpeechToTextSettingsItem():
        # non-optional-blocks
        enable_speech_adaptation: Optional[bool] = None
        
# wrapper list class
class SpeechToTextSettings(BlockList):
        items: List[SpeechToTextSettingsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDialogflowCxAgent(ResourceObject):
    """    
    Args:
        default_language_code (str): The default language of the agent as a language tag. [See Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) 
                    for a list of the currently supported language codes. This field cannot be updated after creation.
        display_name (str): The human-readable name of the agent, unique within the location.
        location (str): The name of the location this agent is located in.

                    ~> **Note:** The first time you are deploying an Agent in your project you must configure location settings.
                     This is a one time step but at the moment you can only [configure location settings](https://cloud.google.com/dialogflow/cx/docs/concept/region#location-settings) via the Dialogflow CX console.
                     Another options is to use global location so you don't need to manually configure location settings.
        time_zone (str): The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York,
                    Europe/Paris.
    """
    _type = 'google_dialogflow_cx_agent'
    
    def __init__(self,
        tf_id: str,
        default_language_code:str,
        display_name:str,
        location:str,
        time_zone:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        avatar_uri: Optional[str] = None,
        description: Optional[str] = None,
        enable_spell_correction: Optional[bool] = None,
        enable_stackdriver_logging: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        security_settings: Optional[str] = None,
        supported_language_codes: Optional[List[str]] = None,
        speech_to_text_settings: Optional[SpeechToTextSettings]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if default_language_code is not None:
                kwargs['default_language_code'] = default_language_code
            if display_name is not None:
                kwargs['display_name'] = display_name
            if location is not None:
                kwargs['location'] = location
            if time_zone is not None:
                kwargs['time_zone'] = time_zone
            if avatar_uri is not None:
                kwargs['avatar_uri'] = avatar_uri
            if description is not None:
                kwargs['description'] = description
            if enable_spell_correction is not None:
                kwargs['enable_spell_correction'] = enable_spell_correction
            if enable_stackdriver_logging is not None:
                kwargs['enable_stackdriver_logging'] = enable_stackdriver_logging
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if security_settings is not None:
                kwargs['security_settings'] = security_settings
            if supported_language_codes is not None:
                kwargs['supported_language_codes'] = supported_language_codes
            if speech_to_text_settings is not None:
                kwargs['speech_to_text_settings'] = speech_to_text_settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
