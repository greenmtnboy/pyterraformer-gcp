
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




class GoogleApigeeEnvgroupAttachment(ResourceObject):
    """    
    Args:
        envgroup_id (str): The Apigee environment group associated with the Apigee environment,
                    in the format 'organizations/{{org_name}}/envgroups/{{envgroup_name}}'.
        environment (str): The resource ID of the environment.
    """
    _type = 'google_apigee_envgroup_attachment'
    
    def __init__(self,
        tf_id: str,
        envgroup_id:str,
        environment:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if envgroup_id is not None:
                kwargs['envgroup_id'] = envgroup_id
            if environment is not None:
                kwargs['environment'] = environment
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
