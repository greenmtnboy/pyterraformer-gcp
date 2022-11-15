
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleLoggingFolderBucketConfig(ResourceObject):
    """    
    Args:
        bucket_id (str): 
        folder (str): 
        location (str): 
    """
    _type = 'google_logging_folder_bucket_config'
    
    def __init__(self,
        tf_id: str,
        bucket_id:str,
        folder:str,
        location:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        retention_days: Optional[float] = None,
        ):
            kwargs = {}
            if bucket_id is not None:
                kwargs['bucket_id'] = bucket_id
            if folder is not None:
                kwargs['folder'] = folder
            if location is not None:
                kwargs['location'] = location
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if retention_days is not None:
                kwargs['retention_days'] = retention_days
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
