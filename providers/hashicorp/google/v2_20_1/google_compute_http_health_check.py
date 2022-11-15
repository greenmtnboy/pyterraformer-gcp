
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




class GoogleComputeHttpHealthCheck(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035.  Specifically, the name must be 1-63 characters long and
                    match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means
                    the first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the
                    last character, which cannot be a dash.
    """
    _type = 'google_compute_http_health_check'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        check_interval_sec: Optional[float] = None,
        description: Optional[str] = None,
        healthy_threshold: Optional[float] = None,
        host: Optional[str] = None,
        id: Optional[str] = None,
        port: Optional[float] = None,
        project: Optional[str] = None,
        request_path: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        unhealthy_threshold: Optional[float] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if check_interval_sec is not None:
                kwargs['check_interval_sec'] = check_interval_sec
            if description is not None:
                kwargs['description'] = description
            if healthy_threshold is not None:
                kwargs['healthy_threshold'] = healthy_threshold
            if host is not None:
                kwargs['host'] = host
            if id is not None:
                kwargs['id'] = id
            if port is not None:
                kwargs['port'] = port
            if project is not None:
                kwargs['project'] = project
            if request_path is not None:
                kwargs['request_path'] = request_path
            if timeout_sec is not None:
                kwargs['timeout_sec'] = timeout_sec
            if unhealthy_threshold is not None:
                kwargs['unhealthy_threshold'] = unhealthy_threshold
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
