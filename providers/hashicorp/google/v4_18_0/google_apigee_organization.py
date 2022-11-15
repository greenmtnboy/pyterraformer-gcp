
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




class GoogleApigeeOrganization(ResourceObject):
    """    
    Args:
        project_id (str): The project ID associated with the Apigee organization.
    """
    _type = 'google_apigee_organization'
    
    def __init__(self,
        tf_id: str,
        project_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        analytics_region: Optional[str] = None,
        authorized_network: Optional[str] = None,
        billing_type: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        runtime_database_encryption_key_name: Optional[str] = None,
        runtime_type: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if project_id is not None:
                kwargs['project_id'] = project_id
            if analytics_region is not None:
                kwargs['analytics_region'] = analytics_region
            if authorized_network is not None:
                kwargs['authorized_network'] = authorized_network
            if billing_type is not None:
                kwargs['billing_type'] = billing_type
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if runtime_database_encryption_key_name is not None:
                kwargs['runtime_database_encryption_key_name'] = runtime_database_encryption_key_name
            if runtime_type is not None:
                kwargs['runtime_type'] = runtime_type
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
