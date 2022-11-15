
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DispatchRulesItem():
        path:str
        service:str
        # non-optional-blocks
        domain: Optional[str] = None
        
# wrapper list class
class DispatchRules(BlockList):
        items: List[DispatchRulesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAppEngineApplicationUrlDispatchRules(ResourceObject):
    """    
    Args:
    """
    _type = 'google_app_engine_application_url_dispatch_rules'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        dispatch_rules: Optional[DispatchRules]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if dispatch_rules is not None:
                kwargs['dispatch_rules'] = dispatch_rules
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
