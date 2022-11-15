
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class OidcTokenItem():
        service_account_email:str
        # non-optional-blocks
        audience: Optional[str] = None
        
# wrapper list class
class OidcToken(BlockList):
        items: List[OidcTokenItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExpirationPolicyItem():
        # non-optional-blocks
        ttl: Optional[str] = None
        
# wrapper list class
class ExpirationPolicy(BlockList):
        items: List[ExpirationPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PushConfigItem():
        push_endpoint:str
        # non-optional-blocks
        attributes: Optional[Dict[str, str]] = None
        oidc_token: Optional[OidcToken]=None,
        
# wrapper list class
class PushConfig(BlockList):
        items: List[PushConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePubsubSubscription(ResourceObject):
    """    
    Args:
        name (str): 
        topic (str): 
    """
    _type = 'google_pubsub_subscription'
    
    def __init__(self,
        tf_id: str,
        name:str,
        topic:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        ack_deadline_seconds: Optional[float] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        message_retention_duration: Optional[str] = None,
        project: Optional[str] = None,
        retain_acked_messages: Optional[bool] = None,
        oidc_token: Optional[OidcToken]=None,
        expiration_policy: Optional[ExpirationPolicy]=None,
        push_config: Optional[PushConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if topic is not None:
                kwargs['topic'] = topic
            if ack_deadline_seconds is not None:
                kwargs['ack_deadline_seconds'] = ack_deadline_seconds
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if message_retention_duration is not None:
                kwargs['message_retention_duration'] = message_retention_duration
            if project is not None:
                kwargs['project'] = project
            if retain_acked_messages is not None:
                kwargs['retain_acked_messages'] = retain_acked_messages
            if oidc_token is not None:
                kwargs['oidc_token'] = oidc_token
            if expiration_policy is not None:
                kwargs['expiration_policy'] = expiration_policy
            if push_config is not None:
                kwargs['push_config'] = push_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
