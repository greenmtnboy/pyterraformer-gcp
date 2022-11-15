
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class ClusterItem():
        cluster_id:str
        zone:str
        # non-optional-blocks
        num_nodes: Optional[float] = None
        storage_type: Optional[str] = None
        
# wrapper list class
class Cluster(BlockSet):
        items: Set[ClusterItem]



class GoogleBigtableInstance(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_bigtable_instance'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        cluster_id: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        instance_type: Optional[str] = None,
        num_nodes: Optional[float] = None,
        project: Optional[str] = None,
        storage_type: Optional[str] = None,
        zone: Optional[str] = None,
        cluster: Optional[Cluster]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if cluster_id is not None:
                kwargs['cluster_id'] = cluster_id
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if instance_type is not None:
                kwargs['instance_type'] = instance_type
            if num_nodes is not None:
                kwargs['num_nodes'] = num_nodes
            if project is not None:
                kwargs['project'] = project
            if storage_type is not None:
                kwargs['storage_type'] = storage_type
            if zone is not None:
                kwargs['zone'] = zone
            if cluster is not None:
                kwargs['cluster'] = cluster
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
