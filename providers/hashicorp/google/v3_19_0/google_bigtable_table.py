
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class ColumnFamilyItem():
        family:str
        # non-optional-blocks
        
# wrapper list class
class ColumnFamily(BlockSet):
        items: Set[ColumnFamilyItem]



class GoogleBigtableTable(ResourceObject):
    """    
    Args:
        instance_name (str): 
        name (str): 
    """
    _type = 'google_bigtable_table'
    
    def __init__(self,
        tf_id: str,
        instance_name:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        split_keys: Optional[List[str]] = None,
        column_family: Optional[ColumnFamily]=None,
        ):
            kwargs = {}
            if instance_name is not None:
                kwargs['instance_name'] = instance_name
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if split_keys is not None:
                kwargs['split_keys'] = split_keys
            if column_family is not None:
                kwargs['column_family'] = column_family
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
