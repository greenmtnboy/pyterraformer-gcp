
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SensitiveLabelsItem():
        # non-optional-blocks
        auth_token: Optional[str] = None
        password: Optional[str] = None
        service_key: Optional[str] = None
        
# wrapper list class
class SensitiveLabels(BlockList):
        items: List[SensitiveLabelsItem]




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
        type (str): The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of valid values such as "email", "slack", etc...
    """
    _type = 'google_monitoring_notification_channel'
    
    def __init__(self,
        tf_id: str,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        user_labels: Optional[Dict[str, str]] = None,
        sensitive_labels: Optional[SensitiveLabels]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if type is not None:
                kwargs['type'] = type
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
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
            if sensitive_labels is not None:
                kwargs['sensitive_labels'] = sensitive_labels
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
