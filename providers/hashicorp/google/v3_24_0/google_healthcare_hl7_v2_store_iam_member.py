
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleHealthcareHl7V2StoreIamMember(ResourceObject):
    """    
    Args:
        hl7_v2_store_id (str): 
        member (str): 
        role (str): 
    """
    _type = 'google_healthcare_hl7_v2_store_iam_member'
    
    def __init__(self,
        tf_id: str,
        hl7_v2_store_id:str,
        member:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if hl7_v2_store_id is not None:
                kwargs['hl7_v2_store_id'] = hl7_v2_store_id
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
