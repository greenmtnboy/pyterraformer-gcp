
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionItem():
        expression:str
        title:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class Condition(BlockList):
        items: List[ConditionItem]




class GoogleBigtableTableIamBinding(ResourceObject):
    """    
    Args:
        instance (str): 
        members (Set[str]): 
        role (str): 
        table (str): 
    """
    _type = 'google_bigtable_table_iam_binding'
    
    def __init__(self,
        tf_id: str,
        instance:str,
        members:Set[str],
        role:str,
        table:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        condition: Optional[Condition]=None,
        ):
            kwargs = {}
            if instance is not None:
                kwargs['instance'] = instance
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if table is not None:
                kwargs['table'] = table
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if condition is not None:
                kwargs['condition'] = condition
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
