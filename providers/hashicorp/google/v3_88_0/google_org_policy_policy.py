
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionItem():
        # non-optional-blocks
        description: Optional[str] = None
        expression: Optional[str] = None
        location: Optional[str] = None
        title: Optional[str] = None
        
# wrapper list class
class Condition(BlockList):
        items: List[ConditionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ValuesItem():
        # non-optional-blocks
        allowed_values: Optional[List[str]] = None
        denied_values: Optional[List[str]] = None
        
# wrapper list class
class Values(BlockList):
        items: List[ValuesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RulesItem():
        # non-optional-blocks
        allow_all: Optional[str] = None
        deny_all: Optional[str] = None
        enforce: Optional[str] = None
        condition: Optional[Condition]=None,
        values: Optional[Values]=None,
        
# wrapper list class
class Rules(BlockList):
        items: List[RulesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SpecItem():
        # non-optional-blocks
        inherit_from_parent: Optional[bool] = None
        reset: Optional[bool] = None
        condition: Optional[Condition]=None,
        values: Optional[Values]=None,
        rules: Optional[Rules]=None,
        
# wrapper list class
class Spec(BlockList):
        items: List[SpecItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleOrgPolicyPolicy(ResourceObject):
    """    
    Args:
        name (str): Immutable. The resource name of the Policy. Must be one of the following forms, where constraint_name is the name of the constraint which this Policy configures: * `projects/{project_number}/policies/{constraint_name}` * `folders/{folder_id}/policies/{constraint_name}` * `organizations/{organization_id}/policies/{constraint_name}` For example, "projects/123/policies/compute.disableSerialPortAccess". Note: `projects/{project_id}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number.
        parent (str): The parent of the resource.
    """
    _type = 'google_org_policy_policy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        condition: Optional[Condition]=None,
        values: Optional[Values]=None,
        rules: Optional[Rules]=None,
        spec: Optional[Spec]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if parent is not None:
                kwargs['parent'] = parent
            if id is not None:
                kwargs['id'] = id
            if condition is not None:
                kwargs['condition'] = condition
            if values is not None:
                kwargs['values'] = values
            if rules is not None:
                kwargs['rules'] = rules
            if spec is not None:
                kwargs['spec'] = spec
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
