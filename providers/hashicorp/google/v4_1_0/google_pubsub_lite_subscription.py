
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DeliveryConfigItem():
        delivery_requirement:str
        # non-optional-blocks
        
# wrapper list class
class DeliveryConfig(BlockList):
        items: List[DeliveryConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePubsubLiteSubscription(ResourceObject):
    """    
    Args:
        name (str): Name of the subscription.
        topic (str): A reference to a Topic resource.
    """
    _type = 'google_pubsub_lite_subscription'
    
    def __init__(self,
        tf_id: str,
        name:str,
        topic:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        zone: Optional[str] = None,
        delivery_config: Optional[DeliveryConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if topic is not None:
                kwargs['topic'] = topic
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if zone is not None:
                kwargs['zone'] = zone
            if delivery_config is not None:
                kwargs['delivery_config'] = delivery_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
