
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




class GoogleBigqueryReservation(ResourceObject):
    """    
    Args:
        name (str): The name of the reservation. This field must only contain alphanumeric characters or dash.
        slot_capacity (float): Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the
                    unit of parallelism. Queries using this reservation might use more slots during runtime if ignoreIdleSlots is set to false.
    """
    _type = 'google_bigquery_reservation'
    
    def __init__(self,
        tf_id: str,
        name:str,
        slot_capacity:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ignore_idle_slots: Optional[bool] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if slot_capacity is not None:
                kwargs['slot_capacity'] = slot_capacity
            if id is not None:
                kwargs['id'] = id
            if ignore_idle_slots is not None:
                kwargs['ignore_idle_slots'] = ignore_idle_slots
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
