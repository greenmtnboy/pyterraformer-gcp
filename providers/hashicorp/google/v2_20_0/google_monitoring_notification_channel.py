
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




class GoogleMonitoringNotificationChannel(ResourceObject):
    """    
    Args:
        display_name (str): An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.
        type (str): The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of valid values such as "email", "slack", etc...
    """
    _type = 'google_monitoring_notification_channel'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        user_labels: Optional[Dict[str, str]] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if type is not None:
                kwargs['type'] = type
            if description is not None:
                kwargs['description'] = description
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if user_labels is not None:
                kwargs['user_labels'] = user_labels
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
