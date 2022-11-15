
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




class GoogleIdentityPlatformTenantDefaultSupportedIdpConfig(ResourceObject):
    """    
    Args:
        client_id (str): OAuth client ID
        client_secret (str): OAuth client secret
        tenant (str): The name of the tenant where this DefaultSupportedIdpConfig resource exists
    """
    _type = 'google_identity_platform_tenant_default_supported_idp_config'
    
    def __init__(self,
        tf_id: str,
        client_id:str,
        client_secret:str,
        tenant:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if client_id is not None:
                kwargs['client_id'] = client_id
            if client_secret is not None:
                kwargs['client_secret'] = client_secret
            if tenant is not None:
                kwargs['tenant'] = tenant
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
