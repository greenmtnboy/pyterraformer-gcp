
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




class GoogleBigqueryReservationAssignment(ResourceObject):
    """    
    Args:
        assignee (str): The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        job_type (str): Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        reservation (str): The reservation for the resource
    """
    _type = 'google_bigquery_reservation_assignment'
    
    def __init__(self,
        tf_id: str,
        assignee:str,
        job_type:str,
        reservation:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if assignee is not None:
                kwargs['assignee'] = assignee
            if job_type is not None:
                kwargs['job_type'] = job_type
            if reservation is not None:
                kwargs['reservation'] = reservation
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
