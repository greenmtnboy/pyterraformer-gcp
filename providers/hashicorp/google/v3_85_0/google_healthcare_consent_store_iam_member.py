
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionItem():
        expression:str
        title:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class Condition(BlockList):
        items: List[ConditionItem]




class GoogleHealthcareConsentStoreIamMember(ResourceObject):
    """    
    Args:
        consent_store_id (str): 
        dataset (str): 
        member (str): 
        role (str): 
    """
    _type = 'google_healthcare_consent_store_iam_member'
    
    def __init__(self,
        tf_id: str,
        consent_store_id:str,
        dataset:str,
        member:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if consent_store_id is not None:
                kwargs['consent_store_id'] = consent_store_id
            if dataset is not None:
                kwargs['dataset'] = dataset
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
