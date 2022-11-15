
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




class GoogleDialogflowAgent(ResourceObject):
    """    
    Args:
        default_language_code (str): The default language of the agent as a language tag. [See Language Support](https://cloud.google.com/dialogflow/docs/reference/language) 
                    for a list of the currently supported language codes. This field cannot be updated after creation.
        display_name (str): The name of this agent.
        time_zone (str): The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York,
                    Europe/Paris.
    """
    _type = 'google_dialogflow_agent'
    
    def __init__(self,
        tf_id: str,
        default_language_code:str,
        display_name:str,
        time_zone:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        api_version: Optional[str] = None,
        avatar_uri: Optional[str] = None,
        classification_threshold: Optional[float] = None,
        description: Optional[str] = None,
        enable_logging: Optional[bool] = None,
        id: Optional[str] = None,
        match_mode: Optional[str] = None,
        project: Optional[str] = None,
        supported_language_codes: Optional[List[str]] = None,
        tier: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if default_language_code is not None:
                kwargs['default_language_code'] = default_language_code
            if display_name is not None:
                kwargs['display_name'] = display_name
            if time_zone is not None:
                kwargs['time_zone'] = time_zone
            if api_version is not None:
                kwargs['api_version'] = api_version
            if avatar_uri is not None:
                kwargs['avatar_uri'] = avatar_uri
            if classification_threshold is not None:
                kwargs['classification_threshold'] = classification_threshold
            if description is not None:
                kwargs['description'] = description
            if enable_logging is not None:
                kwargs['enable_logging'] = enable_logging
            if id is not None:
                kwargs['id'] = id
            if match_mode is not None:
                kwargs['match_mode'] = match_mode
            if project is not None:
                kwargs['project'] = project
            if supported_language_codes is not None:
                kwargs['supported_language_codes'] = supported_language_codes
            if tier is not None:
                kwargs['tier'] = tier
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
