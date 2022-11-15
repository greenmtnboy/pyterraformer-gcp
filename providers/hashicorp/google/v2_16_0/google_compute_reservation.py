
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GuestAcceleratorsItem():
        accelerator_count:float
        accelerator_type:str
        # non-optional-blocks
        
# wrapper list class
class GuestAccelerators(BlockList):
        items: List[GuestAcceleratorsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LocalSsdsItem():
        disk_size_gb:float
        # non-optional-blocks
        interface: Optional[str] = None
        
# wrapper list class
class LocalSsds(BlockList):
        items: List[LocalSsdsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InstancePropertiesItem():
        machine_type:str
        # non-optional-blocks
        min_cpu_platform: Optional[str] = None
        guest_accelerators: Optional[GuestAccelerators]=None,
        local_ssds: Optional[LocalSsds]=None,
        
# wrapper list class
class InstanceProperties(BlockList):
        items: List[InstancePropertiesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SpecificReservationItem():
        count:float
        # non-optional-blocks
        guest_accelerators: Optional[GuestAccelerators]=None,
        local_ssds: Optional[LocalSsds]=None,
        instance_properties: Optional[InstanceProperties]=None,
        
# wrapper list class
class SpecificReservation(BlockList):
        items: List[SpecificReservationItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleComputeReservation(ResourceObject):
    """    
    Args:
        name (str): 
        zone (str): 
    """
    _type = 'google_compute_reservation'
    
    def __init__(self,
        tf_id: str,
        name:str,
        zone:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        specific_reservation_required: Optional[bool] = None,
        guest_accelerators: Optional[GuestAccelerators]=None,
        local_ssds: Optional[LocalSsds]=None,
        instance_properties: Optional[InstanceProperties]=None,
        specific_reservation: Optional[SpecificReservation]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if zone is not None:
                kwargs['zone'] = zone
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if specific_reservation_required is not None:
                kwargs['specific_reservation_required'] = specific_reservation_required
            if guest_accelerators is not None:
                kwargs['guest_accelerators'] = guest_accelerators
            if local_ssds is not None:
                kwargs['local_ssds'] = local_ssds
            if instance_properties is not None:
                kwargs['instance_properties'] = instance_properties
            if specific_reservation is not None:
                kwargs['specific_reservation'] = specific_reservation
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
