
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeSubnetworkIamBinding(ResourceObject):
    """    
    Args:
        members (Set[str]): 
        role (str): 
        subnetwork (str): 
    """
    _type = 'google_compute_subnetwork_iam_binding'
    
    def __init__(self,
        tf_id: str,
        members:Set[str],
        role:str,
        subnetwork:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        ):
            kwargs = {}
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
