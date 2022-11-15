
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class MethodSelectorsItem():
        # non-optional-blocks
        method: Optional[str] = None
        permission: Optional[str] = None
        
# wrapper list class
class MethodSelectors(BlockList):
        items: List[MethodSelectorsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OperationsItem():
        # non-optional-blocks
        service_name: Optional[str] = None
        method_selectors: Optional[MethodSelectors]=None,
        
# wrapper list class
class Operations(BlockList):
        items: List[OperationsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourcesItem():
        # non-optional-blocks
        access_level: Optional[str] = None
        resource: Optional[str] = None
        
# wrapper list class
class Sources(BlockList):
        items: List[SourcesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IngressFromItem():
        # non-optional-blocks
        identities: Optional[List[str]] = None
        identity_type: Optional[str] = None
        sources: Optional[Sources]=None,
        
# wrapper list class
class IngressFrom(BlockList):
        items: List[IngressFromItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IngressToItem():
        # non-optional-blocks
        resources: Optional[List[str]] = None
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        
# wrapper list class
class IngressTo(BlockList):
        items: List[IngressToItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EgressFromItem():
        # non-optional-blocks
        identities: Optional[List[str]] = None
        identity_type: Optional[str] = None
        
# wrapper list class
class EgressFrom(BlockList):
        items: List[EgressFromItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EgressToItem():
        # non-optional-blocks
        resources: Optional[List[str]] = None
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        
# wrapper list class
class EgressTo(BlockList):
        items: List[EgressToItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EgressPoliciesItem():
        # non-optional-blocks
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        egress_from: Optional[EgressFrom]=None,
        egress_to: Optional[EgressTo]=None,
        
# wrapper list class
class EgressPolicies(BlockList):
        items: List[EgressPoliciesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IngressPoliciesItem():
        # non-optional-blocks
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        sources: Optional[Sources]=None,
        ingress_from: Optional[IngressFrom]=None,
        ingress_to: Optional[IngressTo]=None,
        
# wrapper list class
class IngressPolicies(BlockList):
        items: List[IngressPoliciesItem]




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
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        sources: Optional[Sources]=None,
        ingress_from: Optional[IngressFrom]=None,
        ingress_to: Optional[IngressTo]=None,
        egress_from: Optional[EgressFrom]=None,
        egress_to: Optional[EgressTo]=None,
        egress_policies: Optional[EgressPolicies]=None,
        ingress_policies: Optional[IngressPolicies]=None,
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
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        sources: Optional[Sources]=None,
        ingress_from: Optional[IngressFrom]=None,
        ingress_to: Optional[IngressTo]=None,
        egress_from: Optional[EgressFrom]=None,
        egress_to: Optional[EgressTo]=None,
        egress_policies: Optional[EgressPolicies]=None,
        ingress_policies: Optional[IngressPolicies]=None,
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
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        sources: Optional[Sources]=None,
        ingress_from: Optional[IngressFrom]=None,
        ingress_to: Optional[IngressTo]=None,
        egress_from: Optional[EgressFrom]=None,
        egress_to: Optional[EgressTo]=None,
        egress_policies: Optional[EgressPolicies]=None,
        ingress_policies: Optional[IngressPolicies]=None,
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
        method_selectors: Optional[MethodSelectors]=None,
        operations: Optional[Operations]=None,
        sources: Optional[Sources]=None,
        ingress_from: Optional[IngressFrom]=None,
        ingress_to: Optional[IngressTo]=None,
        egress_from: Optional[EgressFrom]=None,
        egress_to: Optional[EgressTo]=None,
        egress_policies: Optional[EgressPolicies]=None,
        ingress_policies: Optional[IngressPolicies]=None,
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
            if method_selectors is not None:
                kwargs['method_selectors'] = method_selectors
            if operations is not None:
                kwargs['operations'] = operations
            if sources is not None:
                kwargs['sources'] = sources
            if ingress_from is not None:
                kwargs['ingress_from'] = ingress_from
            if ingress_to is not None:
                kwargs['ingress_to'] = ingress_to
            if egress_from is not None:
                kwargs['egress_from'] = egress_from
            if egress_to is not None:
                kwargs['egress_to'] = egress_to
            if egress_policies is not None:
                kwargs['egress_policies'] = egress_policies
            if ingress_policies is not None:
                kwargs['ingress_policies'] = ingress_policies
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
            
        
        
