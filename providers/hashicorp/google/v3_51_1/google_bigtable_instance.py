
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
class Cluster(BlockList):
        items: List[ClusterItem]




class GoogleBigtableInstance(ResourceObject):
    """    
    Args:
        name (str): The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.
    """
    _type = 'google_bigtable_instance'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        deletion_protection: Optional[bool] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        instance_type: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        cluster: Optional[Cluster]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if deletion_protection is not None:
                kwargs['deletion_protection'] = deletion_protection
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if instance_type is not None:
                kwargs['instance_type'] = instance_type
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if cluster is not None:
                kwargs['cluster'] = cluster
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
