
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DiskEncryptionKeyItem():
        # non-optional-blocks
        raw_key: Optional[str] = None
        
# wrapper list class
class DiskEncryptionKey(BlockList):
        items: List[DiskEncryptionKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceSnapshotEncryptionKeyItem():
        # non-optional-blocks
        raw_key: Optional[str] = None
        
# wrapper list class
class SourceSnapshotEncryptionKey(BlockList):
        items: List[SourceSnapshotEncryptionKeyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRegionDisk(ResourceObject):
    """    
    Args:
        name (str): 
        replica_zones (List[str]): 
    """
    _type = 'google_compute_region_disk'
    
    def __init__(self,
        tf_id: str,
        name:str,
        replica_zones:List[str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        physical_block_size_bytes: Optional[float] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        size: Optional[float] = None,
        snapshot: Optional[str] = None,
        type: Optional[str] = None,
        disk_encryption_key: Optional[DiskEncryptionKey]=None,
        source_snapshot_encryption_key: Optional[SourceSnapshotEncryptionKey]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if replica_zones is not None:
                kwargs['replica_zones'] = replica_zones
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if physical_block_size_bytes is not None:
                kwargs['physical_block_size_bytes'] = physical_block_size_bytes
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if size is not None:
                kwargs['size'] = size
            if snapshot is not None:
                kwargs['snapshot'] = snapshot
            if type is not None:
                kwargs['type'] = type
            if disk_encryption_key is not None:
                kwargs['disk_encryption_key'] = disk_encryption_key
            if source_snapshot_encryption_key is not None:
                kwargs['source_snapshot_encryption_key'] = source_snapshot_encryption_key
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
