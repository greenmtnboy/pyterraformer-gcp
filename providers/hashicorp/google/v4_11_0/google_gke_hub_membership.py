
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GkeClusterItem():
        resource_link:str
        # non-optional-blocks
        
# wrapper list class
class GkeCluster(BlockList):
        items: List[GkeClusterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AuthorityItem():
        issuer:str
        # non-optional-blocks
        
# wrapper list class
class Authority(BlockList):
        items: List[AuthorityItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EndpointItem():
        # non-optional-blocks
        gke_cluster: Optional[GkeCluster]=None,
        
# wrapper list class
class Endpoint(BlockList):
        items: List[EndpointItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleGkeHubMembership(ResourceObject):
    """    
    Args:
        membership_id (str): The client-provided identifier of the membership.
    """
    _type = 'google_gke_hub_membership'
    
    def __init__(self,
        tf_id: str,
        membership_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        gke_cluster: Optional[GkeCluster]=None,
        authority: Optional[Authority]=None,
        endpoint: Optional[Endpoint]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if membership_id is not None:
                kwargs['membership_id'] = membership_id
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if gke_cluster is not None:
                kwargs['gke_cluster'] = gke_cluster
            if authority is not None:
                kwargs['authority'] = authority
            if endpoint is not None:
                kwargs['endpoint'] = endpoint
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
