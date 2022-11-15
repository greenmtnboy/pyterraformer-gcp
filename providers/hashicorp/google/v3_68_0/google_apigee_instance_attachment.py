
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




class GoogleApigeeInstanceAttachment(ResourceObject):
    """    
    Args:
        environment (str): The resource ID of the environment.
        instance_id (str): The Apigee instance associated with the Apigee environment,
                    in the format 'organisations/{{org_name}}/instances/{{instance_name}}'.
    """
    _type = 'google_apigee_instance_attachment'
    
    def __init__(self,
        tf_id: str,
        environment:str,
        instance_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if environment is not None:
                kwargs['environment'] = environment
            if instance_id is not None:
                kwargs['instance_id'] = instance_id
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
