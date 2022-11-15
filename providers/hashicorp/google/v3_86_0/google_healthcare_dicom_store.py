
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




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleHealthcareDicomStore(ResourceObject):
    """    
    Args:
        dataset (str): Identifies the dataset addressed by this request. Must be in the format
                    'projects/{project}/locations/{location}/datasets/{dataset}'
        name (str): The resource name for the DicomStore.

                    ** Changing this property may recreate the Dicom store (removing all data) **
    """
    _type = 'google_healthcare_dicom_store'
    
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
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
