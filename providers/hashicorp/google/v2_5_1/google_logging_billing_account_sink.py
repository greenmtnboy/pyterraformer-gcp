
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleLoggingBillingAccountSink(ResourceObject):
    """    
    Args:
        billing_account (str): 
        destination (str): 
        name (str): 
    """
    _type = 'google_logging_billing_account_sink'
    
    def __init__(self,
        tf_id: str,
        billing_account:str,
        destination:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if billing_account is not None:
                kwargs['billing_account'] = billing_account
            if destination is not None:
                kwargs['destination'] = destination
            if name is not None:
                kwargs['name'] = name
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
