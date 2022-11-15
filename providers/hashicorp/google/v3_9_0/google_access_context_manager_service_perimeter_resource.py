
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




class GoogleAccessContextManagerServicePerimeterResource(ResourceObject):
    """    
    Args:
        perimeter_name (str): The name of the Service Perimeter to add this resource to.
        resource (str): A GCP resource that is inside of the service perimeter.
                    Currently only projects are allowed.
                    Format: projects/{project_number}
    """
    _type = 'google_access_context_manager_service_perimeter_resource'
    
    def __init__(self,
        tf_id: str,
        perimeter_name:str,
        resource:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if perimeter_name is not None:
                kwargs['perimeter_name'] = perimeter_name
            if resource is not None:
                kwargs['resource'] = resource
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
