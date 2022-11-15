
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleBillingSubaccount(ResourceObject):
    """    
    Args:
        display_name (str): 
        master_billing_account (str): 
    """
    _type = 'google_billing_subaccount'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        master_billing_account:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        deletion_policy: Optional[str] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if master_billing_account is not None:
                kwargs['master_billing_account'] = master_billing_account
            if deletion_policy is not None:
                kwargs['deletion_policy'] = deletion_policy
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
