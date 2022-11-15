
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PubsubItem():
        # non-optional-blocks
        topic: Optional[str] = None
        
# wrapper list class
class Pubsub(BlockList):
        items: List[PubsubItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudRunServiceItem():
        service:str
        # non-optional-blocks
        path: Optional[str] = None
        region: Optional[str] = None
        
# wrapper list class
class CloudRunService(BlockList):
        items: List[CloudRunServiceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GkeItem():
        cluster:str
        location:str
        namespace:str
        service:str
        # non-optional-blocks
        path: Optional[str] = None
        
# wrapper list class
class Gke(BlockList):
        items: List[GkeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DestinationItem():
        # non-optional-blocks
        cloud_function: Optional[str] = None
        workflow: Optional[str] = None
        cloud_run_service: Optional[CloudRunService]=None,
        gke: Optional[Gke]=None,
        
# wrapper list class
class Destination(BlockList):
        items: List[DestinationItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class MatchingCriteriaItem():
        attribute:str
        value:str
        # non-optional-blocks
        operator: Optional[str] = None
        
# wrapper list class
class MatchingCriteria(BlockSet):
        items: Set[MatchingCriteriaItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TransportItem():
        # non-optional-blocks
        pubsub: Optional[Pubsub]=None,
        
# wrapper list class
class Transport(BlockList):
        items: List[TransportItem]




class GoogleEventarcTrigger(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): Required. The resource name of the trigger. Must be unique within the location on the project.
    """
    _type = 'google_eventarc_trigger'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        service_account: Optional[str] = None,
        pubsub: Optional[Pubsub]=None,
        cloud_run_service: Optional[CloudRunService]=None,
        gke: Optional[Gke]=None,
        destination: Optional[Destination]=None,
        matching_criteria: Optional[MatchingCriteria]=None,
        timeouts: Optional[Timeouts]=None,
        transport: Optional[Transport]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if service_account is not None:
                kwargs['service_account'] = service_account
            if pubsub is not None:
                kwargs['pubsub'] = pubsub
            if cloud_run_service is not None:
                kwargs['cloud_run_service'] = cloud_run_service
            if gke is not None:
                kwargs['gke'] = gke
            if destination is not None:
                kwargs['destination'] = destination
            if matching_criteria is not None:
                kwargs['matching_criteria'] = matching_criteria
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if transport is not None:
                kwargs['transport'] = transport
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
