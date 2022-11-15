
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class RawDiskItem():
        source:str
        # non-optional-blocks
        container_type: Optional[str] = None
        sha1: Optional[str] = None
        
# wrapper list class
class RawDisk(BlockList):
        items: List[RawDiskItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeImage(ResourceObject):
    """    
    Args:
        name (str): 
    """
    _type = 'google_compute_image'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disk_size_gb: Optional[float] = None,
        family: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        licenses: Optional[List[str]] = None,
        project: Optional[str] = None,
        source_disk: Optional[str] = None,
        raw_disk: Optional[RawDisk]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if disk_size_gb is not None:
                kwargs['disk_size_gb'] = disk_size_gb
            if family is not None:
                kwargs['family'] = family
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if licenses is not None:
                kwargs['licenses'] = licenses
            if project is not None:
                kwargs['project'] = project
            if source_disk is not None:
                kwargs['source_disk'] = source_disk
            if raw_disk is not None:
                kwargs['raw_disk'] = raw_disk
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
