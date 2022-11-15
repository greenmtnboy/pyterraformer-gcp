
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




class GoogleIapClient(ResourceObject):
    """    
    Args:
        brand (str): Identifier of the brand to which this client
                    is attached to. The format is
                    'projects/{project_number}/brands/{brand_id}/identityAwareProxyClients/{client_id}'.
        display_name (str): Human-friendly name given to the OAuth client.
    """
    _type = 'google_iap_client'
    
    def __init__(self,
        tf_id: str,
        brand:str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if brand is not None:
                kwargs['brand'] = brand
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
