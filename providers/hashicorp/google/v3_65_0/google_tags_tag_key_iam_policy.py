
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleTagsTagKeyIamPolicy(ResourceObject):
    """    
    Args:
        policy_data (str): 
        tag_key (str): 
    """
    _type = 'google_tags_tag_key_iam_policy'
    
    def __init__(self,
        tf_id: str,
        policy_data:str,
        tag_key:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if policy_data is not None:
                kwargs['policy_data'] = policy_data
            if tag_key is not None:
                kwargs['tag_key'] = tag_key
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
