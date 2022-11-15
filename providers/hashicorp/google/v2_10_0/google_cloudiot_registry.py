
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CredentialsItem():
        # non-optional-blocks
        public_key_certificate: Optional[Dict[str, str]] = None
        
# wrapper list class
class Credentials(BlockList):
        items: List[CredentialsItem]




class GoogleCloudiotRegistry(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_cloudiot_registry'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        event_notification_config: Optional[Dict[str, str]] = None,
        http_config: Optional[Dict[str, str]] = None,
        id: Optional[str] = None,
        mqtt_config: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        state_notification_config: Optional[Dict[str, str]] = None,
        credentials: Optional[Credentials]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if event_notification_config is not None:
                kwargs['event_notification_config'] = event_notification_config
            if http_config is not None:
                kwargs['http_config'] = http_config
            if id is not None:
                kwargs['id'] = id
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
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
