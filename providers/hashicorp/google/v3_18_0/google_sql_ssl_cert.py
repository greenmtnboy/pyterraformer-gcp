
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleSqlSslCert(ResourceObject):
    """    
    Args:
        common_name (str): 
        instance (str): 
    """
    _type = 'google_sql_ssl_cert'
    
    def __init__(self,
        tf_id: str,
        common_name:str,
        instance:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if common_name is not None:
                kwargs['common_name'] = common_name
            if instance is not None:
                kwargs['instance'] = instance
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
