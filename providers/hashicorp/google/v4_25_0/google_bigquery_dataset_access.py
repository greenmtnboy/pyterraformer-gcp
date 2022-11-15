
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DatasetItem():
        target_types:List[str]
        # non-optional-blocks
        dataset: Optional[Dataset]=None,
        
# wrapper list class
class Dataset(BlockList):
        items: List[DatasetItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




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




class GoogleBigqueryDatasetAccess(ResourceObject):
    """    
    Args:
        dataset_id (str): A unique ID for this dataset, without the project name. The ID
                    must contain only letters (a-z, A-Z), numbers (0-9), or
                    underscores (_). The maximum length is 1,024 characters.
    """
    _type = 'google_bigquery_dataset_access'
    
    def __init__(self,
        tf_id: str,
        dataset_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        domain: Optional[str] = None,
        group_by_email: Optional[str] = None,
        iam_member: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        role: Optional[str] = None,
        special_group: Optional[str] = None,
        user_by_email: Optional[str] = None,
        dataset: Optional[Dataset]=None,
        timeouts: Optional[Timeouts]=None,
        view: Optional[View]=None,
        ):
            kwargs = {}
            if dataset_id is not None:
                kwargs['dataset_id'] = dataset_id
            if domain is not None:
                kwargs['domain'] = domain
            if group_by_email is not None:
                kwargs['group_by_email'] = group_by_email
            if iam_member is not None:
                kwargs['iam_member'] = iam_member
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if role is not None:
                kwargs['role'] = role
            if special_group is not None:
                kwargs['special_group'] = special_group
            if user_by_email is not None:
                kwargs['user_by_email'] = user_by_email
            if dataset is not None:
                kwargs['dataset'] = dataset
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if view is not None:
                kwargs['view'] = view
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
