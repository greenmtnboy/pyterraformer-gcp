
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




class GoogleIapBrand(ResourceObject):
    """    
    Args:
        application_title (str): Application name displayed on OAuth consent screen.
        support_email (str): Support email displayed on the OAuth consent screen. Can be either a
                    user or group email. When a user email is specified, the caller must
                    be the user with the associated email address. When a group email is
                    specified, the caller can be either a user or a service account which
                    is an owner of the specified group in Cloud Identity.
    """
    _type = 'google_iap_brand'
    
    def __init__(self,
        tf_id: str,
        application_title:str,
        support_email:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if application_title is not None:
                kwargs['application_title'] = application_title
            if support_email is not None:
                kwargs['support_email'] = support_email
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
