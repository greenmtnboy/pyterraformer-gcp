
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




class GoogleContainerAzureClient(ResourceObject):
    """    
    Args:
        application_id (str): Required. The Azure Active Directory Application ID.
        location (str): The location for the resource
        name (str): The name of this resource.
        tenant_id (str): Required. The Azure Active Directory Tenant ID.
    """
    _type = 'google_container_azure_client'
    
    def __init__(self,
        tf_id: str,
        application_id:str,
        location:str,
        name:str,
        tenant_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if application_id is not None:
                kwargs['application_id'] = application_id
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if tenant_id is not None:
                kwargs['tenant_id'] = tenant_id
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
