
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PublicKeyItem():
        format:str
        key:str
        # non-optional-blocks
        
# wrapper list class
class PublicKey(BlockList):
        items: List[PublicKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CredentialsItem():
        # non-optional-blocks
        expiration_time: Optional[str] = None
        public_key: Optional[PublicKey]=None,
        
# wrapper list class
class Credentials(BlockList):
        items: List[CredentialsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GatewayConfigItem():
        # non-optional-blocks
        gateway_auth_method: Optional[str] = None
        gateway_type: Optional[str] = None
        
# wrapper list class
class GatewayConfig(BlockList):
        items: List[GatewayConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudiotDevice(ResourceObject):
    """    
    Args:
        name (str): A unique name for the resource.
        registry (str): The name of the device registry where this device should be created.
    """
    _type = 'google_cloudiot_device'
    
    def __init__(self,
        tf_id: str,
        name:str,
        registry:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        blocked: Optional[bool] = None,
        id: Optional[str] = None,
        log_level: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        public_key: Optional[PublicKey]=None,
        credentials: Optional[Credentials]=None,
        gateway_config: Optional[GatewayConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if registry is not None:
                kwargs['registry'] = registry
            if blocked is not None:
                kwargs['blocked'] = blocked
            if id is not None:
                kwargs['id'] = id
            if log_level is not None:
                kwargs['log_level'] = log_level
            if metadata is not None:
                kwargs['metadata'] = metadata
            if public_key is not None:
                kwargs['public_key'] = public_key
            if credentials is not None:
                kwargs['credentials'] = credentials
            if gateway_config is not None:
                kwargs['gateway_config'] = gateway_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
