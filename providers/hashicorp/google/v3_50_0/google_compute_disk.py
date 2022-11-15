
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DiskEncryptionKeyItem():
        # non-optional-blocks
        kms_key_self_link: Optional[str] = None
        kms_key_service_account: Optional[str] = None
        raw_key: Optional[str] = None
        
# wrapper list class
class DiskEncryptionKey(BlockList):
        items: List[DiskEncryptionKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceImageEncryptionKeyItem():
        # non-optional-blocks
        kms_key_self_link: Optional[str] = None
        kms_key_service_account: Optional[str] = None
        raw_key: Optional[str] = None
        
# wrapper list class
class SourceImageEncryptionKey(BlockList):
        items: List[SourceImageEncryptionKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceSnapshotEncryptionKeyItem():
        # non-optional-blocks
        kms_key_self_link: Optional[str] = None
        kms_key_service_account: Optional[str] = None
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




class GoogleComputeDisk(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
    """
    _type = 'google_compute_disk'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        image: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        physical_block_size_bytes: Optional[float] = None,
        project: Optional[str] = None,
        size: Optional[float] = None,
        snapshot: Optional[str] = None,
        type: Optional[str] = None,
        zone: Optional[str] = None,
        disk_encryption_key: Optional[DiskEncryptionKey]=None,
        source_image_encryption_key: Optional[SourceImageEncryptionKey]=None,
        source_snapshot_encryption_key: Optional[SourceSnapshotEncryptionKey]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if image is not None:
                kwargs['image'] = image
            if labels is not None:
                kwargs['labels'] = labels
            if physical_block_size_bytes is not None:
                kwargs['physical_block_size_bytes'] = physical_block_size_bytes
            if project is not None:
                kwargs['project'] = project
            if size is not None:
                kwargs['size'] = size
            if snapshot is not None:
                kwargs['snapshot'] = snapshot
            if type is not None:
                kwargs['type'] = type
            if zone is not None:
                kwargs['zone'] = zone
            if disk_encryption_key is not None:
                kwargs['disk_encryption_key'] = disk_encryption_key
            if source_image_encryption_key is not None:
                kwargs['source_image_encryption_key'] = source_image_encryption_key
            if source_snapshot_encryption_key is not None:
                kwargs['source_snapshot_encryption_key'] = source_snapshot_encryption_key
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
