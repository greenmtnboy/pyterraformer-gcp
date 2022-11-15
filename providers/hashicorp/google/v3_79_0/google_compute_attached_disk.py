
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




class GoogleComputeAttachedDisk(ResourceObject):
    """    
    Args:
        disk (str): name or self_link of the disk that will be attached.
        instance (str): name or self_link of the compute instance that the disk will be attached to. If the self_link is provided then zone and project are extracted from the self link. If only the name is used then zone and project must be defined as properties on the resource or provider.
    """
    _type = 'google_compute_attached_disk'
    
    def __init__(self,
        tf_id: str,
        disk:str,
        instance:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        device_name: Optional[str] = None,
        id: Optional[str] = None,
        mode: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if disk is not None:
                kwargs['disk'] = disk
            if instance is not None:
                kwargs['instance'] = instance
            if device_name is not None:
                kwargs['device_name'] = device_name
            if id is not None:
                kwargs['id'] = id
            if mode is not None:
                kwargs['mode'] = mode
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
