
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




class GoogleSpannerDatabase(ResourceObject):
    """    
    Args:
        instance (str): The instance to create the database on.
        name (str): A unique identifier for the database, which cannot be changed after
                    the instance is created. Values are of the form [a-z][-a-z0-9]*[a-z0-9].
    """
    _type = 'google_spanner_database'
    
    def __init__(self,
        tf_id: str,
        instance:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        ddl: Optional[List[str]] = None,
        deletion_protection: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if instance is not None:
                kwargs['instance'] = instance
            if name is not None:
                kwargs['name'] = name
            if ddl is not None:
                kwargs['ddl'] = ddl
            if deletion_protection is not None:
                kwargs['deletion_protection'] = deletion_protection
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
