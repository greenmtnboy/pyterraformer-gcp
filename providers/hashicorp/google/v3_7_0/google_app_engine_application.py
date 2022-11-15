
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FeatureSettingsItem():
        split_health_checks:bool
        # non-optional-blocks
        
# wrapper list class
class FeatureSettings(BlockList):
        items: List[FeatureSettingsItem]




class GoogleAppEngineApplication(ResourceObject):
    """    
    Args:
        location_id (str): 
    """
    _type = 'google_app_engine_application'
    
    def __init__(self,
        tf_id: str,
        location_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        auth_domain: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        serving_status: Optional[str] = None,
        feature_settings: Optional[FeatureSettings]=None,
        ):
            kwargs = {}
            if location_id is not None:
                kwargs['location_id'] = location_id
            if auth_domain is not None:
                kwargs['auth_domain'] = auth_domain
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if serving_status is not None:
                kwargs['serving_status'] = serving_status
            if feature_settings is not None:
                kwargs['feature_settings'] = feature_settings
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
