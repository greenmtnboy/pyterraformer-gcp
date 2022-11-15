
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




class GooglePubsubLiteReservation(ResourceObject):
    """    
    Args:
        name (str): Name of the reservation.
        throughput_capacity (float): The reserved throughput capacity. Every unit of throughput capacity is
                    equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed
                    messages.
    """
    _type = 'google_pubsub_lite_reservation'
    
    def __init__(self,
        tf_id: str,
        name:str,
        throughput_capacity:float,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if throughput_capacity is not None:
                kwargs['throughput_capacity'] = throughput_capacity
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
