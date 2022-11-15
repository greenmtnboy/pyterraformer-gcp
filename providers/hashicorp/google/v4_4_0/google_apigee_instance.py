
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




class GoogleApigeeInstance(ResourceObject):
    """    
    Args:
        location (str): Compute Engine location where the instance resides. For trial organization
                    subscriptions, the location must be a Compute Engine zone. For paid organization
                    subscriptions, it should correspond to a Compute Engine region.
        name (str): Resource ID of the instance.
        org_id (str): The Apigee Organization associated with the Apigee instance,
                    in the format 'organizations/{{org_name}}'.
    """
    _type = 'google_apigee_instance'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        org_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disk_encryption_key_name: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        peering_cidr_range: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if org_id is not None:
                kwargs['org_id'] = org_id
            if description is not None:
                kwargs['description'] = description
            if disk_encryption_key_name is not None:
                kwargs['disk_encryption_key_name'] = disk_encryption_key_name
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if peering_cidr_range is not None:
                kwargs['peering_cidr_range'] = peering_cidr_range
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
