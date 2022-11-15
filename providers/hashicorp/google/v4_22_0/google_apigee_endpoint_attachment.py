
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




class GoogleApigeeEndpointAttachment(ResourceObject):
    """    
    Args:
        endpoint_attachment_id (str): ID of the endpoint attachment.
        location (str): Location of the endpoint attachment.
        org_id (str): The Apigee Organization associated with the Apigee instance,
                    in the format 'organizations/{{org_name}}'.
        service_attachment (str): Format: projects/*/regions/*/serviceAttachments/*
    """
    _type = 'google_apigee_endpoint_attachment'
    
    def __init__(self,
        tf_id: str,
        endpoint_attachment_id:str,
        location:str,
        org_id:str,
        service_attachment:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if endpoint_attachment_id is not None:
                kwargs['endpoint_attachment_id'] = endpoint_attachment_id
            if location is not None:
                kwargs['location'] = location
            if org_id is not None:
                kwargs['org_id'] = org_id
            if service_attachment is not None:
                kwargs['service_attachment'] = service_attachment
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
