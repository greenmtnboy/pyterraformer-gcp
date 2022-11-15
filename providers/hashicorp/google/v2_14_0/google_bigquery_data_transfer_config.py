
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBigqueryDataTransferConfig(ResourceObject):
    """    
    Args:
        data_source_id (str): 
        destination_dataset_id (str): 
        display_name (str): 
        params (Dict[str, str]): 
    """
    _type = 'google_bigquery_data_transfer_config'
    
    def __init__(self,
        tf_id: str,
        data_source_id:str,
        destination_dataset_id:str,
        display_name:str,
        params:Dict[str, str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        data_refresh_window_days: Optional[float] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        schedule: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if data_source_id is not None:
                kwargs['data_source_id'] = data_source_id
            if destination_dataset_id is not None:
                kwargs['destination_dataset_id'] = destination_dataset_id
            if display_name is not None:
                kwargs['display_name'] = display_name
            if params is not None:
                kwargs['params'] = params
            if data_refresh_window_days is not None:
                kwargs['data_refresh_window_days'] = data_refresh_window_days
            if disabled is not None:
                kwargs['disabled'] = disabled
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if schedule is not None:
                kwargs['schedule'] = schedule
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
