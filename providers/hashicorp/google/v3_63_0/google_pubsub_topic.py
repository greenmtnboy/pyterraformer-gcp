
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class MessageStoragePolicyItem():
        allowed_persistence_regions:List[str]
        # non-optional-blocks
        
# wrapper list class
class MessageStoragePolicy(BlockList):
        items: List[MessageStoragePolicyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePubsubTopic(ResourceObject):
    """    
    Args:
        name (str): Name of the topic.
    """
    _type = 'google_pubsub_topic'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        kms_key_name: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        message_storage_policy: Optional[MessageStoragePolicy]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if kms_key_name is not None:
                kwargs['kms_key_name'] = kms_key_name
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if message_storage_policy is not None:
                kwargs['message_storage_policy'] = message_storage_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
