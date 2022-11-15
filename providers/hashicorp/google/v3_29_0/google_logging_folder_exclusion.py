
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleLoggingFolderExclusion(ResourceObject):
    """    
    Args:
        filter (str): The filter to apply when excluding logs. Only log entries that match the filter are excluded.
        folder (str): 
        name (str): The name of the logging exclusion.
    """
    _type = 'google_logging_folder_exclusion'
    
    def __init__(self,
        tf_id: str,
        filter:str,
        folder:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if filter is not None:
                kwargs['filter'] = filter
            if folder is not None:
                kwargs['folder'] = folder
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
