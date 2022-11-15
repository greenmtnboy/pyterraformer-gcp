
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




class GoogleComputeNodeGroup(ResourceObject):
    """    
    Args:
        node_template (str): 
        size (float): 
    """
    _type = 'google_compute_node_group'
    
    def __init__(self,
        tf_id: str,
        node_template:str,
        size:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if node_template is not None:
                kwargs['node_template'] = node_template
            if size is not None:
                kwargs['size'] = size
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
