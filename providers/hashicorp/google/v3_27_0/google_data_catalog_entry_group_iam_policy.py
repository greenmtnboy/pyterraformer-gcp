
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleDataCatalogEntryGroupIamPolicy(ResourceObject):
    """    
    Args:
        entry_group (str): 
        policy_data (str): 
    """
    _type = 'google_data_catalog_entry_group_iam_policy'
    
    def __init__(self,
        tf_id: str,
        entry_group:str,
        policy_data:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        ):
            kwargs = {}
            if entry_group is not None:
                kwargs['entry_group'] = entry_group
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
