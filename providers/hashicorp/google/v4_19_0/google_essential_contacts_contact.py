
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




class GoogleEssentialContactsContact(ResourceObject):
    """    
    Args:
        email (str): The email address to send notifications to. This does not need to be a Google account.
        language_tag (str): The preferred language for notifications, as a ISO 639-1 language code. See Supported languages for a list of supported languages.
        notification_category_subscriptions (List[str]): The categories of notifications that the contact will receive communications for.
        parent (str): The resource to save this contact for. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}
    """
    _type = 'google_essential_contacts_contact'
    
    def __init__(self,
        tf_id: str,
        email:str,
        language_tag:str,
        notification_category_subscriptions:List[str],
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if email is not None:
                kwargs['email'] = email
            if language_tag is not None:
                kwargs['language_tag'] = language_tag
            if notification_category_subscriptions is not None:
                kwargs['notification_category_subscriptions'] = notification_category_subscriptions
            if parent is not None:
                kwargs['parent'] = parent
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
