
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class TimeoutItem():
        # non-optional-blocks
        connect_timeout: Optional[str] = None
        max_attempts_timeout: Optional[str] = None
        response_timeout: Optional[str] = None
        
# wrapper list class
class Timeout(BlockList):
        items: List[TimeoutItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleNetworkServicesEdgeCacheOrigin(ResourceObject):
    """    
    Args:
        name (str): Name of the resource; provided by the client when the resource is created.
                    The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
                    and all following characters must be a dash, underscore, letter or digit.
        origin_address (str): A fully qualified domain name (FQDN) or IP address reachable over the public Internet, or the address of a Google Cloud Storage bucket.

                    This address will be used as the origin for cache requests - e.g. FQDN: media-backend.example.com IPv4:35.218.1.1 IPv6:[2607:f8b0:4012:809::200e] Cloud Storage: gs://bucketname

                    When providing an FQDN (hostname), it must be publicly resolvable (e.g. via Google public DNS) and IP addresses must be publicly routable.
                    If a Cloud Storage bucket is provided, it must be in the canonical "gs://bucketname" format. Other forms, such as "storage.googleapis.com", will be rejected.
    """
    _type = 'google_network_services_edge_cache_origin'
    
    def __init__(self,
        tf_id: str,
        name:str,
        origin_address:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        failover_origin: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        max_attempts: Optional[float] = None,
        port: Optional[float] = None,
        project: Optional[str] = None,
        protocol: Optional[str] = None,
        retry_conditions: Optional[List[str]] = None,
        timeout: Optional[Timeout]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if origin_address is not None:
                kwargs['origin_address'] = origin_address
            if description is not None:
                kwargs['description'] = description
            if failover_origin is not None:
                kwargs['failover_origin'] = failover_origin
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if max_attempts is not None:
                kwargs['max_attempts'] = max_attempts
            if port is not None:
                kwargs['port'] = port
            if project is not None:
                kwargs['project'] = project
            if protocol is not None:
                kwargs['protocol'] = protocol
            if retry_conditions is not None:
                kwargs['retry_conditions'] = retry_conditions
            if timeout is not None:
                kwargs['timeout'] = timeout
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
