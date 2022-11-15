
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeSubnetworkIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        subnetwork (str): 
    """
    _type = 'google_compute_subnetwork_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        subnetwork:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
