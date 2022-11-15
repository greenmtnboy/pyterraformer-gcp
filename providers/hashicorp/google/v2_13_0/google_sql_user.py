
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleSqlUser(ResourceObject):
    """    
    Args:
        instance (str): 
        name (str): 
    """
    _type = 'google_sql_user'
    
    def __init__(self,
        tf_id: str,
        instance:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        host: Optional[str] = None,
        id: Optional[str] = None,
        password: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if instance is not None:
                kwargs['instance'] = instance
            if name is not None:
                kwargs['name'] = name
            if host is not None:
                kwargs['host'] = host
            if id is not None:
                kwargs['id'] = id
            if password is not None:
                kwargs['password'] = password
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
