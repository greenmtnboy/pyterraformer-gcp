
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class VpcAccessibleServicesItem():
        # non-optional-blocks
        allowed_services: Optional[List[str]] = None
        enable_restriction: Optional[bool] = None
        
# wrapper list class
class VpcAccessibleServices(BlockList):
        items: List[VpcAccessibleServicesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SpecItem():
        # non-optional-blocks
        access_levels: Optional[List[str]] = None
        resources: Optional[List[str]] = None
        restricted_services: Optional[List[str]] = None
        vpc_accessible_services: Optional[VpcAccessibleServices]=None,
        
# wrapper list class
class Spec(BlockList):
        items: List[SpecItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StatusItem():
        # non-optional-blocks
        access_levels: Optional[List[str]] = None
        resources: Optional[List[str]] = None
        restricted_services: Optional[Set[str]] = None
        vpc_accessible_services: Optional[VpcAccessibleServices]=None,
        
# wrapper list class
class Status(BlockList):
        items: List[StatusItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class ServicePerimetersItem():
        name:str
        title:str
        # non-optional-blocks
        description: Optional[str] = None
        perimeter_type: Optional[str] = None
        use_explicit_dry_run_spec: Optional[bool] = None
        vpc_accessible_services: Optional[VpcAccessibleServices]=None,
        spec: Optional[Spec]=None,
        status: Optional[Status]=None,
        
# wrapper list class
class ServicePerimeters(BlockSet):
        items: Set[ServicePerimetersItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAccessContextManagerServicePerimeters(ResourceObject):
    """    
    Args:
        parent (str): The AccessPolicy this ServicePerimeter lives in.
                    Format: accessPolicies/{policy_id}
    """
    _type = 'google_access_context_manager_service_perimeters'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        vpc_accessible_services: Optional[VpcAccessibleServices]=None,
        spec: Optional[Spec]=None,
        status: Optional[Status]=None,
        service_perimeters: Optional[ServicePerimeters]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if id is not None:
                kwargs['id'] = id
            if vpc_accessible_services is not None:
                kwargs['vpc_accessible_services'] = vpc_accessible_services
            if spec is not None:
                kwargs['spec'] = spec
            if status is not None:
                kwargs['status'] = status
            if service_perimeters is not None:
                kwargs['service_perimeters'] = service_perimeters
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
