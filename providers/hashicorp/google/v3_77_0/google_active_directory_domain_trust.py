
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




class GoogleActiveDirectoryDomainTrust(ResourceObject):
    """    
    Args:
        domain (str): The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions, 
                    https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.
        target_dns_ip_addresses (Set[str]): The target DNS server IP addresses which can resolve the remote domain involved in the trust.
        target_domain_name (str): The fully qualified target domain name which will be in trust with the current domain.
        trust_direction (str): The trust direction, which decides if the current domain is trusted, trusting, or both. Possible values: ["INBOUND", "OUTBOUND", "BIDIRECTIONAL"]
        trust_handshake_secret (str): The trust secret used for the handshake with the target domain. This will not be stored.
        trust_type (str): The type of trust represented by the trust resource. Possible values: ["FOREST", "EXTERNAL"]
    """
    _type = 'google_active_directory_domain_trust'
    
    def __init__(self,
        tf_id: str,
        domain:str,
        target_dns_ip_addresses:Set[str],
        target_domain_name:str,
        trust_direction:str,
        trust_handshake_secret:str,
        trust_type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        selective_authentication: Optional[bool] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if domain is not None:
                kwargs['domain'] = domain
            if target_dns_ip_addresses is not None:
                kwargs['target_dns_ip_addresses'] = target_dns_ip_addresses
            if target_domain_name is not None:
                kwargs['target_domain_name'] = target_domain_name
            if trust_direction is not None:
                kwargs['trust_direction'] = trust_direction
            if trust_handshake_secret is not None:
                kwargs['trust_handshake_secret'] = trust_handshake_secret
            if trust_type is not None:
                kwargs['trust_type'] = trust_type
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if selective_authentication is not None:
                kwargs['selective_authentication'] = selective_authentication
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
