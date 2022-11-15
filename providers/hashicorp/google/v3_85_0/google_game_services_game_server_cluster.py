
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GkeClusterReferenceItem():
        cluster:str
        # non-optional-blocks
        
# wrapper list class
class GkeClusterReference(BlockList):
        items: List[GkeClusterReferenceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConnectionInfoItem():
        namespace:str
        # non-optional-blocks
        gke_cluster_reference: Optional[GkeClusterReference]=None,
        
# wrapper list class
class ConnectionInfo(BlockList):
        items: List[ConnectionInfoItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleGameServicesGameServerCluster(ResourceObject):
    """    
    Args:
        cluster_id (str): Required. The resource name of the game server cluster
        realm_id (str): The realm id of the game server realm.
    """
    _type = 'google_game_services_game_server_cluster'
    
    def __init__(self,
        tf_id: str,
        cluster_id:str,
        realm_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        gke_cluster_reference: Optional[GkeClusterReference]=None,
        connection_info: Optional[ConnectionInfo]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if cluster_id is not None:
                kwargs['cluster_id'] = cluster_id
            if realm_id is not None:
                kwargs['realm_id'] = realm_id
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if gke_cluster_reference is not None:
                kwargs['gke_cluster_reference'] = gke_cluster_reference
            if connection_info is not None:
                kwargs['connection_info'] = connection_info
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
