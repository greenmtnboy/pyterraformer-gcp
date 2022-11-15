
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleProjectUsageExportBucket(ResourceObject):
    """    
    Args:
        bucket_name (str): 
    """
    _type = 'google_project_usage_export_bucket'
    
    def __init__(self,
        tf_id: str,
        bucket_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        prefix: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if bucket_name is not None:
                kwargs['bucket_name'] = bucket_name
            if id is not None:
                kwargs['id'] = id
            if prefix is not None:
                kwargs['prefix'] = prefix
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
