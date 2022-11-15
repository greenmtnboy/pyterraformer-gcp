
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleLoggingBillingAccountExclusion(ResourceObject):
    """    
    Args:
        billing_account (str): 
        filter (str): The filter to apply when excluding logs. Only log entries that match the filter are excluded.
        name (str): The name of the logging exclusion.
    """
    _type = 'google_logging_billing_account_exclusion'
    
    def __init__(self,
        tf_id: str,
        billing_account:str,
        filter:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if billing_account is not None:
                kwargs['billing_account'] = billing_account
            if filter is not None:
                kwargs['filter'] = filter
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
