
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




class GoogleMonitoringGroup(ResourceObject):
    """    
    Args:
        display_name (str): A user-assigned name for this group, used only for display
                    purposes.
        filter (str): The filter used to determine which monitored resources
                    belong to this group.
    """
    _type = 'google_monitoring_group'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        filter:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        is_cluster: Optional[bool] = None,
        parent_name: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            if is_cluster is not None:
                kwargs['is_cluster'] = is_cluster
            if parent_name is not None:
                kwargs['parent_name'] = parent_name
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
