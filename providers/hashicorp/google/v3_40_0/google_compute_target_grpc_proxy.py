
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




class GoogleComputeTargetGrpcProxy(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource
                    is created. The name must be 1-63 characters long, and comply
                    with RFC1035. Specifically, the name must be 1-63 characters long
                    and match the regular expression [a-z]([-a-z0-9]*[a-z0-9])? which
                    means the first character must be a lowercase letter, and all
                    following characters must be a dash, lowercase letter, or digit,
                    except the last character, which cannot be a dash.
    """
    _type = 'google_compute_target_grpc_proxy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        url_map: Optional[str] = None,
        validate_for_proxyless: Optional[bool] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if url_map is not None:
                kwargs['url_map'] = url_map
            if validate_for_proxyless is not None:
                kwargs['validate_for_proxyless'] = validate_for_proxyless
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
