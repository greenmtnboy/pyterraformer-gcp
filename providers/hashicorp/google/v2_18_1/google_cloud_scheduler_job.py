
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class OauthTokenItem():
        # non-optional-blocks
        scope: Optional[str] = None
        service_account_email: Optional[str] = None
        
# wrapper list class
class OauthToken(BlockList):
        items: List[OauthTokenItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OidcTokenItem():
        # non-optional-blocks
        audience: Optional[str] = None
        service_account_email: Optional[str] = None
        
# wrapper list class
class OidcToken(BlockList):
        items: List[OidcTokenItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AppEngineRoutingItem():
        # non-optional-blocks
        instance: Optional[str] = None
        service: Optional[str] = None
        version: Optional[str] = None
        
# wrapper list class
class AppEngineRouting(BlockList):
        items: List[AppEngineRoutingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AppEngineHttpTargetItem():
        relative_uri:str
        # non-optional-blocks
        body: Optional[str] = None
        headers: Optional[Dict[str, str]] = None
        http_method: Optional[str] = None
        app_engine_routing: Optional[AppEngineRouting]=None,
        
# wrapper list class
class AppEngineHttpTarget(BlockList):
        items: List[AppEngineHttpTargetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpTargetItem():
        uri:str
        # non-optional-blocks
        body: Optional[str] = None
        headers: Optional[Dict[str, str]] = None
        http_method: Optional[str] = None
        oauth_token: Optional[OauthToken]=None,
        oidc_token: Optional[OidcToken]=None,
        
# wrapper list class
class HttpTarget(BlockList):
        items: List[HttpTargetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PubsubTargetItem():
        topic_name:str
        # non-optional-blocks
        attributes: Optional[Dict[str, str]] = None
        data: Optional[str] = None
        
# wrapper list class
class PubsubTarget(BlockList):
        items: List[PubsubTargetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RetryConfigItem():
        # non-optional-blocks
        max_backoff_duration: Optional[str] = None
        max_doublings: Optional[float] = None
        max_retry_duration: Optional[str] = None
        min_backoff_duration: Optional[str] = None
        retry_count: Optional[float] = None
        
# wrapper list class
class RetryConfig(BlockList):
        items: List[RetryConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleCloudSchedulerJob(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_cloud_scheduler_job'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        schedule: Optional[str] = None,
        time_zone: Optional[str] = None,
        oauth_token: Optional[OauthToken]=None,
        oidc_token: Optional[OidcToken]=None,
        app_engine_routing: Optional[AppEngineRouting]=None,
        app_engine_http_target: Optional[AppEngineHttpTarget]=None,
        http_target: Optional[HttpTarget]=None,
        pubsub_target: Optional[PubsubTarget]=None,
        retry_config: Optional[RetryConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if schedule is not None:
                kwargs['schedule'] = schedule
            if time_zone is not None:
                kwargs['time_zone'] = time_zone
            if oauth_token is not None:
                kwargs['oauth_token'] = oauth_token
            if oidc_token is not None:
                kwargs['oidc_token'] = oidc_token
            if app_engine_routing is not None:
                kwargs['app_engine_routing'] = app_engine_routing
            if app_engine_http_target is not None:
                kwargs['app_engine_http_target'] = app_engine_http_target
            if http_target is not None:
                kwargs['http_target'] = http_target
            if pubsub_target is not None:
                kwargs['pubsub_target'] = pubsub_target
            if retry_config is not None:
                kwargs['retry_config'] = retry_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
