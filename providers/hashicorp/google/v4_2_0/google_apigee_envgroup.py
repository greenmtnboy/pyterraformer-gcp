
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




class GoogleApigeeEnvgroup(ResourceObject):
    """    
    Args:
        name (str): The resource ID of the environment group.
        org_id (str): The Apigee Organization associated with the Apigee environment group,
                    in the format 'organizations/{{org_name}}'.
    """
    _type = 'google_apigee_envgroup'
    
    def __init__(self,
        tf_id: str,
        name:str,
        org_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        hostnames: Optional[List[str]] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if org_id is not None:
                kwargs['org_id'] = org_id
            if hostnames is not None:
                kwargs['hostnames'] = hostnames
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
