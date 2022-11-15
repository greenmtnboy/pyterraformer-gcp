
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AllowedApplicationsItem():
        package_name:str
        sha1_fingerprint:str
        # non-optional-blocks
        
# wrapper list class
class AllowedApplications(BlockList):
        items: List[AllowedApplicationsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AndroidKeyRestrictionsItem():
        # non-optional-blocks
        allowed_applications: Optional[AllowedApplications]=None,
        
# wrapper list class
class AndroidKeyRestrictions(BlockList):
        items: List[AndroidKeyRestrictionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ApiTargetsItem():
        service:str
        # non-optional-blocks
        methods: Optional[List[str]] = None
        
# wrapper list class
class ApiTargets(BlockList):
        items: List[ApiTargetsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BrowserKeyRestrictionsItem():
        allowed_referrers:List[str]
        # non-optional-blocks
        
# wrapper list class
class BrowserKeyRestrictions(BlockList):
        items: List[BrowserKeyRestrictionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IosKeyRestrictionsItem():
        allowed_bundle_ids:List[str]
        # non-optional-blocks
        
# wrapper list class
class IosKeyRestrictions(BlockList):
        items: List[IosKeyRestrictionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ServerKeyRestrictionsItem():
        allowed_ips:List[str]
        # non-optional-blocks
        
# wrapper list class
class ServerKeyRestrictions(BlockList):
        items: List[ServerKeyRestrictionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RestrictionsItem():
        # non-optional-blocks
        allowed_applications: Optional[AllowedApplications]=None,
        android_key_restrictions: Optional[AndroidKeyRestrictions]=None,
        api_targets: Optional[ApiTargets]=None,
        browser_key_restrictions: Optional[BrowserKeyRestrictions]=None,
        ios_key_restrictions: Optional[IosKeyRestrictions]=None,
        server_key_restrictions: Optional[ServerKeyRestrictions]=None,
        
# wrapper list class
class Restrictions(BlockList):
        items: List[RestrictionsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleApikeysKey(ResourceObject):
    """    
    Args:
        name (str): The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: [a-z]([a-z0-9-]{0,61}[a-z0-9])?.
    """
    _type = 'google_apikeys_key'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        allowed_applications: Optional[AllowedApplications]=None,
        android_key_restrictions: Optional[AndroidKeyRestrictions]=None,
        api_targets: Optional[ApiTargets]=None,
        browser_key_restrictions: Optional[BrowserKeyRestrictions]=None,
        ios_key_restrictions: Optional[IosKeyRestrictions]=None,
        server_key_restrictions: Optional[ServerKeyRestrictions]=None,
        restrictions: Optional[Restrictions]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if allowed_applications is not None:
                kwargs['allowed_applications'] = allowed_applications
            if android_key_restrictions is not None:
                kwargs['android_key_restrictions'] = android_key_restrictions
            if api_targets is not None:
                kwargs['api_targets'] = api_targets
            if browser_key_restrictions is not None:
                kwargs['browser_key_restrictions'] = browser_key_restrictions
            if ios_key_restrictions is not None:
                kwargs['ios_key_restrictions'] = ios_key_restrictions
            if server_key_restrictions is not None:
                kwargs['server_key_restrictions'] = server_key_restrictions
            if restrictions is not None:
                kwargs['restrictions'] = restrictions
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
