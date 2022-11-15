
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




class GoogleHealthcareConsentStore(ResourceObject):
    """    
    Args:
        dataset (str): Identifies the dataset addressed by this request. Must be in the format
                    'projects/{project}/locations/{location}/datasets/{dataset}'
        name (str): The name of this ConsentStore, for example:
                    "consent1"
    """
    _type = 'google_healthcare_consent_store'
    
    def __init__(self,
        tf_id: str,
        dataset:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        default_consent_ttl: Optional[str] = None,
        enable_consent_create_on_update: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dataset is not None:
                kwargs['dataset'] = dataset
            if name is not None:
                kwargs['name'] = name
            if default_consent_ttl is not None:
                kwargs['default_consent_ttl'] = default_consent_ttl
            if enable_consent_create_on_update is not None:
                kwargs['enable_consent_create_on_update'] = enable_consent_create_on_update
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
