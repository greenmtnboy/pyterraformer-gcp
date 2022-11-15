
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AndroidSettingsItem():
        # non-optional-blocks
        allow_all_package_names: Optional[bool] = None
        allowed_package_names: Optional[List[str]] = None
        
# wrapper list class
class AndroidSettings(BlockList):
        items: List[AndroidSettingsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IosSettingsItem():
        # non-optional-blocks
        allow_all_bundle_ids: Optional[bool] = None
        allowed_bundle_ids: Optional[List[str]] = None
        
# wrapper list class
class IosSettings(BlockList):
        items: List[IosSettingsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TestingOptionsItem():
        # non-optional-blocks
        testing_challenge: Optional[str] = None
        testing_score: Optional[float] = None
        
# wrapper list class
class TestingOptions(BlockList):
        items: List[TestingOptionsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class WebSettingsItem():
        integration_type:str
        # non-optional-blocks
        allow_all_domains: Optional[bool] = None
        allow_amp_traffic: Optional[bool] = None
        allowed_domains: Optional[List[str]] = None
        challenge_security_preference: Optional[str] = None
        
# wrapper list class
class WebSettings(BlockList):
        items: List[WebSettingsItem]




class GoogleRecaptchaEnterpriseKey(ResourceObject):
    """    
    Args:
        display_name (str): Human-readable display name of this key. Modifiable by user.
    """
    _type = 'google_recaptcha_enterprise_key'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        android_settings: Optional[AndroidSettings]=None,
        ios_settings: Optional[IosSettings]=None,
        testing_options: Optional[TestingOptions]=None,
        timeouts: Optional[Timeouts]=None,
        web_settings: Optional[WebSettings]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if android_settings is not None:
                kwargs['android_settings'] = android_settings
            if ios_settings is not None:
                kwargs['ios_settings'] = ios_settings
            if testing_options is not None:
                kwargs['testing_options'] = testing_options
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if web_settings is not None:
                kwargs['web_settings'] = web_settings
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
