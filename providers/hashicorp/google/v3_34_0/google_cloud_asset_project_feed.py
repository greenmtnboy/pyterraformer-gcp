
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PubsubDestinationItem():
        topic:str
        # non-optional-blocks
        
# wrapper list class
class PubsubDestination(BlockList):
        items: List[PubsubDestinationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FeedOutputConfigItem():
        # non-optional-blocks
        pubsub_destination: Optional[PubsubDestination]=None,
        
# wrapper list class
class FeedOutputConfig(BlockList):
        items: List[FeedOutputConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudAssetProjectFeed(ResourceObject):
    """    
    Args:
        feed_id (str): This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
    """
    _type = 'google_cloud_asset_project_feed'
    
    def __init__(self,
        tf_id: str,
        feed_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        asset_names: Optional[List[str]] = None,
        asset_types: Optional[List[str]] = None,
        billing_project: Optional[str] = None,
        content_type: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        pubsub_destination: Optional[PubsubDestination]=None,
        feed_output_config: Optional[FeedOutputConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if feed_id is not None:
                kwargs['feed_id'] = feed_id
            if asset_names is not None:
                kwargs['asset_names'] = asset_names
            if asset_types is not None:
                kwargs['asset_types'] = asset_types
            if billing_project is not None:
                kwargs['billing_project'] = billing_project
            if content_type is not None:
                kwargs['content_type'] = content_type
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if pubsub_destination is not None:
                kwargs['pubsub_destination'] = pubsub_destination
            if feed_output_config is not None:
                kwargs['feed_output_config'] = feed_output_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
