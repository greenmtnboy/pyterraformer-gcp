
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




class GoogleIdentityPlatformTenant(ResourceObject):
    """    
    Args:
        display_name (str): Human friendly display name of the tenant.
    """
    _type = 'google_identity_platform_tenant'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        allow_password_signup: Optional[bool] = None,
        disable_auth: Optional[bool] = None,
        enable_email_link_signin: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if allow_password_signup is not None:
                kwargs['allow_password_signup'] = allow_password_signup
            if disable_auth is not None:
                kwargs['disable_auth'] = disable_auth
            if enable_email_link_signin is not None:
                kwargs['enable_email_link_signin'] = enable_email_link_signin
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
