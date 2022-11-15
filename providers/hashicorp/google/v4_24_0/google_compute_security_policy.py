
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigItem():
        src_ip_ranges:Set[str]
        # non-optional-blocks
        
# wrapper list class
class Config(BlockList):
        items: List[ConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExprItem():
        expression:str
        # non-optional-blocks
        
# wrapper list class
class Expr(BlockList):
        items: List[ExprItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MatchItem():
        # non-optional-blocks
        versioned_expr: Optional[str] = None
        config: Optional[Config]=None,
        expr: Optional[Expr]=None,
        
# wrapper list class
class Match(BlockList):
        items: List[MatchItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class RuleItem():
        action:str
        priority:float
        # non-optional-blocks
        description: Optional[str] = None
        preview: Optional[bool] = None
        config: Optional[Config]=None,
        expr: Optional[Expr]=None,
        match: Optional[Match]=None,
        
# wrapper list class
class Rule(BlockSet):
        items: Set[RuleItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeSecurityPolicy(ResourceObject):
    """    
    Args:
        name (str): The name of the security policy.
    """
    _type = 'google_compute_security_policy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        type: Optional[str] = None,
        config: Optional[Config]=None,
        expr: Optional[Expr]=None,
        match: Optional[Match]=None,
        rule: Optional[Rule]=None,
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
            if type is not None:
                kwargs['type'] = type
            if config is not None:
                kwargs['config'] = config
            if expr is not None:
                kwargs['expr'] = expr
            if match is not None:
                kwargs['match'] = match
            if rule is not None:
                kwargs['rule'] = rule
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
