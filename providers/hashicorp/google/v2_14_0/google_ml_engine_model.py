
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DefaultVersionItem():
        # non-optional-blocks
        name: Optional[str] = None
        
# wrapper list class
class DefaultVersion(BlockList):
        items: List[DefaultVersionItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleMlEngineModel(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_ml_engine_model'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        online_prediction_console_logging: Optional[bool] = None,
        online_prediction_logging: Optional[bool] = None,
        project: Optional[str] = None,
        regions: Optional[List[str]] = None,
        default_version: Optional[DefaultVersion]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if online_prediction_console_logging is not None:
                kwargs['online_prediction_console_logging'] = online_prediction_console_logging
            if online_prediction_logging is not None:
                kwargs['online_prediction_logging'] = online_prediction_logging
            if project is not None:
                kwargs['project'] = project
            if regions is not None:
                kwargs['regions'] = regions
            if default_version is not None:
                kwargs['default_version'] = default_version
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
