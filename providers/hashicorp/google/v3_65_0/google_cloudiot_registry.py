
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CredentialsItem():
        public_key_certificate:Dict[str, str]
        # non-optional-blocks
        
# wrapper list class
class Credentials(BlockList):
        items: List[CredentialsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EventNotificationConfigsItem():
        pubsub_topic_name:str
        # non-optional-blocks
        subfolder_matches: Optional[str] = None
        
# wrapper list class
class EventNotificationConfigs(BlockList):
        items: List[EventNotificationConfigsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudiotRegistry(ResourceObject):
    """    
    Args:
        name (str): A unique name for the resource, required by device registry.
    """
    _type = 'google_cloudiot_registry'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        http_config: Optional[Dict[str, str]] = None,
        id: Optional[str] = None,
        log_level: Optional[str] = None,
        mqtt_config: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        state_notification_config: Optional[Dict[str, str]] = None,
        credentials: Optional[Credentials]=None,
        event_notification_configs: Optional[EventNotificationConfigs]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if http_config is not None:
                kwargs['http_config'] = http_config
            if id is not None:
                kwargs['id'] = id
            if log_level is not None:
                kwargs['log_level'] = log_level
            if mqtt_config is not None:
                kwargs['mqtt_config'] = mqtt_config
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if state_notification_config is not None:
                kwargs['state_notification_config'] = state_notification_config
            if credentials is not None:
                kwargs['credentials'] = credentials
            if event_notification_configs is not None:
                kwargs['event_notification_configs'] = event_notification_configs
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
