
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SingleClusterRoutingItem():
        cluster_id:str
        # non-optional-blocks
        allow_transactional_writes: Optional[bool] = None
        
# wrapper list class
class SingleClusterRouting(BlockList):
        items: List[SingleClusterRoutingItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBigtableAppProfile(ResourceObject):
    """    
    Args:
        app_profile_id (str): The unique name of the app profile in the form '[_a-zA-Z0-9][-_.a-zA-Z0-9]*'.
    """
    _type = 'google_bigtable_app_profile'
    
    def __init__(self,
        tf_id: str,
        app_profile_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ignore_warnings: Optional[bool] = None,
        instance: Optional[str] = None,
        multi_cluster_routing_use_any: Optional[bool] = None,
        project: Optional[str] = None,
        single_cluster_routing: Optional[SingleClusterRouting]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if app_profile_id is not None:
                kwargs['app_profile_id'] = app_profile_id
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ignore_warnings is not None:
                kwargs['ignore_warnings'] = ignore_warnings
            if instance is not None:
                kwargs['instance'] = instance
            if multi_cluster_routing_use_any is not None:
                kwargs['multi_cluster_routing_use_any'] = multi_cluster_routing_use_any
            if project is not None:
                kwargs['project'] = project
            if single_cluster_routing is not None:
                kwargs['single_cluster_routing'] = single_cluster_routing
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
