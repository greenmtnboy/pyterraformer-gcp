
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleDnsRecordSet(ResourceObject):
    """    
    Args:
        managed_zone (str): The name of the zone in which this record set will reside.
        name (str): The DNS name this record set will apply to.
        rrdatas (List[str]): The string data for the records in this record set whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding \" if you don't want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add \"\" inside the Terraform configuration string (e.g. "first255characters\"\"morecharacters").
        ttl (float): The time-to-live of this record set (seconds).
        type (str): The DNS record set type.
    """
    _type = 'google_dns_record_set'
    
    def __init__(self,
        tf_id: str,
        managed_zone:str,
        name:str,
        rrdatas:List[str],
        ttl:float,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        ):
            kwargs = {}
            if managed_zone is not None:
                kwargs['managed_zone'] = managed_zone
            if name is not None:
                kwargs['name'] = name
            if rrdatas is not None:
                kwargs['rrdatas'] = rrdatas
            if ttl is not None:
                kwargs['ttl'] = ttl
            if type is not None:
                kwargs['type'] = type
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
