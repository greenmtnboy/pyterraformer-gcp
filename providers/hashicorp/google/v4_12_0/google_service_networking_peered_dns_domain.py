
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
        read: Optional[str] = None




class GoogleServiceNetworkingPeeredDnsDomain(ResourceObject):
    """    
    Args:
        dns_suffix (str): The DNS domain name suffix of the peered DNS domain.
        name (str): Name of the peered DNS domain.
        network (str): Network in the consumer project to peer with.
    """
    _type = 'google_service_networking_peered_dns_domain'
    
    def __init__(self,
        tf_id: str,
        dns_suffix:str,
        name:str,
        network:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        service: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dns_suffix is not None:
                kwargs['dns_suffix'] = dns_suffix
            if name is not None:
                kwargs['name'] = name
            if network is not None:
                kwargs['network'] = network
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if service is not None:
                kwargs['service'] = service
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
