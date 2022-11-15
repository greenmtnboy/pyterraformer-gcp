
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




class GoogleIdentityPlatformOauthIdpConfig(ResourceObject):
    """    
    Args:
        client_id (str): The client id of an OAuth client.
        issuer (str): For OIDC Idps, the issuer identifier.
        name (str): The name of the OauthIdpConfig. Must start with 'oidc.'.
    """
    _type = 'google_identity_platform_oauth_idp_config'
    
    def __init__(self,
        tf_id: str,
        client_id:str,
        issuer:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        client_secret: Optional[str] = None,
        display_name: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if client_id is not None:
                kwargs['client_id'] = client_id
            if issuer is not None:
                kwargs['issuer'] = issuer
            if name is not None:
                kwargs['name'] = name
            if client_secret is not None:
                kwargs['client_secret'] = client_secret
            if display_name is not None:
                kwargs['display_name'] = display_name
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
