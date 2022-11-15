
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class TimePartitioningItem():
        type:str
        # non-optional-blocks
        expiration_ms: Optional[float] = None
        field: Optional[str] = None
        require_partition_filter: Optional[bool] = None
        
# wrapper list class
class TimePartitioning(BlockList):
        items: List[TimePartitioningItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ViewItem():
        query:str
        # non-optional-blocks
        use_legacy_sql: Optional[bool] = None
        
# wrapper list class
class View(BlockList):
        items: List[ViewItem]




class GoogleBigqueryTable(ResourceObject):
    """    
    Args:
        dataset_id (str): 
        table_id (str): 
    """
    _type = 'google_bigquery_table'
    
    def __init__(self,
        tf_id: str,
        dataset_id:str,
        table_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        expiration_time: Optional[float] = None,
        friendly_name: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        schema: Optional[str] = None,
        time_partitioning: Optional[TimePartitioning]=None,
        view: Optional[View]=None,
        ):
            kwargs = {}
            if dataset_id is not None:
                kwargs['dataset_id'] = dataset_id
            if table_id is not None:
                kwargs['table_id'] = table_id
            if description is not None:
                kwargs['description'] = description
            if expiration_time is not None:
                kwargs['expiration_time'] = expiration_time
            if friendly_name is not None:
                kwargs['friendly_name'] = friendly_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if schema is not None:
                kwargs['schema'] = schema
            if time_partitioning is not None:
                kwargs['time_partitioning'] = time_partitioning
            if view is not None:
                kwargs['view'] = view
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
