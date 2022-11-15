
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class MaxAgeItem():
        # non-optional-blocks
        days: Optional[float] = None
        duration: Optional[str] = None
        
# wrapper list class
class MaxAge(BlockList):
        items: List[MaxAgeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaxVersionItem():
        number:float
        # non-optional-blocks
        
# wrapper list class
class MaxVersion(BlockList):
        items: List[MaxVersionItem]




class GoogleBigtableGcPolicy(ResourceObject):
    """    
    Args:
        column_family (str): The name of the column family.
        instance_name (str): The name of the Bigtable instance.
        table (str): The name of the table.
    """
    _type = 'google_bigtable_gc_policy'
    
    def __init__(self,
        tf_id: str,
        column_family:str,
        instance_name:str,
        table:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        mode: Optional[str] = None,
        project: Optional[str] = None,
        max_age: Optional[MaxAge]=None,
        max_version: Optional[MaxVersion]=None,
        ):
            kwargs = {}
            if column_family is not None:
                kwargs['column_family'] = column_family
            if instance_name is not None:
                kwargs['instance_name'] = instance_name
            if table is not None:
                kwargs['table'] = table
            if id is not None:
                kwargs['id'] = id
            if mode is not None:
                kwargs['mode'] = mode
            if project is not None:
                kwargs['project'] = project
            if max_age is not None:
                kwargs['max_age'] = max_age
            if max_version is not None:
                kwargs['max_version'] = max_version
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
