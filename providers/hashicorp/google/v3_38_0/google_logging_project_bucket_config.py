
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleLoggingProjectBucketConfig(ResourceObject):
    """    
    Args:
        bucket_id (str): The name of the logging bucket. Logging automatically creates two log buckets: _Required and _Default.
        location (str): The location of the bucket. The supported locations are: "global" "us-central1"
        project (str): The parent project that contains the logging bucket.
    """
    _type = 'google_logging_project_bucket_config'
    
    def __init__(self,
        tf_id: str,
        bucket_id:str,
        location:str,
        project:str,
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
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if retention_days is not None:
                kwargs['retention_days'] = retention_days
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
