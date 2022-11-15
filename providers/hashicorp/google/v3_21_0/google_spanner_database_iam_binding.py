
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleSpannerDatabaseIamBinding(ResourceObject):
    """    
    Args:
        database (str): 
        instance (str): 
        members (Set[str]): 
        role (str): 
    """
    _type = 'google_spanner_database_iam_binding'
    
    def __init__(self,
        tf_id: str,
        database:str,
        instance:str,
        members:Set[str],
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if database is not None:
                kwargs['database'] = database
            if instance is not None:
                kwargs['instance'] = instance
            if members is not None:
                kwargs['members'] = members
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
