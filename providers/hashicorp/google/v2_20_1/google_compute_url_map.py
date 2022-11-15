
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PathRuleItem():
        paths:Set[str]
        service:str
        # non-optional-blocks
        
# wrapper list class
class PathRule(BlockList):
        items: List[PathRuleItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class HostRuleItem():
        hosts:Set[str]
        path_matcher:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class HostRule(BlockSet):
        items: Set[HostRuleItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class PathMatcherItem():
        default_service:str
        name:str
        # non-optional-blocks
        description: Optional[str] = None
        path_rule: Optional[PathRule]=None,
        
# wrapper list class
class PathMatcher(BlockList):
        items: List[PathMatcherItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TestItem():
        host:str
        path:str
        service:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class Test(BlockList):
        items: List[TestItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeUrlMap(ResourceObject):
    """    
    Args:
        default_service (str): The backend service or backend bucket to use when none of the given rules match.
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
    """
    _type = 'google_compute_url_map'
    
    def __init__(self,
        tf_id: str,
        default_service:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        path_rule: Optional[PathRule]=None,
        host_rule: Optional[HostRule]=None,
        path_matcher: Optional[PathMatcher]=None,
        test: Optional[Test]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if default_service is not None:
                kwargs['default_service'] = default_service
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if path_rule is not None:
                kwargs['path_rule'] = path_rule
            if host_rule is not None:
                kwargs['host_rule'] = host_rule
            if path_matcher is not None:
                kwargs['path_matcher'] = path_matcher
            if test is not None:
                kwargs['test'] = test
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
