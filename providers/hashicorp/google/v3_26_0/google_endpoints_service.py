
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




class GoogleEndpointsService(ResourceObject):
    """    
    Args:
        service_name (str): 
    """
    _type = 'google_endpoints_service'
    
    def __init__(self,
        tf_id: str,
        service_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        grpc_config: Optional[str] = None,
        id: Optional[str] = None,
        openapi_config: Optional[str] = None,
        project: Optional[str] = None,
        protoc_output_base64: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if service_name is not None:
                kwargs['service_name'] = service_name
            if grpc_config is not None:
                kwargs['grpc_config'] = grpc_config
            if id is not None:
                kwargs['id'] = id
            if openapi_config is not None:
                kwargs['openapi_config'] = openapi_config
            if project is not None:
                kwargs['project'] = project
            if protoc_output_base64 is not None:
                kwargs['protoc_output_base64'] = protoc_output_base64
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
