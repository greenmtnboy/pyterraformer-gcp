
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




class GoogleSpannerInstance(ResourceObject):
    """    
    Args:
        config (str): 
        display_name (str): 
    """
    _type = 'google_spanner_instance'
    
    def __init__(self,
        tf_id: str,
        config:str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        num_nodes: Optional[float] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if config is not None:
                kwargs['config'] = config
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if name is not None:
                kwargs['name'] = name
            if num_nodes is not None:
                kwargs['num_nodes'] = num_nodes
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
