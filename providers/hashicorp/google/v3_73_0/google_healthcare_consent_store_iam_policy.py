
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleHealthcareConsentStoreIamPolicy(ResourceObject):
    """    
    Args:
        consent_store_id (str): 
        dataset (str): 
        policy_data (str): 
    """
    _type = 'google_healthcare_consent_store_iam_policy'
    
    def __init__(self,
        tf_id: str,
        consent_store_id:str,
        dataset:str,
        policy_data:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if consent_store_id is not None:
                kwargs['consent_store_id'] = consent_store_id
            if dataset is not None:
                kwargs['dataset'] = dataset
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
