
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleSqlUser(ResourceObject):
    """    
    Args:
        instance (str): The name of the Cloud SQL instance. Changing this forces a new resource to be created.
        name (str): The name of the user. Changing this forces a new resource to be created.
    """
    _type = 'google_sql_user'
    
    def __init__(self,
        tf_id: str,
        instance:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        deletion_policy: Optional[str] = None,
        host: Optional[str] = None,
        id: Optional[str] = None,
        password: Optional[str] = None,
        project: Optional[str] = None,
        type: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if instance is not None:
                kwargs['instance'] = instance
            if name is not None:
                kwargs['name'] = name
            if deletion_policy is not None:
                kwargs['deletion_policy'] = deletion_policy
            if host is not None:
                kwargs['host'] = host
            if id is not None:
                kwargs['id'] = id
            if password is not None:
                kwargs['password'] = password
            if project is not None:
                kwargs['project'] = project
            if type is not None:
                kwargs['type'] = type
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
