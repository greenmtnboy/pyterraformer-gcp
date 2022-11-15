
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class StreamingConfigItem():
        filter:str
        # non-optional-blocks
        
# wrapper list class
class StreamingConfig(BlockList):
        items: List[StreamingConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleSccNotificationConfig(ResourceObject):
    """    
    Args:
        config_id (str): This must be unique within the organization.
        organization (str): The organization whose Cloud Security Command Center the Notification
                    Config lives in.
        pubsub_topic (str): The Pub/Sub topic to send notifications to. Its format is
                    "projects/[project_id]/topics/[topic]".
    """
    _type = 'google_scc_notification_config'
    
    def __init__(self,
        tf_id: str,
        config_id:str,
        organization:str,
        pubsub_topic:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        streaming_config: Optional[StreamingConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if config_id is not None:
                kwargs['config_id'] = config_id
            if organization is not None:
                kwargs['organization'] = organization
            if pubsub_topic is not None:
                kwargs['pubsub_topic'] = pubsub_topic
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if streaming_config is not None:
                kwargs['streaming_config'] = streaming_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
