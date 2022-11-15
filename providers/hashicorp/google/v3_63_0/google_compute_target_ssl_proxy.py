
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




class GoogleComputeTargetSslProxy(ResourceObject):
    """    
    Args:
        backend_service (str): A reference to the BackendService resource.
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
        ssl_certificates (List[str]): A list of SslCertificate resources that are used to authenticate
                    connections between users and the load balancer. At least one
                    SSL certificate must be specified.
    """
    _type = 'google_compute_target_ssl_proxy'
    
    def __init__(self,
        tf_id: str,
        backend_service:str,
        name:str,
        ssl_certificates:List[str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        proxy_header: Optional[str] = None,
        ssl_policy: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if backend_service is not None:
                kwargs['backend_service'] = backend_service
            if name is not None:
                kwargs['name'] = name
            if ssl_certificates is not None:
                kwargs['ssl_certificates'] = ssl_certificates
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if proxy_header is not None:
                kwargs['proxy_header'] = proxy_header
            if ssl_policy is not None:
                kwargs['ssl_policy'] = ssl_policy
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
