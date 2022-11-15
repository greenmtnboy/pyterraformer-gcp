
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




class GoogleDnsRecordSet(ResourceObject):
    """    
    Args:
        managed_zone (str): Identifies the managed zone addressed by this request.
        name (str): For example, www.example.com.
        type (str): One of valid DNS resource types. Possible values: ["A", "AAAA", "CAA", "CNAME", "DNSKEY", "DS", "IPSECVPNKEY", "MX", "NAPTR", "NS", "PTR", "SOA", "SPF", "SRV", "SSHFP", "TLSA", "TXT"]
    """
    _type = 'google_dns_record_set'
    
    def __init__(self,
        tf_id: str,
        managed_zone:str,
        name:str,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        rrdatas: Optional[List[str]] = None,
        ttl: Optional[float] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if managed_zone is not None:
                kwargs['managed_zone'] = managed_zone
            if name is not None:
                kwargs['name'] = name
            if type is not None:
                kwargs['type'] = type
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if rrdatas is not None:
                kwargs['rrdatas'] = rrdatas
            if ttl is not None:
                kwargs['ttl'] = ttl
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
