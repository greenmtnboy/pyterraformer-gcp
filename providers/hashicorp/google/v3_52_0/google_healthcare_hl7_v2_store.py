
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NotificationConfigItem():
        pubsub_topic:str
        # non-optional-blocks
        
# wrapper list class
class NotificationConfig(BlockList):
        items: List[NotificationConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NotificationConfigsItem():
        pubsub_topic:str
        # non-optional-blocks
        filter: Optional[str] = None
        
# wrapper list class
class NotificationConfigs(BlockList):
        items: List[NotificationConfigsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ParserConfigItem():
        # non-optional-blocks
        allow_null_header: Optional[bool] = None
        schema: Optional[str] = None
        segment_terminator: Optional[str] = None
        
# wrapper list class
class ParserConfig(BlockList):
        items: List[ParserConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleHealthcareHl7V2Store(ResourceObject):
    """    
    Args:
        dataset (str): Identifies the dataset addressed by this request. Must be in the format
                    'projects/{project}/locations/{location}/datasets/{dataset}'
        name (str): The resource name for the Hl7V2Store.

                    ** Changing this property may recreate the Hl7v2 store (removing all data) **
    """
    _type = 'google_healthcare_hl7_v2_store'
    
    def __init__(self,
        tf_id: str,
        dataset:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        notification_config: Optional[NotificationConfig]=None,
        notification_configs: Optional[NotificationConfigs]=None,
        parser_config: Optional[ParserConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dataset is not None:
                kwargs['dataset'] = dataset
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if notification_config is not None:
                kwargs['notification_config'] = notification_config
            if notification_configs is not None:
                kwargs['notification_configs'] = notification_configs
            if parser_config is not None:
                kwargs['parser_config'] = parser_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
