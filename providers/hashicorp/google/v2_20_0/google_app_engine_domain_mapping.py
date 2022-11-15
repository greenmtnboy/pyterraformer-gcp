
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SslSettingsItem():
        # non-optional-blocks
        certificate_id: Optional[str] = None
        ssl_management_type: Optional[str] = None
        
# wrapper list class
class SslSettings(BlockList):
        items: List[SslSettingsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAppEngineDomainMapping(ResourceObject):
    """    
    Args:
        domain_name (str): Relative name of the domain serving the application. Example: example.com.
    """
    _type = 'google_app_engine_domain_mapping'
    
    def __init__(self,
        tf_id: str,
        domain_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        override_strategy: Optional[str] = None,
        project: Optional[str] = None,
        ssl_settings: Optional[SslSettings]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if domain_name is not None:
                kwargs['domain_name'] = domain_name
            if id is not None:
                kwargs['id'] = id
            if override_strategy is not None:
                kwargs['override_strategy'] = override_strategy
            if project is not None:
                kwargs['project'] = project
            if ssl_settings is not None:
                kwargs['ssl_settings'] = ssl_settings
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
