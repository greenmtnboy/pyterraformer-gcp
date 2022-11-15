
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




class GoogleResourceManagerLien(ResourceObject):
    """    
    Args:
        origin (str): A stable, user-visible/meaningful string identifying the origin
                    of the Lien, intended to be inspected programmatically. Maximum length of
                    200 characters.
        parent (str): A reference to the resource this Lien is attached to.
                    The server will validate the parent against those for which Liens are supported.
                    Since a variety of objects can have Liens against them, you must provide the type
                    prefix (e.g. "projects/my-project-name").
        reason (str): Concise user-visible strings indicating why an action cannot be performed
                    on a resource. Maximum length of 200 characters.
        restrictions (List[str]): The types of operations which should be blocked as a result of this Lien.
                    Each value should correspond to an IAM permission. The server will validate
                    the permissions against those for which Liens are supported.  An empty
                    list is meaningless and will be rejected.
                    e.g. ['resourcemanager.projects.delete']
    """
    _type = 'google_resource_manager_lien'
    
    def __init__(self,
        tf_id: str,
        origin:str,
        parent:str,
        reason:str,
        restrictions:List[str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if origin is not None:
                kwargs['origin'] = origin
            if parent is not None:
                kwargs['parent'] = parent
            if reason is not None:
                kwargs['reason'] = reason
            if restrictions is not None:
                kwargs['restrictions'] = restrictions
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
