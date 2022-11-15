
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ViewItem():
        dataset_id:str
        project_id:str
        table_id:str
        # non-optional-blocks
        
# wrapper list class
class View(BlockList):
        items: List[ViewItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class AccessItem():
        # non-optional-blocks
        domain: Optional[str] = None
        group_by_email: Optional[str] = None
        role: Optional[str] = None
        special_group: Optional[str] = None
        user_by_email: Optional[str] = None
        view: Optional[View]=None,
        
# wrapper list class
class Access(BlockSet):
        items: Set[AccessItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBigqueryDataset(ResourceObject):
    """    
    Args:
        dataset_id (str): 
    """
    _type = 'google_bigquery_dataset'
    
    def __init__(self,
        tf_id: str,
        dataset_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        default_partition_expiration_ms: Optional[float] = None,
        default_table_expiration_ms: Optional[float] = None,
        delete_contents_on_destroy: Optional[bool] = None,
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        view: Optional[View]=None,
        access: Optional[Access]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dataset_id is not None:
                kwargs['dataset_id'] = dataset_id
            if default_partition_expiration_ms is not None:
                kwargs['default_partition_expiration_ms'] = default_partition_expiration_ms
            if default_table_expiration_ms is not None:
                kwargs['default_table_expiration_ms'] = default_table_expiration_ms
            if delete_contents_on_destroy is not None:
                kwargs['delete_contents_on_destroy'] = delete_contents_on_destroy
            if description is not None:
                kwargs['description'] = description
            if friendly_name is not None:
                kwargs['friendly_name'] = friendly_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if view is not None:
                kwargs['view'] = view
            if access is not None:
                kwargs['access'] = access
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
