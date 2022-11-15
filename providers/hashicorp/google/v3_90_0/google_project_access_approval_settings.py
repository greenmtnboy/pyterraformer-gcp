
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class EnrolledServicesItem():
        cloud_product:str
        # non-optional-blocks
        enrollment_level: Optional[str] = None
        
# wrapper list class
class EnrolledServices(BlockSet):
        items: Set[EnrolledServicesItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleProjectAccessApprovalSettings(ResourceObject):
    """    
    Args:
        project_id (str): ID of the project of the access approval settings.
    """
    _type = 'google_project_access_approval_settings'
    
    def __init__(self,
        tf_id: str,
        project_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        notification_emails: Optional[Set[str]] = None,
        project: Optional[str] = None,
        enrolled_services: Optional[EnrolledServices]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if project_id is not None:
                kwargs['project_id'] = project_id
            if id is not None:
                kwargs['id'] = id
            if notification_emails is not None:
                kwargs['notification_emails'] = notification_emails
            if project is not None:
                kwargs['project'] = project
            if enrolled_services is not None:
                kwargs['enrolled_services'] = enrolled_services
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
