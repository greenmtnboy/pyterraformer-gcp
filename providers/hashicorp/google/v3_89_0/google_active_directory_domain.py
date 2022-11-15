
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




class GoogleActiveDirectoryDomain(ResourceObject):
    """    
    Args:
        domain_name (str): The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions, 
                    https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.
        locations (List[str]): Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/] 
                    e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.
        reserved_ip_range (str): The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. 
                    Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks
    """
    _type = 'google_active_directory_domain'
    
    def __init__(self,
        tf_id: str,
        domain_name:str,
        locations:List[str],
        reserved_ip_range:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        admin: Optional[str] = None,
        authorized_networks: Optional[Set[str]] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if domain_name is not None:
                kwargs['domain_name'] = domain_name
            if locations is not None:
                kwargs['locations'] = locations
            if reserved_ip_range is not None:
                kwargs['reserved_ip_range'] = reserved_ip_range
            if admin is not None:
                kwargs['admin'] = admin
            if authorized_networks is not None:
                kwargs['authorized_networks'] = authorized_networks
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
